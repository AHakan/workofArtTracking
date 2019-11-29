#!/usr/bin/env python3
#-*-coding:utf-8-*-

import sys
import work

dosya=open("eserliste.txt")

a=dosya.readlines()

print(a)

while True:
    print("""
        1- Ekleme
        2- Silme
        3- Güncelleme
        """)
    secim = input("Lütfen yapmak istediğin işlemi seç: ")
    if secim=="1":
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
            
        kontrol=a.count(isim+" "+tur+" "+sahip+" "+id+"\n")
        if kontrol!=0:
            print("*---Bu kayıt liste de var---*")
            continue
        else:
            eser=work.workofArt(isim, tur, sahip, id)
    
    print(eser.erisimliste)


