import sys
from tkinter.filedialog import askopenfile
from collections import Counter
from random import randint as rand

str_list = ["LoWLoWLoWLoWLoWLoWLoW","HiGhHiGhHiGhHiGhHiGhHiGh"]


def High(str1):
    return str1.upper()

def Low(str2):
    return str2.lower()

def Task1():
    lower_reg = ''.join(map(Low, str_list[0]))
    higher_reg = ''.join(map(High, str_list[1]))

    print('Original: ', str_list)
    print('High register: ', higher_reg)
    print('Low register: ', lower_reg)

def Task2():
    i = 0
    nums = []
    quantity = int(input('Enter a quantity of numbers: '))
    for j in range(0, quantity):
        nums.append(rand(1, 50))
    square = list(map(lambda x: x*x, nums))
    print('Original: ', nums)
    print('Square: ', square)


def Task3():
    j = 1
    while j != 0:
        try:
            j = int(input('Print - 1 If u want to use default file, or print - 2 if u want to open file, (0 == Exit): '))
        except:
            print("Incorrect") 
        else:
            if j == 1:
                filename = sys.argv[0]
                f = open(filename, 'r')
                txt=[word for line in f for word in line.split()]
                print(Counter([''.join(filter(str.isalpha, x.lower())) for x in txt if ''.join(filter(str.isalpha, x.lower()))]))
                f.close
            elif j == 2: 
                fopen = askopenfile(mode='r', filetypes=[('txt', '.txt')])
                if fopen is not None:
                    txt2=[word for line in fopen for word in line.split()]
                    print(Counter([''.join(filter(str.isalpha, x.lower())) for x in txt2 if ''.join(filter(str.isalpha, x.lower()))]))
                    fopen.close
                else:
                    return
            elif j == 0: 
                print("Exit...")#выход 
            else:
                print("Incorrect") 


def shortestsequencerange(*args):
    return range(min(map(len, args)))


def Task4():
    a = 'asdfgh'
    b = (10, 20, 30, 40)
    c = ((a[i], b[i])
    for i in shortestsequencerange(a, b) )

    for item in c:
        print(item)
    

def switch():#меню выбора
   t=1
   while t != 0: 
       try: 
        t = int(input(" \nTask1 => 1(изменение регистра); \nTask2 => 2(возведение в степень);\nTask3 => 3(поиск кол-ва повторяющихся слов в тексте); \nTask4 => 4(zip()); \nExit => 0 \nEnter task number: ")) 
       except: 
        print("Incorrect") 
       else: 
           if t == 1: 
            Task1()#изменение регистра 
           elif t == 2: 
            Task2()#возведение в степень
           elif t == 3: 
            Task3()#поиск кол-ва слов
           elif t == 4: 
            Task4()#zip
           elif t == 0: 
            print("Exit...")#выход из программы
           else: 
            print("Wrong task!")

switch()