def isUnique(st):
  chars = []
  for x in st:
    if x in chars:
      return False
    else:
      chars.append(x)
  return True  

print(isUnique("aabbc"));
print(isUnique("abc"));