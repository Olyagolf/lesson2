def job_for_age(age):
    if age is None :
        print('Значение не введено')
    elif age <= 0 :
        print('Вы еще не родились!')
    elif 0 < age < 8 :
        print('Вам нужно в детский сад')
    elif 8 <= age < 17:
        print('Вы должны ходить в школу')
    elif 17 <= age < 23:
        print('Вы должны учиться в институте')
    else:
        print('Арбайтен! Халява закончилась!')

age=input('Ваш возраст?')
try:
    age = int(age)
    answer=job_for_age(age)
except ValueError:
    print('Не число!')

