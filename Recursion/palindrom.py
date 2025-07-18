# def is_palindrom(s):

#   # base case
#   if len(s) == 1 or len(s) == 0: 
#     return True
  
#   if s[0] != s[-1]:
#     return False
  
#   return is_palindrom(s[1 : -1])


# x = input("Enter a string : ")

# s = is_palindrom(x)

# if s:
#   print("Yes Plaindrom")
# else:
#   print("Not Palindrom")



def is_palindrome(s, depth=0):
    indent = "  " * depth
    print(f"{indent}is_palindrome({s})")

    if len(s) <= 1:
        print(f"{indent}✔️ Base case for '{s}' → return True")
        return True

    if s[0] != s[-1]:
        print(f"{indent}❌ Mismatch: {s[0]} != {s[-1]} → return False")
        return False

    print(f"{indent}✔️ Match: {s[0]} == {s[-1]}, checking {s[1:-1]}")
    result = is_palindrome(s[1:-1], depth + 1)
    print(f"{indent}⬅️ Returning {result} to caller for {s}")
    return result

is_palindrome("madam")