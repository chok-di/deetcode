# def smaller(arr):
#     print(arr)
#     res = []
#     sorted = []
#     def addnum(left,right,num):
#         if len(sorted) == 0 or num > sorted[-1]:
#             sorted.append(num)
#             return len(sorted) - 1
#         if num <= sorted[0]:
#             sorted.insert(0,num)
#             return 0
#         while left <= right:
#             mid = (left + right) // 2
#             if sorted[mid + 1]  < num:
#                 left = mid + 1
#             if sorted[mid] >= num:
#                 right = mid
#             if sorted[mid] < num and sorted[mid + 1] >= num:
#                 sorted.insert(mid + 1,num)
#                 return mid + 1
#     for i in range(len(arr) - 1, -1 ,-1):
#         print(arr[i])
#         if i == len(arr) - 1:
#             res.insert(0,addnum(0,len(sorted) - 1, arr[i]))
# #         elif arr[i] ==arr[i + 1]:
# #             res.insert(0,res[0])
#         elif arr[i] > arr[i + 1]:
#             res.insert(0,addnum(res[0], len(sorted) - 1, arr[i]))
#         elif arr[i] <= arr[i + 1]:
#             res.insert(0,addnum(0,res[0],arr[i]))
#         print(sorted)
#         print(res)
#     return res

def smaller(arr):
    arr_original = arr.copy()
    arr.sort()
    res = []
    def findIndex(left,right,num):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid]  < num:
                left = mid + 1
            if arr[mid] > num:
                right = mid - 1
            if arr[mid] == num:
              while arr[mid - 1] == num:
                mid -= 1
              arr.pop(mid)
              return mid
    for i in range(len(arr)):
        if i == len(arr) - 1:
            res.insert(0,findIndex(0,len(sorted) - 1, arr[i]))
        elif arr[i] > arr[i + 1]:
            res.insert(0,findIndex(res[0], len(sorted) - 1, arr[i]))
        elif arr[i] <= arr[i + 1]:
            res.insert(0,findIndex(0,res[0],arr[i]))
    return res


    def smaller(arr):
#     print(arr)
    arr_original = arr.copy()
    arr.sort()
    res = []
    def findIndex(left,right,num):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid]  < num:
                left = mid + 1
            if arr[mid] > num:
                right = mid - 1
            if arr[mid] == num:
                while mid > 0 and arr[mid - 1] == num:
                    mid -= 1
                arr.pop(mid)
                return mid
    for i in range(len(arr_original)):
#         print(res)
#         print
        if i == 0:
            res.append(findIndex(0,len(arr) - 1, arr_original[i]))
        elif arr_original[i] > arr_original[i - 1]:
            res.append(findIndex(res[i - 1],len(arr) - 1, arr_original[i]))
        elif arr_original[i] <= arr_original[i - 1]:
            res.append(findIndex(0,res[-1],arr_original[i]))
    return res