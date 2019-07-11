#4. hafta odev 2
#girdi tasnifleme

print("""Lütfen kısaca kendinizden bahsediniz!
***lütfen dogum yeri, yas ve memleket bilgileri icersin***""")


rakamlar=["1","2","3","4","5","6","7","8","9","0"]
kucuk=0
buyuk=0
rakam=0
dıger=0

while True:
    try:
        bilgiler=input("bilgileri giriniz(cıkmak ıcın q):  ")
        if not bilgiler:
            print("daha dogmadınız sanırım??")
            break
        if bilgiler=="q":
            break
        for i in bilgiler:
            if i in rakamlar:
                rakam+=1
            elif i.islower()==True:
                kucuk+=1
            elif i.isupper()==True:
                buyuk+=1
            else:
                dıger+=1
        print("kucuk harf sayısı: {}\nbuyuk harf sayısı: {}\nrakam sayısı: {}\nozel karakter sayısı:{}\n".format(kucuk,buyuk,rakam,dıger),end="")
        break
    except:
        print("hata olustu")
        
