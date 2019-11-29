#!usr/bin/env python3
#-*-coding:utf-8-*-

dosya=open("eserliste.txt", "r+")

class editArt():
    erisimliste = []
    degisveri = []

    def __init__(self, isim, tur, sahip, id):
        self.id = id
        self.isim = isim
        self.tur = tur
        self.sahip = sahip
        self.veri = self.isim + " " + self.tur + " " + self.sahip + " " + self.id + "\n"
        self.veri2=""
        self.indx = 0
        self.duzenle()

    def duzenle(self):
        self.erisimliste.append(self.isim+" ")
        self.erisimliste.append(self.tur+" ")
        self.erisimliste.append(self.sahip+" ")
        self.erisimliste.append(self.id+"\n")
        self.eserduzenle()

    def eserduzenle(self):
        self.degisveri = self.degisveri + dosya.readlines()
        self.indx = self.degisveri.index(self.veri)
        self.degisveri.remove(self.veri)
        print("Veri işaretleniyor...")
        print("Güncel veriyi giriniz.")
        self.yeniad=input("Adı: ")
        self.yenitur=input("Türü: ")
        self.yenisahip=input("Sahibi: ")
        self.yeniid=input("IDsi: ")
        self.veri2 = self.yeniad + " " + self.yenitur + " " + self.yenisahip + " " + self.yeniid + "\n"
        self.degisveri.insert(self.indx, self.veri2)
