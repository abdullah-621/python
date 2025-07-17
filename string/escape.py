# Code	Result	
# \' => Single Quote	
# \\	=> Backslash	
# \n	=> New Line	
# \t	=> Tab	
# \b	=> Backspace	
# \r	=> Carriage Return	
# \f	=> Form Feed	
# \ooo	=> Octal value	
# \xhh	=> Hex value
a = "Hi my\\ name is\t masum \n i am a \"good\" boy ,\n I am a\b student, \n ,my home is joypurhat\r,my father\r is a farmer"
print(a)

import time

for i in range(5):
    print(f"\rLoading {i}", end="")
    time.sleep(1)
