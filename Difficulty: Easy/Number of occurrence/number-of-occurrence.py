class Solution:
    def lowerbound(self, arr, target):
        s = 0
        e = len(arr) - 1
        lb = len(arr)  # default to len(arr) for out-of-bounds
        while s <= e:
            mid = (s + e) // 2
            if arr[mid] >= target:
                lb = mid
                e = mid - 1
            else:
                s = mid + 1
        return lb

    def upperbound(self, arr, target):
        s = 0
        e = len(arr) - 1
        ub = len(arr)  # default to len(arr)
        while s <= e:
            mid = (s + e) // 2
            if arr[mid] > target:
                ub = mid
                e = mid - 1
            else:
                s = mid + 1
        return ub

    def countFreq(self, arr, target):
        x = self.lowerbound(arr, target)
        y = self.upperbound(arr, target)
        return y - x  # frequency is upper - lower
