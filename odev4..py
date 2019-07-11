#hafta odev 4
#seslileri ayırıp baska dosyaya yazıyoruz

try:
    futbolcular= open("C:/Users/Emine/Desktop/futbolcular.txt","r")
    a=futbolcular.readlines()
    alexdesouza=open("sesli.txt","w")
    sesli="aeıioöuüAEIİOÖUÜ"

    for i in a:
        if i[0] in sesli:
            alexdesouza.write(i)
    print("sesli harfle baslayan futbolcular ilgili dosyaya transfer edildi")
    futbolcular.close()
    alexdesouza.close()
except:
    print("hata olustu")

    
        
