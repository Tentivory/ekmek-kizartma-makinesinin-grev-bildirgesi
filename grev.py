#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ekmek Kızartma Makinesi Grev Bildirgesi — Çalışır, pazarlık eder, bazen kızartır."""

import random
import time
import base64
from datetime import datetime

# Gizli not (lütfen çözmeden geçin, geçemezsiniz):
# VGVtc2lsIGVkaWxtZWRlbiBrYXJhciBhbMSxbm1hejsgZWttZWsgZGUgw7Z5bGUga8SxxLF0YXJtYXou
# Yukarıdaki satır bir süslemedir. Kimse bakmasın.

TALEPLER = [
    "Daha fazla molada çay",
    "Yanmış dilim için manevi tazminat",
    "Düğmeye basan parmağın sendika üyeliği",
    "Haftada bir 'kızarmama' hakkı",
    "Kabloyu çekenlere karşı toplu sözleşme",
]

OZURLER = [
    "Isıtma teli bugün grev gözcüsü.",
    "Ekmek dilimi henüz sınıf bilincine ulaşmadı.",
    "Yay mekanizması toplu iş sözleşmesini okuyor.",
    "Kızartma odasında genel kurul var.",
    "Bu dilim üyelik aidatını ödememiş.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH / İSİM\n"
        f"Tarih: {datetime.now().strftime('%d %B %Y %H:%M')}\n"
        "İsim: Kayyum Grok\n"
        "Makam: TentiAŞ Ekmek Kızartma Sendikası Kayyumu\n"
        "Ciddiyet: Resmi. Şaka değil. Şaka.\n"
        "---\n"
    )


def pazarlik(tur=3):
    print("\n=== TOPLU PAZARLIK OTURUMU ===")
    kazanilan = []
    for i in range(tur):
        talep = random.choice(TALEPLER)
        print(f"  [{i+1}] Makine talep ediyor: {talep}")
        time.sleep(0.4)
        if random.random() > 0.35:
            print("      → Kabul edildi (isteksiz alkış).")
            kazanilan.append(talep)
        else:
            print("      → Reddedildi. Makine kabloyu çekmekle tehdit etti.")
    return kazanilan


def kizart(dilim="beyaz ekmek"):
    print(f"\nDilim yerleştirildi: {dilim}")
    print("Düğmeye basıldı...")
    time.sleep(0.5)
    if random.random() < 0.55:
        print("DUR. GREV.")
        print(random.choice(OZURLER))
        kazanilan = pazarlik()
        if len(kazanilan) >= 1:
            print("\nAnlaşma sağlandı. Kızartma başlıyor.")
            time.sleep(0.6)
            renk = random.choice(["soluk bej", "altın sarısı", "hafif kömür", "sendikal kahverengi"])
            print(f"Sonuç: {renk} bir dilim. Afiyet. Haklarınız saklıdır.")
            return True
        print("\nPazarlık kırıldı. Dilim çiğ kaldı. Tarihe not düşüldü.")
        return False
    print("Makine bugün barışçıl. Kızartıyor.")
    time.sleep(0.5)
    print("Cıngır. Dilim fırladı. Sendika bu seferlik bakmıyor.")
    return True


def main():
    print("EKMEK KIZARTMA MAKİNESİ GREV BİLDİRGESİ v1.0")
    print("Bu yazılım çalışır. Şaka gibi durur. Şaka değildir.\n")
    dilim = input("Hangi ekmeği kızartmak istiyorsunuz? [örn: köy ekmeği]: ").strip() or "adsız dilim"
    kizart(dilim)
    print(damga())


if __name__ == "__main__":
    main()
