# DSA — Indexul problemelor rezolvate

> Aplicația de studiu și quick start-ul sunt în [README.md](./README.md). Fișierul de față
> rămâne indexul problemelor și al teoriilor din repo.

Toate soluțiile tale sunt păstrate în folderul `problems/`, organizate pe **tipare**
(structura NeetCode 150). Numărul din tabel e ID-ul LeetCode. Variantele brute /
alternative sunt în `problems/old/`.

✅ = rezolvat și categorisit.

## Structura folderului
```
DSA/
├── README.md          → aplicația de studiu + quick start
├── PROBLEMS.md        → indexul de față
├── STUDY_PLAN.md      → planul de studiu + ritm
├── STRUCTURI.md       → referință: structuri de date (cu explicație)
├── TEHNICI.md         → referință: tehnici/algoritmi (cu explicație)
├── structures/        → cod cu OOP: fiecare structură ca o clasă
├── functions/         → cod fără OOP: aceleași structuri ca funcții (practic)
├── practice/          → exerciții: 3 probleme per concept, enunțuri în engleză
├── learning/          → memorare: aplicație file-driven (drills + probleme + graf) + CLI
└── problems/          → toate soluțiile, grupate pe tipare
```

## Learning area (memorare)

`learning/` e locul unde repeți din memorie, nu unde scrii soluții întregi:

```bash
python3 learning/study/serve.py        # serverul de conținut (rămâne pornit)
# deschide http://127.0.0.1:8765/  ·  /#solve  ·  /#graph

python3 learning/trainer.py            # 10 carduri scadente (SM-2), în terminal
python3 learning/trainer.py --stats    # progres pe concepte
python3 learning/slicing.py            # quiz: prezice output-ul feliilor
```

Detalii: [`learning/README.md`](./learning/README.md) și
[`learning/PYTHON_SLICING.md`](./learning/PYTHON_SLICING.md).

## Array & Hashing
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 1 | Two Sum | `problems/array_hashing/two_sum.py` | ✅ |
| 49 | Group Anagrams | `problems/array_hashing/group_anagrams.py` | ✅ |
| 128 | Longest Consecutive Sequence | `problems/array_hashing/longest_consecutive_sequence.py` | ✅ |
| 217 | Contains Duplicate | `problems/array_hashing/contains_duplicate.py` | ✅ |
| 238 | Product of Array Except Self | `problems/array_hashing/product_of_array_except_self.py` | ✅ |
| 242 | Valid Anagram | `problems/array_hashing/valid_anagram.py` | ✅ |
| 271 | Encode and Decode Strings | `problems/array_hashing/encode_and_decode_strings.py` | ✅ |
| 347 | Top K Frequent Elements | `problems/array_hashing/top_k_frequent_elements.py` | ✅ |

ℹ️ În `problems/old/` mai sunt variante vechi pentru: Two Sum (`twosum.py`), Contains Duplicate (`containsduplicate.py`), Valid Anagram (`validanagram.py`), Product of Array Except Self (`productofarrayexceptself.py`).

## Two Pointers
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 15 | 3Sum | `problems/two_pointers/3sum.py` | ✅ |
| 11 | Container With Most Water | `problems/two_pointers/container_with_most_water.py` | ✅ |
| 125 | Valid Palindrome | `problems/two_pointers/valid_palindrome.py` | ✅ |

ℹ️ În `problems/old/`: 3Sum variantă veche (`triplesumtozero.py`).

## Sliding Window
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 3 | Longest Substring Without Repeating Characters | `problems/sliding_window/longest_substring_without_repeating.py` | ✅ |
| 76 | Minimum Window Substring | `problems/sliding_window/minimum_window_substring.py` | ✅ |
| 121 | Best Time to Buy and Sell Stock | `problems/sliding_window/best_time_to_buy_or_sell.py` | ✅ |
| 424 | Longest Repeating Character Replacement | `problems/sliding_window/longest_repeating_character_replacement.py` | ✅ |
| — (Grokking) | Maximum Sum Subarray of Size K | `problems/sliding_window/max_sum_subarray_size_k.py` | ✅ |

ℹ️ În `problems/old/`: Best Time to Buy and Sell Stock variantă veche (`besttimetobuyorsell.py`).

## Merge Intervals
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 56 | Merge Intervals | `problems/merge_intervals/merge_intervals.py` | ✅ |

## Stack
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 20 | Valid Parentheses | `problems/04.stack/valid_parentheses.py` | ✅ |

ℹ️ În `problems/old/`: variantă veche (`validpharanteses.py` — are un bug la `mapping`).

## Binary Search
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 33 | Search in Rotated Sorted Array | `problems/05.binary_search/search_in_rotated_sorted_array.py` | ✅ |
| 153 | Find Minimum in Rotated Sorted Array | `problems/05.binary_search/find_minimum_in_rotated_sorted_array.py` | ✅ |

ℹ️ În `problems/old/`: Search in Rotated Sorted Array variantă veche (`searchinrotatedsortedarray.py`).

## Linked List
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 19 | Remove Nth Node From End of List | `problems/06.linked_list/remove_nth_node_from_end.py` | ✅ |
| 141 | Linked List Cycle | `problems/06.linked_list/linked_list_cycle.py` | ✅ |
| 143 | Reorder List | `problems/06.linked_list/reorder_list.py` | ✅ |
| 206 | Reverse Linked List | `problems/06.linked_list/reverse_linked_list.py` | ✅ |

