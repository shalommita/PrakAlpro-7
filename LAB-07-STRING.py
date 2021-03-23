# SHALOMMITA PRANATANTRI
# 71200640
# INFORMATIKA UKDW
# STRING - LAB/07

# REFERENSI DARI INTERNET TENTANG MENENTUKAN KATA
# TERMASUK ANAGRAM / BUKAN dan Mencari Karakter

# INPUT
# 2 KATA INPUTAN 1 inputan karakter
def nama():
    satu=input("Kata Pertama: ")
    dua=input("Kata Kedua: ")
    caKar=input("Karakter yang dicari: ")

    if sorted(satu.lower())==sorted(dua.lower()):
        print("Anagram!")
    else:
        print("Bukan Anagram !!!")
    
    tmp=False
    for i in range(len(satu)):
        if satu[i]==caKar:
            tmp=True
            break
    if tmp == True:
        print("Ketemu")
    else:
        print("Tidak Ada, Guys !!!")            
nama()

# PROSES



# OUTPUT

