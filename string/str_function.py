str = " abdullah al masum "

print(len(str))

print(str.endswith("ah"))

print(str.startswith("ad"))

print(str.capitalize()) # first word latter capital

print(str.title()) # all firsrt word latter capital

print(str.lower())

print(str.upper())

print(str.strip()) # Removes leading/trailing spaces

print(str.lstrip()) # Removes leading spaces

print(str.rstrip()) # Removes trailing spaces

print(str.replace("masum","noman")) # replace all occurence

print("*".join(['a','b','c'])) #list বা অন্য iterable‑এর সব element‑কে একটি string‑এ জুড়ে দেয়, একটি নির্দিষ্ট separator (বিভাজক) দিয়ে

print(str.find('al'))  # Finds index of first occurrence

print(str.rfind('a'))  # Finds index of last occurrence

print(str.index("al")) # Like find() but raises error if not found

c = "al al ma al al"
print(c.count('al'))  # Counts occurrences of substring

s = 'asd7654'
print(s.isalnum()) # check alphanumeric
print(s.isalpha()) # check al alphabetic
print(s.isdigit()) # check all digit

k = "asdf"
print(k.islower())
print(k.isupper())

num = "e4"
print(num.zfill(4)) # leading zero (0) যোগ করে দেয়, যতক্ষণ না সেটা নির্দিষ্ট length এ পৌঁছায়

u = 2
i = 3
o = u + i
print(u ,"+", i , "=" , o)
print(f"{u} + {i} = {o}")
print("{} + {} = {}".format(u,i,o))


data = "name:Abdullah , age:22"
print(data.split(",")) 
# split(",")	কমা দিয়ে ভাগ করবে
# split(" ")	স্পেস দিয়ে ভাগ করবে
# split("-")	ড্যাশ দিয়ে ভাগ করবে