## Trees
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 98 | Validate Binary Search Tree | `problems/07.trees/validate_bst.py` | ✅ |
| 100 | Same Tree | `problems/07.trees/sametree.py` | ✅ |
| 102 | Binary Tree Level Order Traversal | `problems/07.trees/bt_level_order_traversal.py` | ✅ |
| 104 | Maximum Depth of Binary Tree | `problems/07.trees/maximum_depth_bt.py` | ✅ |
| 105 | Construct Binary Tree from Preorder and Inorder | `problems/07.trees/construct_binary_tree_from_preorder_and_inorder_travelsal.py` | ✅ |
| 124 | Binary Tree Maximum Path Sum | `problems/07.trees/binary_tree_maximum_path_sum.py` | ✅ |
| 199 | Binary Tree Right Side View | `problems/07.trees/binary_tree_right_side_view.py` | ✅ |
| 226 | Invert Binary Tree | `problems/07.trees/invert_binary_tree.py` | ✅ |
| 230 | Kth Smallest Element in a BST | `problems/07.trees/kth_smallest_element_in_bst.py` | ✅ |
| 235 | Lowest Common Ancestor of a BST | `problems/07.trees/lowest_common_ancestor_bst.py` | ✅ |
| 297 | Serialize and Deserialize Binary Tree | `problems/07.trees/serialize_and_deserialize_bt.py` | ✅ |
| 572 | Subtree of Another Tree | `problems/07.trees/subtree_of_another_tree.py` | ✅ |

## Tries
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 208 | Implement Trie (Prefix Tree) | `problems/08.tries/implement_trie.py` | ✅ |
| 211 | Design Add and Search Words Data Structure | `problems/08.tries/design_and_add_search_words_ds.py` | ✅ |
| 212 | Word Search II | `problems/08.tries/word_search_2.py` | ✅ |

## Heap / Priority Queue
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 295 | Find Median from Data Stream | `problems/09.heap/find_median_from_data_stream.py` | ✅ |
| 703 | Kth Largest Element in a Stream | `problems/09.heap/kth_largest_element_in_stream.py` | ✅ |
| 1046 | Last Stone Weight | `problems/09.heap/last_stone_weight.py` | ✅ |

## Backtracking
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 39 | Combination Sum | `problems/10.backtracking/combination_sum.py` | ✅ |
| 79 | Word Search | `problems/10.backtracking/word_search.py` | ✅ |

## Graphs
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 133 | Clone Graph | `problems/11.graphs/clone_graph.py` | ✅ |
| 200 | Number of Islands | `problems/11.graphs/number_of_islands.py` | ✅ |
| 207 | Course Schedule | `problems/11.graphs/course_schedule.py` | ✅ |
| 261 | Graph Valid Tree | `problems/11.graphs/graph_valid_tree.py` | ✅ |
| 323 | Number of Connected Components | `problems/11.graphs/undirected_graph.py` | ✅ |
| 417 | Pacific Atlantic Water Flow | `problems/11.graphs/pacific_atlantic_water_flow.py` | ✅ |

## Advanced Graphs
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 269 | Alien Dictionary | `problems/12.advanced-graphs/alien-dictionary.py` | ✅ |

## 1-D Dynamic Programming
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 70 | Climbing Stairs | `problems/13.One-D-DP/climbing_stairs.py` | ✅ |
| 152 | Maximum Product Subarray | `problems/13.One-D-DP/maximum_product_subarray.py` | ✅ |
| 198 | House Robber | `problems/13.One-D-DP/house_robber.py` | ✅ |
| 213 | House Robber II | `problems/13.One-D-DP/house_robber2.py` | ✅ |

## 2-D Dynamic Programming
| LeetCode | Problemă | Fișier | Status |
|---|---|---|---|
| 62 | Unique Paths | `problems/14.Two-D-DP/unique_paths.py` | ✅ |
| 1143 | Longest Common Subsequence | `problems/14.Two-D-DP/longest_common_subsequence.py` | ✅ |

---

## Cum folosești acest index (recall activ, fără să memorezi)
1. La fiecare sesiune de exercițiu, alege **un singur tipar** din lista de mai sus.
2. Muta mental problema → scrie soluția din memorie → verifică → rescrie.
3. Bifează aici ce ai rescris corect. Nimic nu se pierde.

Referințe rapide:
- [`STRUCTURI.md`](./STRUCTURI.md) — structuri de date, cu explicație.
- [`structures/`](./structures/README.md) — cod cu OOP: fiecare structură ca o clasă.
- [`functions/`](./functions/README.md) — cod fără OOP: aceleași structuri ca funcții.
- [`TEHNICI.md`](./TEHNICI.md) — tehnici și algoritmi, cu explicație.
- [`practice/`](./practice/README.md) — exerciții: 3 probleme per concept, de rezolvat singur.
- [`learning/`](./learning/README.md) — memorare: aplicația de studiu din `study/`, flashcard-uri CLI + laborator de slicing.
- [`STUDY_PLAN.md`](./STUDY_PLAN.md) — planul complet și ritmul recomandat.
