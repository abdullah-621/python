class myclass:
  a = 0


s = myclass()

print(s.a) # print the class attribute because instant attribute does not exist
s.a = 10 # set the instant attribute
print(s.a) # print the instant attribute
print(myclass.a) # but instant attribute can not change class attribute