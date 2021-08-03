# # У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz. До третьего необходимо досчитать от единицы.
#  Считая, надо выводить число. Если число кратно fizz - надо выводить F вместо числа. Если число кратно buzz - надо выводить B вместо числа.
#   Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число.

# Пример условия и результата:
# Введены числа 2, 5, 18
# Вывод должен быть таким:
 # 1 F 3 F B F 7 F 9 FB 11 F 13 F B F 17 F





fb = []

i = int(input())
j = int(input())
k = int(input())

for n in range(1, k +1):
    if not (n%i or n%j):
        fb.append(str('FB'))
    elif not n%i:
        fb.append(str('F'))
    elif not n%j:
        fb.append(str('B'))
    else:
        fb.append(str(n))
        
        ' '.join(fb)  	
# print (fb)

sfb = [str(n) for n in fb]
print(" " . join(sfb))
