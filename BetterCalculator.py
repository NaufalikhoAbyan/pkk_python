import math

while True:
    border = "-" * 50

    print(border)
    print("KALKULATOR")
    print("Kalkulator sederhana yang dapat melakukan operasi penjumlahan, pengurangan, dan faktorial")
    print(border)
    
    operasi = input("Silahkan masukkan operasi matematika yang ingin dilakukan: ")
    tambah = True
    hasil = None
    faktorial = None

    for i in operasi.split():
        if i == "+":
            tambah = True
        elif i == "-":
            tambah = False
        else:
            if i.startswith('!'):
                faktorial = int(i[1:])
            elif i.endswith('!'):
                faktorial = int(i[:-1])
            else:
                faktorial = None

            if faktorial is not None:
                faktorial_hasil = math.factorial(faktorial)
                if hasil is None:
                    hasil = faktorial_hasil
                elif tambah:
                    hasil += faktorial_hasil
                else:
                    hasil -= faktorial_hasil
            else:
                if hasil is None:
                    hasil = int(i)
                elif tambah:
                    hasil += int(i)
                else:
                    hasil -= int(i)

    print("Hasil:", hasil)

# elif(i.find('!')):
# print(math.factorial(int(i.strip('!'))))