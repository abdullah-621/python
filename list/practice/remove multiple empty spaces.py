li = ["Hello   world", "   Python is  great  ", "   Extra  spaces here  "]

c = []

for string in li:
  s = string.split()
  # print(type(s))
  print(s)
  c.append(' '.join(s))  # list বা অন্য iterable‑এর সব element‑কে একটি string‑এ জুড়ে দেয়, একটি নির্দিষ্ট separator (বিভাজক) দিয়ে

print(c)