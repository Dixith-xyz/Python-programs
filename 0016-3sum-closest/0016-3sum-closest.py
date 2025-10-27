class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the array. This is crucial for the two-pointer approach.
        nums.sort()
        n = len(nums)
        
        # Initialize closest_sum with the sum of the first three elements as a baseline.
        closest_sum = nums[0] + nums[1] + nums[2]

        # Step 2: Main loop to fix the first element of the triplet.
        for i in range(n - 2):
            # Step 3: Two-pointer squeeze on the rest of the array.
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we found a sum that is closer to the target, update our result.
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with the target.
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # If the sum is exactly the target, the difference is 0.
                    # This is the closest possible, so we can return immediately.
                    return target
        
        return closest_sum