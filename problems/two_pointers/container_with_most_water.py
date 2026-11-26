# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the 
#  line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        max_area = max(max_area, h * width)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result1 = maxArea(height1)
print("Output:", result1)

# Output: 49