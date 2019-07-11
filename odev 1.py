#4. hafta odev 1
#input buyuk harfe donusturme programı

while True: 
    try:
        a=input("En çok hangi meyveyi seversiniz?(cevaplamak istemezsen q'ya bas):")
        if not a:
            print("meyve sevmeyen insan mı olur??kapat kapat!!")
            break
        if a=="q":
            break
        b=a.upper()
        print(b, "dedın benım de canım cektı bak sımdı!")
    except:
        print("bir hata olustu")
