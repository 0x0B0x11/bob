#!/bin/python3
class MyClass:
	default_color = "green"
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def staticmethod(fn):           # декоратор
		def wrapper():
			print(f"-------- {fn()}\
 --------")
		return wrapper
	@staticmethod
	def ex_static_method1():
		 return "Вариант №1"
	@staticmethod
	def ex_static_method2():
		return "Вариант №2"
#	@staticmethod
	def ex_method(self):
		print("Периметр =", 2*(self.width+self.height))

if __name__ == "__main__":
    MyClass.ex_static_method1()
    m = MyClass(10, 20)             # задает класс с параметрами 10 и 20
    
    #MyClass.ex_method()            # ошибка
    m.ex_method()                   # выводит: "Периметр = 60"    
    MyClass.ex_static_method2()     # выводит: -------- Вариант №2 --------
    m.default_color = "red"         
    print(m.default_color, end=' ') # выводит: "red " без перевода строки
    print(MyClass.default_color)    # выводит: "green"