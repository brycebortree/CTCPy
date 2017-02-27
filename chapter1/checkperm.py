def isPerm(st1, st2):
  if len(st1) != len(st2):
    return False

  st1_chars = [];

  for x in st1:
    st1_chars.append(x)
  
  for y in st2:
    if y not in st1_chars:
      return False
      
  return True

print(isPerm("aabc", "abc"))
print(isPerm("sty", "stl"))
print(isPerm("holler", "relloh"))

