
def calculateDigits(startNum,j):
    digit_sum = 0
    for i in range(1,len(str(startNum))):
        digit_sum += i * (10**i - 10**(i - 1))
    digit_sum += (startNum - 10**(len(str(startNum)) - 1) + 1) * len(str(startNum))
    digit_sum -= j
    return digit_sum
  

def find_position(string):
    # print(string)
    digits = 1
    res = []
    if string.replace("0","") == "":
        startNum = int("1" + string) - 1
        return calculateDigits(startNum,0) + 1
    while digits:
        for j in range(digits):
            if j > 0 and string[:j].replace('9',"") == "":
                checkNum = int(string[j:] + "0"* (digits - len(string) + j))  #j: where the first checkNum start.
                # print("way 1     " + str(checkNum))
       
            elif j + digits <= len(string):
                print(string[j: j+digits])
                checkNum = int(string[j: j+digits])
                print("way 2     " + str(checkNum))
            elif str(int(string[:j]) + 1).startswith(string[digits:]):                                                                              
                checkNum = int(string[j:digits] + str(int(string[:j]) + 1))
            else:
                # print("head  " + string[j:])
                # print("tail:  " + string[(len(string) - digits - 1):j])
                checkNum = int(string[j:] + string[(len(string) - digits):j]) + 1
            # print(checkNum)
            startNum = checkNum - 1
            if startNum < 0:
                continue
            checkStr = string[:j]
            print(f'digits:    {digits}')
            print(j)
            print(f'checkStr:    {checkStr}')
            print(f'checkNum:     {checkNum}')
            print(f'startNum:      {startNum}')
            if not str(startNum).endswith(checkStr):
                continue

            while len(checkStr) < len(string) + digits:
                checkStr += str(checkNum)
                checkNum += 1
            if checkStr.startswith(string):
                print(f'success startNum:  {startNum}' )
                print(j)
                res.append(calculateDigits(startNum,j))
                # print(startNum)
                #how many digits in total when startNum finishes
                # digit_sum = 0
                # for i in range(1,len(str(startNum))):
                #     digit_sum += i * (10**i - 10**(i - 1))
                # digit_sum += (startNum - 10**(len(str(startNum)) - 1) + 1) * len(str(startNum))
                # digit_sum -= j
                # print(res)
                
                continue
  
        if len(res) > 0:

            res.sort()
            print(res)
            return res[0]
        digits += 1

#6957586376885
print(calculateDigits(1815835412119,1))
print(find_position("918158354121201"))




        #     if not startNum.endswith(head):
        #       continue
        #     checkNum = int(startNum) +1
        #     i = digits * 2 - j
        #     digits_change = len(str(int(startNum) + 1))
        #     while i in range(digits,len(string)):
        #         nextNum = string[i:i + digits_change]
        #         print("net" + str(nextNum))
        #         if str(checkNum).startswith(nextNum):
        #           # print("so far so good")
        #           checkNum += 1
        #           i += digits_change
        #           digits_change = max(digits_change, len(str(checkNum)))
        #           if i >= len(string):
        #             num_before = int(startNum) - 1
        #             # print(num_before)
        #             digit_sum = 0
        #             for i in range(1,len(str(num_before))):
        #               digit_sum += i * (10**i - 10**(i - 1))
        #             digit_sum += (num_before - 10**(len(str(num_before)) - 1) + 1) * len(str(num_before))
        #             digit_sum += j 

        #             # print(digits)
        #             # print(digits_change)
        #             # print(digits)
        #             return digit_sum
        #         elif nextNum not in str(checkNum):
        #             break
        # digits += 1            

# print(find_position("9100"))


# def find_position(string):
#     #1314
#     #digit = 2
#     digits = 1
#     while digits:
#         for j in range(digits):  
#             # print("digits" + str(digits))#string[0] is the jth digit of the count number
#             startNum = str(int(string[digits - j: digits * 2 - j]) - 1)
#             print(f'startNum {startNum}')
#             head = string[:digits - j]
#             print(head)
#             if not startNum.endswith(head):
#               continue
#             checkNum = int(startNum) +1
#             i = digits * 2 - j
#             digits_change = len(str(int(startNum) + 1))
#             while i in range(digits,len(string)):
#                 nextNum = string[i:i + digits_change]
#                 print("net" + str(nextNum))
#                 if str(checkNum).startswith(nextNum):
#                   # print("so far so good")
#                   checkNum += 1
#                   i += digits_change
#                   digits_change = max(digits_change, len(str(checkNum)))
#                   if i >= len(string):
#                     num_before = int(startNum) - 1
#                     # print(num_before)
#                     digit_sum = 0
#                     for i in range(1,len(str(num_before))):
#                       digit_sum += i * (10**i - 10**(i - 1))
#                     digit_sum += (num_before - 10**(len(str(num_before)) - 1) + 1) * len(str(num_before))
#                     digit_sum += j 

#                     # print(digits)
#                     # print(digits_change)
#                     # print(digits)
#                     return digit_sum
#                 elif nextNum not in str(checkNum):
#                     break
#         digits += 1            

# print(find_position("9100"))

# t

# Testing for: 92135075102
# 92135075102
# 102102374717 should equal 1810456478

# Testing for: 918158354121201
# 918158354121201
# 1691766126420073 should equal 22494749246448
