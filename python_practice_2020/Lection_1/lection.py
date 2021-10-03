age = int(input('How old are you?\n'))
x = age + 1
print('А я думал тебе ', x, ' ', sep='', end='')
if x >= 11 and x <= 19:
    print('лет')
else:
    if x % 10 == 1:
        print('год')
    else:
        if x % 10 >= 2 and x % 10 <= 4:
            print('года')
        else:
            print('лет')
