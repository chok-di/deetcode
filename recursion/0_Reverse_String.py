# reverse a string recursively
def reverseString(str):
  if len(str) == 1:
    return str[0]
  return str[-1] + reverseString(str[:len(str) - 1])

print(reverseString("woody"))