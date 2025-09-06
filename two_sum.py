'''
two sum
Question 1 (Easy – Hash Map / Arrays)

👉 Problem:
You are given an array of integers nums and an integer target. Return the indices of the two numbers that add up to target.

Assume exactly one solution exists.

Do not use the same element twice.

Example:

Input: nums = [1, 3, 4, 2], target = 6
Output: [1, 2]   # because nums[1] + nums[2] = 3 + 4 = 7

'''



'''
solution)
1, 3, 4, 2 
1 and target -1 which is 5 
if 5 in dictionary's keys   
i.e dictinary.get(i,0) means if i has an entry in the dictionary, return its value; otherwise, return 0.
wait:
it was d.get(i,0)+1  means if i is already in the dictionary, increment its count by 1; otherwise, initialize its count to 1.
wait
its needed to check if target-i is in the dictionary

wait the if also not needed
only .get(i,0) is enough


'''


def two_sum(nums, target):
    d={}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]] , i]
        else:
            d[nums[i]]=i
    

print(two_sum([1,3,4,2],6))
        