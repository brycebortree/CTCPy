def isPermPal(st):
  # if even, count up for one, count down for second 
  # counting for zeroes
  counter = {}
  once_times = 0;
  
  for x in st:
    counter[x] = st.count(x)
  
  if len(st) % 2 == 0:
    for y in counter:
      if counter[y] > 2:
        return False
  else:
    for y in counter:
      if counter[y] == 1:
        once_times += 1
    return once_times == 1

  return True
  
print(isPermPal("Taco cat"))
print(isPermPal("hello"))

#use counter next time
