import math

while True:
    print("KALKULATOR")
    print("Kakulator sederhana yang dapat melakukan operasi penjumlahan, pengurangan, dan faktorial")
    print("---------------------")
    
    operasi = input("Silahkan masukan operasi matematika yang ingin dilakukan: ")
    noBitches = True
    hasil = 0
    me = 0
    for i in operasi.split():
        if(i == "+"):
            pass
        elif(i == "-"):
            pass
        elif(i.find('!')):
            print(math.factorial(int(i.strip('!'))))
        else:
            hasil += int(i)