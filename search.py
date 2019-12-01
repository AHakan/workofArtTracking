#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time

dosya = open("eserliste.txt")
oku = dosya.readlines()

class ara():

    def __init__(self, parametre, deger):
        self.parametre=parametre
        self.deger=deger
        self.uzunluk=len(parametre)
        self.dosyaread=""
        if deger=="1":
            self.isimara()
        if deger=="2":
            self.turara()
        if deger=="3":
            self.sahipara()
        if deger=="4":
            self.idara()

    def isimara(self):
        self.l=0
        print("Aranıyor...")
        for i in range(0, len(oku)):
            for k in range(0, self.uzunluk):
                self.dosyaread=self.dosyaread + oku[i][k]
            if self.dosyaread == self.parametre:
                time.sleep(1)
                print(oku[i])
                self.l=self.l+1
            self.dosyaread = ""

        if self.l!=0:
            print(str(self.l) + " Değer bulundu.\n")
        if self.l==0:
            print("Aradığınız isim de kayıt yoktur. \n")

    #def turara(self):






