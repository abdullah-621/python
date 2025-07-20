
with open("log.txt") as f:
  content = f.readlines()

lineNo = 1

# for i in content:
#   if not "python" in i:
#     lineNo += 1
#   else:
#     break

# print(f"Line no is : {lineNo}")


for i in content:
  if "python" in i:
    print("Python is present, line no : ",lineNo )
    break
  lineNo += 1

else:
 print("Python is not present")
