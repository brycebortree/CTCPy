def urlify(str)
  new_str = ""

  for x in str:
    if x == " "
      new_str.append(%20)
    new_str.append(x)

  return new_str