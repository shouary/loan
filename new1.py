lst=['1', '2' ,'3']
my_tuple=lst[:]
num='1'
new=tuple (num)
pos=2
my_tuple1=my_tuple[: pos-1]
my_tuple1+=new
my_tuple=my_tuple1+my_tuple[pos: ]
print(my_tuple)