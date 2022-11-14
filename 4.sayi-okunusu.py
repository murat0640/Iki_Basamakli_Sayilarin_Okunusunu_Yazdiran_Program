print(""""

IKi Basamakli Sayilarin Okunusunu Bulma Programina Hosgeldiniz

""")

birler = ["","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz"]
onlar = ["","on","yirmi","otuz","kirk","elli","atmis","yetmis","seksen","doksan"]


def okunus(sayi):
    x= sayi % 10
    y= sayi//10

    return onlar[y] + " " + birler[x]

sayi = int(input("Okunmasini istediginiz sayiyi giriniz:"))

print(okunus(sayi))



