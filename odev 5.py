#hafta 4 odev 5
#turkce karakterler sorununu cozup yen� dosyaya yazd�r�yoruz

try:
    futbolcular = open("C:/Users/Emine/Desktop/futbolcular.txt","r")
    eski = futbolcular.read()
    yeni = open("sonhali.txt","w")
    
    kaynak = "������������"
    hedef = "scoguiSCOGUI"
    �eviri_tablosu = str.maketrans(kaynak, hedef)
    print(eski.translate(�eviri_tablosu))
    yeni.write(eski.translate(�eviri_tablosu))

    yeni.close()
    futbolcular.close()

except:
    print("bir hata olu�tu!")
    
