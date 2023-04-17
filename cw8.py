# l = [1, 2, 4, 2, 3, 3, 4, 4, 5]
# print("Original List: ", l)
# res = [*set(l)]
# print("List after removing duplicate data:  ", res)

# ----------------------------------------------------------- 

# init_dict = {'a': 11, 'b': 21, 'c': 19}
# print(init_dict)

# init_dict_second = dict(a=11, b=21, c=19)
# print(init_dict_second)

# init_dict_third = {k: v for k, v in (('a', 11), ('b', 21), ('c', 19))}
# print(init_dict_third)

Str="Lovely Professional University"
lower=0
upper=0
for i in Str:
      if(i.islower()):
            lower+=1
      else:
            upper+=1
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)