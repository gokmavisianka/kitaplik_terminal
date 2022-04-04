class Kitaplık:
    def __init__(self):
        self.kitaplar = []
        self.ana_menü()

    def ekle(self):
        isim = input("Eklenecek kitap adını giriniz: ")
        if isim not in self.kitaplar:
            self.kitaplar.append(isim)
            print("Kitap başarıyla eklendi!")
        else:
            print("Bu kitap zaten mevcut!")

    def sil(self):
        isim = input("Silinecek kitap adını giriniz: ")
        if isim in self.kitaplar:
            self.kitaplar.remove(isim)
            print("Kitap başarıyla silindi!")
        else:
            print("Böyle bir kitap yok!")

    def listele(self):
        uzunluk = len(self.kitaplar)
        if uzunluk > 0:
            for indeks in range(uzunluk):
                kitap = self.kitaplar[indeks]
                print(f"{indeks + 1}-{kitap}")
        else:
            print("Kitaplığınız boş!")

    def seç(self):
        print("-----------------------")
        seçenekler = ("1-Kitap ekleme", "2-Kitap silme", "3-Kitap listeleme", "4-Çıkış")
        metin = "\n".join(seçenekler) + "\nSeçiminiz: "
        while True:
            try:
                seçim = input(metin)
                seçim = int(seçim)
                assert (seçim in [1, 2, 3, 4]) == True
                return seçim
            except (ValueError, AssertionError):
                print(f"'{seçim}' değerini girdiniz fakat bu değer 1, 2, 3 ya da 4 olmalıdır.")
                continue
            finally:
                print("-----------------------")
                
    def ana_menü(self):
        while True:
            try:
                seçim = self.seç()  
                if seçim == 1:
                    fonksiyon = self.ekle
                elif seçim == 2:
                    fonksiyon = self.sil
                elif seçim == 3:
                    fonksiyon = self.listele
                elif seçim == 4:
                    quit()
                while True:
                    fonksiyon()
                    while True:
                        karar = input("Bitirelim mi(E/H): ")
                        if karar == "H":
                            break
                        elif karar == "E":
                            raise Exception
                        else:
                            print(f"'{karar}' değerini girdiniz fakat bu değer 'E' ya da 'H' olmalıdır.")
                    print("-----------------------")
            except Exception:
                continue

kitaplık = Kitaplık()
        
            
