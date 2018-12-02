def check_lines(a, b):
    if type(a) == str and type(b) == str:
            if a == b:
                return 1          
            elif b == 'learn':
                return 3
            elif len(a) > len(b):
                return 2
            else:
                print('Данное условие не заданно')
    else:
        return 0

print(check_lines(7,7))
print(check_lines(7,"hello"))
print(check_lines("sun",500))
print(check_lines("olyagolf","olyagolf"))
print(check_lines("olyagolf","golf"))
print(check_lines("sun","morning"))
print(check_lines("olyagolf","learn"))
print(check_lines("learn","learn"))

#C:\pr\lesson2>stroki.py
#0
#0
#0
#1
#2
#Данное условие не заданно
#None
#3
#1