test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
repl_chr = '*'
ret_chr = 'G' 

res = [ele if ele == ret_chr else repl_chr for ele in test_list]

# for i in test_list:
#   if i != ret_chr:
#     res.append('*')
#   else:
#     res.append(i)

print(res)