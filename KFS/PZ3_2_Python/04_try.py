#!/bin/python3
try:
	a = input("Введите первое число: "); print(a)
	b = input("Введите второе число: "); print(b)
	result = int(a)/int(b)
except (ValueError, ZeroDivisionError): 
	print("Что-то пошло не так...")
else: 
	print("Результат a/b в квадрате: ", result**2)
finally: 
	x = 2; print("Операция выполнена.", x) 
    
