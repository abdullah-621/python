name = ["masum","noman","shafi","nipu"]

name.append("rakib") # Adds an element at the end of the list

name.insert(3,"kalam") # Adds an element at the specified position

cars = ['Ford', 'BMW', 'Volvo']

name.extend(cars) # Add the elements of a list (or any iterable), to the end of the current list

x = cars.copy()
print(x)

y = cars.index("Volvo")   #  list-এ প্রথম যেই position-এ কোন value পাওয়া যায়, সেই index (অর্থাৎ অবস্থান) রিটার্ন করে।
print(y)

print(name.count("noman")) # ist-এ একটি নির্দিষ্ট element কয়বার আছে সেটা গণনা করে।

name.sort()
name.reverse()
name.remove("shafi")

print(name)

name.clear()
print(name)

