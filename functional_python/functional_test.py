
# use map and reduce :)
names = ['Mary', 'Isla', 'Sam']
name_length = map(len, ['Mary', 'Isla', 'Sam'])
print (name_length)

secret_names = map(hash, names)
secret_names

squares = map(lamda x : x * x , [0, 1, 2, 3, 4])