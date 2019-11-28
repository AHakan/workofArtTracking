#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys
import work
import edit
import delete

dosya = open("eserliste.txt", "r+")
a = dosya.readlines()

while True:
    # print(a)
    isim = input("Lütfen eserin ismini giriniz: ")
    isimkontrol=""
    if len(isim) > 15:
        sys.exit()
            
    tur = input("Lütfen eserin türünü giriniz: ")
    if len(tur) > 15:
        sys.exit()
        
    sahip = input("Lütfen eserin sahibini giriniz: ")
    if len(sahip) > 15:
        sys.exit()
            
    id = input("Lütfen eserin id numarasını giriniz: ")
    if len(id) > 15:
        sys.exit()

    print("""
        1- Ekleme
        2- Güncelleme
        3- Silme
        """)
    secim = input("Lütfen yapmak istediğin işlemi seç: ")

    if secim=="1":
        kontrol=a.count(isim+" "+tur+" "+sahip+" "+id+"\n")
        if kontrol!=0:
            print("*---Bu kayıt liste de var---*")
            continue
        else:
            eser=work.workofArt(isim, tur, sahip, id)
        print(eser.erisimliste)
        cikis=input("İşlemlere devam etmek için D'ye, Çıkış için C ye basınız: ")
        if cikis=="C" or cikis=="c":
            print("Çıkış yapılıyor...")
            sys.exit()
        elif cikis=="D" or cikis=="d":
            continue
        #Ekstra girdiler kontrol edilmeli.

    if secim=="2":
        #eksik
        eski = a.index(isim + " " + tur + " " + sahip + " " + id + "\n")
        print(eski)
        duzenle=edit.edit(isim, tur, sahip, id)


    if secim=="3":
        kontrol = a.count(isim + " " + tur + " " + sahip + " " + id + "\n")
        if kontrol == 0:
            print("*---Bu kayıt liste de yok---*")
            continue
        else:
            silArt=delete.deleteArt(isim, tur, sahip, id)
            silverilist = silArt.silveri
            dosya.seek(0)
            dosya.writelines(silverilist)
