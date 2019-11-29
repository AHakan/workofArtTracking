#!/usr/bin/env python3
#-*-coding:utf-8-*-

dosya=open("eserliste.txt","a+")

class addArt():
    erisimliste=[]
    
    def __init__(self, isim, tur, sahip, id):
        self.id=id
        self.isim=isim
        self.tur=tur
        self.sahip=sahip
        self.ekle()
    
    def ekle(self):
        self.erisimliste.append(self.isim+" ")
        self.erisimliste.append(self.tur+" ")
        self.erisimliste.append(self.sahip+" ")
        self.erisimliste.append(self.id+"\n")
        self.dosyayaz()
        
    def dosyayaz(self):
        dosya.writelines(self.erisimliste)



