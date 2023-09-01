import math

while True:
    print("KALKULATOR")
    print("Kakulator sederhana yang dapat melakukan operasi penjumlahan, pengurangan, dan faktorial")
    print("---------------------")
    
    operasi = input("Silahkan masukan operasi matematika yang ingin dilakukan: ")
    noBitches = False
    hasil = 0
    me = None
    for i in operasi.split():
        if(i == "+"):
            pass
        elif(i == "-"):
            pass
        elif(i.find('!')):
            print(math.factorial(int(i.strip('!'))))
        else:
            hasil += int(i)