        else:
            for i in range(0, len(a)):
                for j in range(0, 15):
                    if a[i][j]==" ":
                        break
                    else:
                        kontrol=a[i][j]
                        isimkontrol=isimkontrol+kontrol
                            
                if isim==isimkontrol:
                    print("Bu isimden vardır.")
                    sys.exit()
                
