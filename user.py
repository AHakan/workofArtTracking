#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import search


while True:
    print("1- Eser İsmi\n"
          "2- Eser Türü\n"
          "3- Eser Sahibi\n"
          "4- Eser ID\n")
    parametre=input("Hangi parametre ile aramak istiyorsunuz: ")
    if parametre=="1":
        isim=input("Lütfen ismi giriniz: ")
        ara=search.ara(isim, "1")
    if parametre=="2":
        tur=input("Lütfen türü giriniz:")


    #if parametre=="3":

    #if parametre=="4":