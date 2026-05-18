numbers = [5,10,15,17,13,19]
sum = 0
for num in numbers:
    print(num)
    sum += num
print(sum)

text = 'Bangladesh'
for char in text:
    print(char)


# Range
for i in range(1, 11, 2):
    print(i)

friends = ['Shuvo', 'Billah', 'Nazmul', 'Shohan', 'Shoyon', 'Safin', 'Mridul', 'Alamin']
for idx, friend in enumerate(friends):
    print(idx, friend)

name = "sifat"
for idx, latter in enumerate(name):
    print(idx, latter)

text2 = "Hello World"
for idx, latter in enumerate(text2):
    print(idx, latter, text2)