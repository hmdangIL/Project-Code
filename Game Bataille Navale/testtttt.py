dict={}
for i in range(15):
    key = str("x" + str(i))
    dict[key] = i
for key, value in dict.items():
    exec(f'{key}={value}')


print(x3)
