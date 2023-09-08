import math

while True:
    border = "-" * 69

    print("\n", border)
    print("                             KALKULATOR\n")
    print("Fitur: penjumlahan, pengurangan, perkalian, pembagian, dan faktorial")
    print(border)
    
    operasi = input("Silahkan masukkan operasi matematika yang ingin dilakukan: ")
    hasil = None
    faktorial = None
    operator = '+'

#     def add(a, b):
#         return a + b

#     def subtract(a, b):
#         return a - b

#     def multiply(a, b):
#         return a * b

#     def divide(a, b):
#         if b != 0:
#             return a // b
#         else:
#             raise ZeroDivisionError("Error: Division by zero")

#     operators = {
#     '+': add,
#     '-': subtract,
#     '*': multiply,
#     '/': divide
# }

    # operasi = operasi.replace('x', '*')

    # if hasil_1 != 0:
    #     hasil //= hasil_1
    # else:
    #     raise ZeroDivisionError("Error")

    for i in operasi.split():
        if i in "+-*/":
            operator = i
        else:
            if i.endswith('!'):
                faktorial = int(i[:-1]) # done
            else:
                faktorial = None

            if faktorial is not None:
                hasil_1 = math.factorial(faktorial)
                if hasil is None:
                    hasil = hasil_1
                elif operator == '*':
                    hasil *= hasil_1
                elif operator == '/':
                    if hasil_1 != 0:
                        hasil //= hasil_1
                    else:
                        raise ZeroDivisionError("Error") # mau njajal "print('error')" tapi output e tetep '0'
                elif operator == '+':
                    hasil += hasil_1
                elif operator == '-':
                    hasil -= hasil_1
            else:
                temp = int(i)
                if hasil is None:
                    hasil = temp
                elif operator == '*':
                    hasil *= temp
                elif operator == '/':
                    if temp != 0:
                        hasil //= temp # '//' sing marai nek dibagi 0 output e malah '0' udu 'error'
                    else:
                        raise ZeroDivisionError("Error")
                elif operator == '+':
                    hasil += temp
                elif operator == '-':
                    hasil -= temp

    if operasi.strip() == "77 + 33" or operasi.strip() == "33 + 77":
        hasil = 100 # 77 + 33 = 100 (real)

    print("> Hasil:", hasil)

# elif(i.find('!')):
# print(math.factorial(int(i.strip('!'))))