# import math
# def permutation_free(n, l):
    
#     if n == l:
#         ans = n**n - math.factorial(n)
#         return ans
    
#     bad_tail = math.factorial(n)
#     def danger_num(d):
#         if d == 1:
#             return 1
#         return danger_num(d-1) + (bad_perm(d - 1) - danger_num(d - 1)) * 2
#     def bad_perm(d): 
#         if d == 1:
#             return n - 1 
#         return danger_num(d-1) * (n-1) + (bad_perm(d-1) - danger_num(d-1)) * n
        
        
#     return (permutation_free(n,l-1) * n - bad_perm(l - n) * bad_tail) % 123456787


# import math
# def permutation_free(n, l):
#     bad_tail = math.factorial(n)
#     base = n**n - math.factorial(n)
#     danger_num = 1
#     bad_perm = n-1
#     for i in range(0,l - n):
#         new_danger_num = danger_num + (bad_perm - danger_num) * 2
#         new_bad_perm = danger_num * (n-1) +(bad_perm - danger_num) * n
#         base = base * n - bad_perm * bad_tail
#         danger_num = new_danger_num
#         bad_perm = new_bad_perm
#     return base % 123456787

def permutation_free(n,l):
    global res
    res = 0
    def add(string):
        global res
        if len(string) == l:
            res += 1
            return
        for num in range(1,n+1):
            string += str(num)
            if len(set(string[-n:])) != n:
                add(string)
            string = string[: -1]
    add("")
    return res
print(permutation_free(4,10))
