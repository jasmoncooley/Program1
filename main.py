def createNewFile(file,rightMarg,leftMarg):
  
  max =80
  length = 0
  margRSpace = " " * rightMarg
  margLSpace = " " * leftMarg
  t= open(file,"r+")
  f= open("DAT1.txt","w+")
  
  old = t.readlines()
  print(old)
  f.write(str(margLSpace))
  for line in old:
    for word in line.split():
      length += len(word) +1
      if len(margRSpace)+ length+ len(margLSpace) > max:
        length =0
        f.write(str(margRSpace))
        f.write(str('\n'))
        f.write(str(margLSpace))
        f.write(str(word)+ " ")
      else:
        f.write(str(word) + " ")
  
  
if __name__ == "__main__":
    createNewFile("data.txt",5,7)
  