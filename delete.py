#!/usr/bin/env python3
# -*-coding:utf-8-*-

dosya = open("eserliste.txt", "r+")


class deleteArt():
    erisimliste = []
    silveri = []

    def __init__(self, isim, tur, sahip, id):
        self.id = id
        self.isim = isim
        self.tur = tur
        self.sahip = sahip
        self.veri = self.isim + " " + self.tur + " " + self.sahip + " " + self.id + "\n"
        self.veri2 = "***" + self.veri
        self.indx=0
        self.sil()

    def sil(self):
        self.erisimliste.append(self.isim+" ")
        self.erisimliste.append(self.tur+" ")
        self.erisimliste.append(self.sahip+" ")
        self.erisimliste.append(self.id+"\n")
        self.verisil()

    def verisil(self):
        self.silveri=self.silveri+ dosya.readlines()
        self.indx=self.silveri.index(self.veri)
        self.silveri.remove(self.veri)
        self.silveri.insert(self.indx, self.veri2)
        print(self.silveri)
        self.silveri.remove(self.veri2)
        a=" "
        a=a*100
        self.silveri.append(a)

        #dosya.seek(0)
        #dosya.writelines(self.silveri)
        #print(self.silveri)
        #print(dosya.readlines())
        #print(self.erisimliste)