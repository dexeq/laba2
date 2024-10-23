print("Пример внутренней функции:")
def outer(out_param1, out_param2):
    def inner(in_param1, in_param2):
        return in_param1 + in_param2
    return inner(out_param1, out_param2)
print(outer(5,6))

print("пример без замыкания, где происходит работа со строкой, когда внутренняя функция добавляет текст в свой аргумент:")
def outer(out_param):
    def inner(in_param):
        return f'Outer def have value: {in_param}'
    return inner(out_param)
print(outer('TEST'))

print("Пример с использованием замыкания:")
def outer2(out_param):
    def inner2():
        return f'Outer def have value: {out_param}'
    return inner2
value = outer2('TEST')
print(value())