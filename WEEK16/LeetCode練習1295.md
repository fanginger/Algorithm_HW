# LeetCode練習1295
## 1295. Find Numbers with Even Number of Digits

題目:
>Given an array nums of integers, return how many of them contain an even number of digits.
>
測資：
>Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.


時間：12:25-12:38

想法：
把數值轉換成str看是不是偶數個數就可以簡單辨別。

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num = 0
        for i in nums:
            temp = str(i)
            if len(temp)%2 ==0:
                num += 1
        return num

```