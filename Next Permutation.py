class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return
        
        for i in range (len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
            #从后往前查找，找到前面比后面大的数字就进入下一个序列    
                for k in range(len(nums)-1,i,-1):
                    #定位比[i]大的最后面的一个数字，交换nums[i],nums[k]，交换完毕后将i位后面所有数字都sorted。
                    if nums[k] > nums[i]: 
                        nums[i],nums[k]=nums[k],nums[i]
                        nums[i+1:]=sorted(nums[i+1:])
                        break
                #进行完一次下一序列的操作后，将循环退出。
                break
            #如果到了i=0的时候，还在进行循环，代表还没进行操作，所以sort。    
            else:
                if i == 0:
                    nums.sort()

