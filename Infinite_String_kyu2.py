
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
print(find_position("9181583541 21201"))



