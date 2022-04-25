# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums)):
            for i in range(n + 1,len(nums)):
                if (nums[n] + nums[i] == target):
                    a = [n,i]
                    print(a)

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
def main():
    nums = [2,7,11,15]
    target = 9
    a = Solution()
    a.twoSum(nums,target)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
