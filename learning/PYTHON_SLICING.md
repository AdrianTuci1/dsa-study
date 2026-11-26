# Slicing în Python — `a[:1]`, `a[1][:]` și restul

> Răspunsul scurt: **`a[i:j]` construiește un obiect NOU de același tip, cu
> referințe la aceleași elemente (copie „superficială"), iar `a[1][:]` se
> citește de la stânga la dreapta: întâi `a[1]`, apoi `[:]` pe rezultat.**
> Nu are nicio legătură cu sintaxa specială pentru „al doilea argument".

## 1. Regula

```python
a[start:stop:step]
```

- ia elementele de la `start` **până la `stop`, exclusiv**;
- pasul implicit e `1`; direcția se schimbă dacă `step` e negativ;
- fiecare componentă e opțională: `a[:]`, `a[1:]`, `a[:2]`, `a[::2]`, `a[::-1]`;
- **nu aruncă niciodată `IndexError`**: limitele se taie la capetele listei;
- rezultatul e un obiect **nou** de același tip (`list` → `list`, `str` → `str`),
  dar elementele din interior sunt **aceleași obiecte** (copie superficială).

O imagine bună: feliezi o prăjitură — apare o farfurie nouă, dar bucățile sunt
aceleași bucăți.

## 2. Tabel cu `a = [10, 20, 30, 40, 50]`

| Expresie | Rezultat | De ce |
|---|---|---|
| `a[0]` | `10` | primul element (nu e felie) |
| `a[-1]` | `50` | ultimul element |
| `a[:1]` | `[10]` | de la 0 până la 1, exclusiv → **o listă cu un element** |
| `a[1:]` | `[20, 30, 40, 50]` | de la 1 până la capăt |
| `a[:]` | `[10, 20, 30, 40, 50]` | copie a listei |
| `a[1:4]` | `[20, 30, 40]` | 1, 2, 3 |
| `a[::2]` | `[10, 30, 50]` | din 2 în 2 |
| `a[::-1]` | `[50, 40, 30, 20, 10]` | inversată |
| `a[4:1]` | `[]` | `start` după `stop`, pas pozitiv → gol |
| `a[100:]` | `[]` | se taie la capăt, fără eroare |
| `a[-2:]` | `[40, 50]` | ultimele două |

## 3. `a[:1]` vs `a[1]` — diferența care produce bug-uri

```python
a = [10, 20, 30]
a[:1]   # [10]   -> listă cu 1 element
a[1]    # 20     -> elementul de pe poziția 1
```

`[:1]` înseamnă „o felie de lungime 1", nu „elementul 1". De aceea se scrie des
în cod recursive ca să iei „capul" listei ca listă:

```python
def solve(argument):
    if not argument:
        return
    head = argument[:1]   # [primul]  - listă
    rest = argument[1:]   # restul    - listă
```

Echivalent cu `head, rest = argument[:1], argument[1:]`, sau cu
`head, *rest = argument` (aici `head` e elementul, nu lista).

## 4. `a[1][:]` — se evaluează de la stânga la dreapta

```python
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

1. `a[1]` → `[4, 5, 6]` (al doilea rând);
2. `[:]` pe acel rând → **o copie nouă** a rândului: `[4, 5, 6]`.

Deci `a[1][:]` = „o copie a rândului 1". Important:

```python
a[1] is a[1][:]      # False  -> obiect nou
a[1][0] is a[1][:][0]  # True   -> elementele sunt aceleași obiecte
```

Dacă `a[1]` ar fi un string, `s[:]` returnează **chiar același string**
(stringurile sunt imutabile, deci copierea e inutilă):

```python
s = "python"
s[:] is s    # True
s[1][:]      # 'y'   (s[1] e 'y', felia completă a lui 'y' e tot 'y')
```

La fel:

| Expresie (cu `a` de mai sus) | Rezultat | Explicație |
|---|---|---|
| `a[1][:]` | `[4, 5, 6]` | copie a rândului 1 |
| `a[1][:1]` | `[4]` | primul element din rândul 1 |
| `a[:1][0]` | `[1, 2, 3]` | prima linie, apoi elementul 0 din ea |
| `a[1:][0]` | `[4, 5, 6]` | de la rândul 1 încolo, apoi primul |
| `a[:][1]` | `[4, 5, 6]` | copie a matricei, apoi rândul 1 |
| `a[0][::-1]` | `[3, 2, 1]` | primul rând inversat |

Reține ordinea: **fiecare `[...]` se aplică pe rezultatul din stânga lui.**
`a[1][:]` nu e „elementele 1.. din `a`", e „`[:]` pe `a[1]`".

## 5. Copie superficială: de ce contează la backtracking

```python
path = [1, 2]
res = []
res.append(path)      # BUG: pune referința
path.append(3)
res                   # [[1, 2, 3]]
```

```python
res = []
res.append(path[:])   # corect: copie la momentul respectiv
path.append(3)
res                   # [[1, 2]]
```

Aceleași două linii apar peste tot în soluții:

- backtracking: `res.append(path[:])`, niciodată `res.append(path)`;
- matrice: `matrix[:] = ...` (înlocuiește conținutul **în același obiect**,
  deci respectă cerința „in place");
- copiere de rânduri: `grid = [row[:] for row in matrix]` — dacă scrii
  `grid = matrix[:]`, rândurile sunt partajate și modificările „sar" între ele.

```python
copie = matrix[:]        # listă nouă, DAR aceleași rânduri
copie[0][0] = 99         # modifică și matrix[0][0]!
```

## 6. Capcane frecvente

1. **`b = a` nu copiază nimic** — două nume pentru același obiect.
   `b = a[:]` copiază un nivel; `b = [row[:] for row in a]` copiază două.
2. **`a[:1]` e listă, `a[1]` e element.** Dacă funcția așteaptă element, nu
   trimite felia.
3. **`a[1][:]` nu protejează elementele din interior** dacă acestea sunt
   mutabile: `b = a[1][:]` apoi `b[0].append(...)` modifică și `a`.
4. **`stepul 0` dă eroare**: `a[::0]` → `ValueError: slice step cannot be zero`.
5. **Slicing assignment** poate schimba lungimea listei:
   `a[:1] = [7, 8]` înlocuiește primul element cu două; `del a[1:3]` șterge.
6. **Pe stringuri, slicing-ul e „gratis"** (imutabil, nu se copiază realmente),
   dar pe liste mari `a[:]` chiar alocă.

## 7. Exersează

- `python3 learning/slicing.py` — quiz interactiv: prezice output-ul, apoi
  vezi explicația. Răspunsurile sunt calculate cu Python la rulare, deci nu pot
  fi greșite.
- `python3 learning/slicing.py --answers` — doar tabelul cu întrebări/răspunsuri.
- `python3 learning/slicing.py --verify` — self-check al laboratorului.
