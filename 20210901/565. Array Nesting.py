class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].
        You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:
        The first element in s[k] starts with the selection of the element nums[k] of index = k.
        The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
        We stop adding right before a duplicate element occurs in s[k].
        Return the longest length of a set s[k].
        
        ============
        1. Brute force search
        Time complexity = O(N+N^2+N^3+...+N^N) = O(N^N)
        
        ============
        2. Hold previous value as next index
        Time complexity = O(N^2)
        
        ============
        3. Don't use known value as first index of num in the looping
        Ex)
        nums = [5,4,0,3,1,6,2]
        s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}
        -> Don't calculate s[5], s[6] and s[2] because they should be the same length as s[0].
        -> So for the next step search s[1]
        s[1] = {nums[1], nums[4]} = {4, 1}
        -> Don't calculate s[4] because it should be the same length as s[1].
        -> So for the final step search s[3]
        s[3] = {nums[3]} = {3}
        
        Longest length of set s[k] is 4 as s[0].
        Time complexity = O(logN)?
        
        """
        
        # known_values = []
        # max_count = 0
        # for i in range(len(nums)):
        #     if i in known_values:
        #         continue
        #     else:
        #         k = i
        #         count = 0
        #         while True:
        #             known_values.append(k)
        #             k = nums[k]
        #             count += 1                  
        #             if k in known_values:
        #                 break
        #         if count > max_count:
        #             max_count = count
        # return max_count
    
        """
        Question
        When I submitted the above code, time exceeded at the last test case (855 / 856 test cases passed).
        Then I checked and run some times for the test case and aware that the time is not the same everytime.
        Moreover, Runtime range was around 3-10s. They are so different. Why?
        
        ============
        Solution
        I checked solution and list(boolean) is used there.
        So I changed "if i in known_values:" part to "if known_values[i]==1:".
        Then, Time Complexity was reduced and submit accepted.
        
        "in": O(N) -> X[i]==1: O(1)
        
        """

        known_values = [0]*len(nums)
        max_count = 0
        for i in range(len(nums)):
            if known_values[i]==1:
                continue
            else:
                k = i
                count = 0
                while True:
                    known_values[k] = 1
                    k = nums[k]
                    count += 1
                    if known_values[k]==1:
                        break
                if count > max_count:
                    max_count = count
        return max_count