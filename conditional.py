# in, not, not in, is, is not

num1 = 5
num2 = 9

if num1 > num2:
    print("5 এর বেশি")
elif num1 > 7:
    print("7 এর বেশি")
else:
    print("5 এর কম")

bd = True

# if bd is True:
#     print("Bangladesh is well noon country")
# else:
#     print("Bangladesh is not a rich courtry")

if bd is not True:
    print("Bangladesh is well noon country")
else:
    print("Bangladesh is not a rich courtry")

money = 9000

if money > 5000 and money < 9000:
    print("Cox's Bazar jabo")
    if money - 5000 == 2000:
        print("Sitakundo Jabo")
elif money > 8000:
    print("Bandarban jabo")
else:
    print("Tour Cancle")