class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list_length = len(nums)
        half_length = int(list_length/2)
        print(list_length)
        print(list_length/2)
        print(half_length)

        for i in range(half_length):
            for j in range(half_length,list_length):
                # 因为前一部分或后一部分会有符合的条件
                print(nums[i],nums[j])
                if nums[i] + nums[j] == target:
                    # return i,j
                    print(nums[i],nums[j],target_number)
                 # else:
                    # print("No match")


source = [2,7,12,15]
# source = [3,2,4]
destination = []
# target_number = 9
target_number = 9
example = Solution()
example.twoSum(source,target_number)
# pos_one, pos_two = example.twoSum(source,target_number)
# destination.append(pos_one)
# destination.append(pos_two)
# print(destination)

