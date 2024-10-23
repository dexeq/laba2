print("Определение и вызов функции")
print("Пример простейшей функции без параметров: ")
def example():
    print("Доброе утро!")
example()

print("Использование return: ")
def example():
    return True
example = example()
print(type(example))
print(example)