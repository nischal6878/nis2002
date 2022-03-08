def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "ti no yaw ysae ot dnif lliw nosrep yzal a esuacaeb boj drah ot nosrep yzal a esoohc I"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using loops) is : ",end="")
print (reverse(s))