immutable_var= 1,2,3, 'Urban',
print(immutable_var)
# immutable_var[1]=77
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
print(type(immutable_var))
mutable_list=['football' , 'cars' ,'student' ]
print(mutable_list)
mutable_list[1]='plane'
print(mutable_list)

