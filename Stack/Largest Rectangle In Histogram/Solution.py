from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #[0, 0, 1, 1, 1, 4]
        stack = []
        left_min_pos = [0]*len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left_min_pos[i] = 0 if not stack else stack[-1]+1
            stack.append(i)
        stack = []
        right_min_pos = [0]*len(heights)
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right_min_pos[i] = len(heights)-1 if not stack else stack[-1]-1
            stack.append(i)
        print(f"left: {left_min_pos} and right:{right_min_pos}")
        max_area=0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i]*(right_min_pos[i]-left_min_pos[i]+1))
        return max_area


# ============================================================================
# EXPLANATION OF YOUR SOLUTION (Two-Pass Method)
# ============================================================================
"""
YOUR SOLUTION ANALYSIS:
Time Complexity: O(n) - Each element is pushed/popped once per pass
Space Complexity: O(n) - For arrays and stack

Your approach is excellent! Here's how it works:

1. **First Pass (Left to Right)**: Find the leftmost boundary for each bar
   - For each bar at index i, find the leftmost position where all bars 
     have height >= heights[i]
   - Use a stack to maintain bars in increasing height order
   
2. **Second Pass (Right to Left)**: Find the rightmost boundary for each bar  
   - Similar logic but going from right to left
   - Find rightmost position where all bars have height >= heights[i]

3. **Calculate Areas**: For each bar, the maximum rectangle with that bar as 
   minimum height has width = right_boundary - left_boundary + 1

Example with [2,1,5,6,2,3]:
- Bar at index 2 (height=5): left=2, right=3, area = 5*(3-2+1) = 10
- This gives us the maximum rectangle of area 10
"""


class SinglePassStackSolution:
    """
    CLASSIC SINGLE-PASS O(N) STACK METHOD
    
    This is the most common textbook solution for this problem.
    """
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        KEY INSIGHT: Use a monotonic increasing stack
        
        The main idea:
        - Maintain a stack of indices with strictly increasing heights
        - When we encounter a bar shorter than the stack top, it means
          we cannot extend rectangles from previous taller bars anymore
        - Pop taller bars and calculate their maximum possible rectangle area
        
        How width calculation works:
        - Right boundary: current index (where height decreases)  
        - Left boundary: index right after the new stack top
        - If stack becomes empty, left boundary is 0 (beginning of array)
        
        Step-by-step for [2,1,5,6,2,3]:
        
        i=0, h=2: stack=[] -> stack=[0]
        i=1, h=1: h < heights[0], so pop 0
                  area = 2 * (1-(-1)-1) = 2 * 1 = 2
                  stack=[1]
        i=2, h=5: h > heights[1] -> stack=[1,2]  
        i=3, h=6: h > heights[2] -> stack=[1,2,3]
        i=4, h=2: h < heights[3], so pop 3
                  area = 6 * (4-2-1) = 6 * 1 = 6
                  h < heights[2], so pop 2  
                  area = 5 * (4-1-1) = 5 * 2 = 10 ← Maximum!
                  stack=[1,4]
        i=5, h=3: h > heights[4] -> stack=[1,4,5]
        
        Process remaining: areas for bars 1,4,5 extending to end
        """
        stack = []  # Stack stores indices
        max_area = 0
        
        for i, height in enumerate(heights):
            # Pop all bars taller than current height
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]  # Height of rectangle
                # Width: from position after new stack top to current position
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            
            stack.append(i)
        
        # Process remaining bars (they extend to the end of array)
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        return max_area


class OptimizedStackSolution:
    """
    OPTIMIZED SINGLE-PASS WITH SENTINEL VALUES
    
    Adding dummy values at start/end eliminates boundary condition handling.
    """
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Trick: Add 0 at beginning and end
        - Left sentinel (0) ensures stack never becomes empty during processing
        - Right sentinel (0) ensures all bars get processed
        
        This eliminates the need for separate logic to handle:
        1. Empty stack when calculating width
        2. Remaining bars in stack after main loop
        """
        # Add sentinels: [0, original_heights..., 0]
        heights = [0] + heights + [0]
        stack = [0]  # Start with left sentinel index
        max_area = 0
        
        for i in range(1, len(heights)):
            while heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1  # No need to check if stack is empty
                max_area = max(max_area, h * w)
            stack.append(i)
        
        return max_area


def demonstrate_all_methods():
    """
    Demonstrate all three approaches with step-by-step visualization.
    """
    print("=== LARGEST RECTANGLE IN HISTOGRAM - METHOD COMPARISON ===\n")
    
    test_heights = [2, 1, 5, 6, 2, 3]
    print(f"Input: {test_heights}")
    
    # Visual representation
    print("\nHistogram visualization:")
    max_h = max(test_heights)
    for level in range(max_h, 0, -1):
        row = f"{level} |"
        for h in test_heights:
            row += "██" if h >= level else "  "
        print(row)
    print("   " + "".join([f" {i}" for i in range(len(test_heights))]))
    
    # Test all methods
    original = Solution()
    single_pass = SinglePassStackSolution() 
    optimized = OptimizedStackSolution()
    
    result1 = original.largestRectangleArea(test_heights.copy())
    result2 = single_pass.largestRectangleArea(test_heights.copy())
    result3 = optimized.largestRectangleArea(test_heights.copy())
    
    print(f"\nResults:")
    print(f"Your two-pass method: {result1}")
    print(f"Single-pass stack: {result2}")  
    print(f"Optimized with sentinels: {result3}")
    print(f"Expected: 10 (rectangle at indices 2-3 with height 5)")
    
    print(f"\nAll methods agree: {result1 == result2 == result3}")


def compare_time_complexity():
    """
    Explain why all methods are O(n) despite different appearances.
    """
    print("\n=== TIME COMPLEXITY ANALYSIS ===")
    print("All three methods are O(n), here's why:")
    print()
    print("1. YOUR TWO-PASS METHOD:")
    print("   - Two separate O(n) passes")
    print("   - Each element pushed/popped at most once per pass")  
    print("   - Total: O(n) + O(n) = O(n)")
    print()
    print("2. SINGLE-PASS STACK METHOD:")
    print("   - One pass through array: O(n)")
    print("   - Each element pushed exactly once: O(n) total pushes")
    print("   - Each element popped at most once: O(n) total pops")
    print("   - Total: O(n)")
    print()
    print("3. OPTIMIZED WITH SENTINELS:")
    print("   - Same as single-pass but cleaner code")
    print("   - Sentinels eliminate conditional checks")
    print("   - Still O(n) time and space")


if __name__ == "__main__":
    demonstrate_all_methods()
    compare_time_complexity()
