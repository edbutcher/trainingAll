def missing_char(str, n):
  if n == 0:
    return str[1:]
  elif n == 6:
    return str[0:5]
  else:
    return (str[0:n] + str[n+1:])


#def missing_char(str, n):
#  front = str[:n]   # up to but not including n
#  back = str[n+1:]  # n+1 through end of string
