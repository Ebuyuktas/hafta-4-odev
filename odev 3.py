#hafta 4 odev 3
#inputtaki sayıları degıskene atayıp toplamını alma

print("""rakam içeren bir parola olusturun""")
rakam=["1","2","3","4","5","6","7","8","9","0"]
toplam=0

while True:
    try:
        parola=input("parolanızı giriniz(cıkmak icin q):  ")
        if parola=="q":
            break
        if not parola:
            print("bos gecmeyelim")
            continue
        for i in parola:
            if i in rakam:
                toplam+=int(i)
        else:
            print("parolanızda rakam bulunmamaktadır.")
        print("parolanız:",parola,"\nparolanızdaki rakamların toplamı:",toplam,"\n",end="")
                
    except:
        print("bir hata oluştu")
