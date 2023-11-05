class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        list1 = num1.split("+")
        list2 = num2.split("+")
        r1 = int(list1[0])
        r2 = int(list2[0])
        i1 = int(list1[1][:-1])
        i2 = int(list2[1][:-1])
        r = r1 * r2 - i1 * i2
        i = i1 * r2 + i2 * r1
        a = str(r) + "+" + str(i) + "i"
        return a