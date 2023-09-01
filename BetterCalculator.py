import math

while True:
    print("KALKULATOR")
    print("Kakulator sederhana yang dapat melakukan operasi penjumlahan, pengurangan, dan faktorial")
    print("---------------------")
    
    operasi = input("Silahkan masukan operasi matematika yang ingin dilakukan: ")
    tambah = True
    hasil = None
    for i in operasi.split():
        if(i == "+"):
            tambah = True
        elif(i == "-"):
            tambah = False
        # elif(i.find('!')):
        #     print(math.factorial(int(i.strip('!'))))
        else:
            if(hasil == None):
                hasil = int(i)
            elif(tambah):
                hasil += int(i)
            else:
                hasil -= int(i)
    print(hasil)