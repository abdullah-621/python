import os
def genarated_table(n):
  table = ""
  for i in range(1 , 11):
    table += f"{i} X {n} = {i * n} \n"

  os.makedirs("tables", exist_ok=True)  # if tables forlder not exist 

  with open(f"tables/table_{n}.txt", "w") as t:
    t.write(table)

  
for i in range(2 , 21):
  genarated_table(i)
