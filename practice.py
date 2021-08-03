def prost(n):
    d=2 
    while n%d!=0: 
    	d+=1
        print(d==n) 
    return d==n 
print(prost(8))
if __name__ == '__main__':
	n=int(input())     
print(n)
squared = n ** 2
if prost(n)==True:
        
    print("число простое, квадрат равен :" , squared)
else:
    print("число составное")


def my_square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(my_square, numbers))

print(squared_numbers)

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Создать структуру данных для студентов из имен и фамилий, можно случайных. Придумать структуру данных, чтобы указывать, в какой группе учится студент 
# (Группы Python, FrontEnd, FullStack, Java). 
# Студент может учиться в нескольких группах. Затем вывести:

# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java


student_list = {'Lisitskiy Vladimir':['Python', 'Java'],
                'Michael Jackson':['Java'],
                'Leo Messi': ['FrontEnd'],
                'Albert Einstein':['FullStek'],
                'Mark Zuckerberg':['Python'],
                'Elon Musk':['FrontEnd', 'Java']}
for key, values in student_list.items():
	if len(values) >= 2:
		print("Cтудент", key, "учится в двух и более группах")
print()
for key, values in student_list.items():
	if "Java" in values and "Python" in values:
		print("Студент", key, "изучает Python и Java")
	elif "Java" in values:
		print("Студент", key, "изучает Java")
	elif "Python" in values:
		print("Студент", key, "изучает Python")
print()
for key, values in student_list.items():
	for group in values:
	if not "FrontEnd" in values:
		print("Студент", key, "не изучает фронтенд")



# Написать функцию перевода размеров женского белья из международного во все остальные. 
# Внтри функции нужно просто обращаться к правильно составленному словарю.
sizes = {
    'XXS': {'Russia': 42, 'Germany': 36, 'USA': 8, 'France': 38, 'UK': 24},
    'XS': {'Russia': 44, 'Germany': 38, 'USA': 10, 'France': 40, 'UK': 26},
    'S': {'Russia': 46, 'Germany': 40, 'USA': 12, 'France': 42, 'UK': 28},
    'M': {'Russia': 48, 'Germany': 42, 'USA': 14, 'France': 44, 'UK': 30},
    'L': {'Russia': 50, 'Germany': 44, 'USA': 16, 'France': 46, 'UK': 32},
    'XL': {'Russia': 52, 'Germany': 46, 'USA': 18, 'France': 48, 'UK': 34},
    'XXL': {'Russia': 54, 'Germany': 48, 'USA': 20, 'France': 50, 'UK': 36},
    'XXXL': {'Russia': 56, 'Germany': 50, 'USA': 22, 'France': 52, 'UK': 38}}

input_size = input("Input international size: ")
get_size = input("Convert to size: ")


def convert(size):
	key = get_size
	if key in sizes[input_size]:
		print(get_size, "size: ", sizes[input_size][get_size])
	else:
		print("size is not found")
			
convert(input_size)		