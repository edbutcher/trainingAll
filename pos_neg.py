def pos_neg(a, b, negative):
  if a < 0 < b and not negative:
    return True
  elif a > 0 > b and not negative:
    return True
  elif (a, b < 0, 0) and negative:
    return True
  else:
    return False
print(pos_neg(-4, 5, True))
