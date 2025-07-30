# দুইটা সেটের সেই উপাদানগুলো যেগুলো শুধু একটার মধ্যে আছে, কিন্তু দুটোতেই একসাথে নেই

a = {1,2,3,4,5,6,7}
b  = {6,7,8,9,10}

c = a.symmetric_difference(b)
# c = a ^ b
print(c)

a.symmetric_difference_update(b)
# a ^= b
print(a)