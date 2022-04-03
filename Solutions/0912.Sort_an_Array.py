/*
Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

*/

#归并排序：NlogN
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        # ste p1: divide - 由于每次都是稳定取中间进行divide
        # 所以recursion tree的深度可以稳定在log(N)
        mid = len(nums) // 2
        leftArr = self.sortArray(nums[:mid])
        rightArr = self.sortArray(nums[mid:])
        
        #step2: conquer
        i, j, k = 0, 0, 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                nums[k] = leftArr[i]
                i += 1
                k += 1
            else:
                nums[k] = rightArr[j]
                j += 1
                k += 1
        while i < len(leftArr):
                nums[k] = leftArr[i]
                i += 1
                k += 1
        while j < len(rightArr):
                nums[k] = rightArr[j]
                j += 1
                k += 1      
        return nums
        

//归并排序
class Solution {
    public int[] sortArray(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }
        int[] temp = new int[nums.length];
        mergeSort(nums, 0, nums.length - 1, temp);
        return nums;
    }
    
    private void mergeSort(int[] nums, int start, int end, int[] temp) {
        if (start >= end) {
            return;
        }
        int left = start, right = end;
        int mid = (start + end) / 2;
        
        //先划分成左右两边的归并排序
        mergeSort(nums, start, mid, temp);
        mergeSort(nums, mid + 1, end, temp);
        merge(nums, start, end, temp);
    }
    
    //将两个排好序的数组合并成一个
    private void merge(int[] nums, int start, int end, int[] temp) {
        int middle = (start + end) / 2;
        int leftStart = start;
        int rightStart = middle + 1;
        int index = leftStart;
        
        while (leftStart <= middle && rightStart <= end) {
            if (nums[leftStart] < nums[rightStart]) {
                temp[index++] = nums[leftStart++];
                
            } else {
                temp[index++] = nums[rightStart++];
            }
        }
        
        while (leftStart <= middle) {
            temp[index++] = nums[leftStart++];
        }
        
        while (rightStart <= end) {
            temp[index++] = nums[rightStart++];
        }
        
        for (int i = start; i <= end; i++) {
            nums[i] = temp[i];
        }
    }
}


//快速排序
class Solution {
    public int[] sortArray(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return nums;
        }
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }
    
    private void quickSort(int[] nums, int start, int end) {
        if (start >= end) {
            return;
        }
        int left = start, right = end;
        
        //1.pivot, A[start], A[end]
        //get value not index
        int pivot = nums[(start + end) / 2]; 
        
        //2.left <= right not left < right
        while (left <= right) {
            //3.A[left] < pivot not <=
            while ((left <= right) && (nums[left] < pivot)) {
                left++;
            }
            while ((left <= right) && (nums[right] > pivot)) {
                right--;
            }
            //这里的判断别忘记了，因为left有可能>right
            if (left <= right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            } 
        }
        quickSort(nums, start, right);
        quickSort(nums, left, end);
    }
}




