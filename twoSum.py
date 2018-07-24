class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(len(nums)):
                if (not (i == j)) and nums[i] + nums[j] == target:
                    return i,j
                 # else:
                    # print("No match")


source = [2,7,12,15]
# source = [3,2,4]
destination = []
# target_number = 9
target_number = 9
example = Solution()
pos_one, pos_two = example.twoSum(source,target_number)
destination.append(pos_one)
destination.append(pos_two)
print(destination)

