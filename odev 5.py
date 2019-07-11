#hafta 4 odev 5
#turkce karakterler sorununu cozup yený dosyaya yazdýrýyoruz

try:
    futbolcular = open("C:/Users/Emine/Desktop/futbolcular.txt","r")
    eski = futbolcular.read()
    yeni = open("sonhali.txt","w")
    
    kaynak = "þçöðüýÞÇÖÐÜÝ"
    hedef = "scoguiSCOGUI"
    çeviri_tablosu = str.maketrans(kaynak, hedef)
    print(eski.translate(çeviri_tablosu))
    yeni.write(eski.translate(çeviri_tablosu))

    yeni.close()
    futbolcular.close()

except:
    print("bir hata oluþtu!")
    
