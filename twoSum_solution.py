class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # total = 0
        length = len(nums)
        # destination = []
        for i in range(length):
            # print("i:",i)
            for j in range(i + 1, length):
                # 当前位置和之后的位置的数字的和
                # print("j:", j)
                if nums[i] + nums[j] == target:
                    # destination.append(j)
                    # destination.append(i)
                    # print(destination)
                    return (i, j)
                    break
                # else:
                # continue
            # break

        # print(total)


source = [2, 7, 12, 15]
# source = [3,2,4]
destination = []
# target_number = 9
target_number = 9
example = Solution()
pos_one, pos_two = example.twoSum(source, target_number)
destination.append(pos_one)
destination.append(pos_two)
print(destination)
