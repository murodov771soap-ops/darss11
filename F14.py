import matplotlib.pyplot as plt

oylar = ["Yan", "Fev", "Mar", "Apr", "May", "Iyun"]
daromad = [12, 15, 11, 19, 22, 18]

plt.figure(figsize=(8, 4))
plt.plot(oylar, daromad, marker="o", color="b", linestyle="-")
plt.title("Oylik daromad dinamikasi")
plt.xlabel("Oylar")
plt.ylabel("Daromad (mln so'm)")
plt.grid(True)
plt.show()

kategoriyalar = ["Texnika", "Kiyim", "Oziq-ovqat"]
savdo = [35, 20, 45]  # dona

plt.figure(figsize=(8, 4))
plt.bar(kategoriyalar, savdo, color="orange")
plt.title("Kategoriyalar savdosi")
plt.xlabel("Kategoriyalar")
plt.ylabel("Sotilgan miqdor (dona)")
plt.show()


buyurtma qiymatlari = [
    50,
    75,
    80,
    60,
    90,
    110,
    120,
    70,
    85,
    95,
    130,
    100,
]  

plt.figure(figsize=(8, 4))
plt.hist(buyurtma_qiymatlari, bins=5, color="green", edgecolor="black")
plt.title("Buyurtma qiymatlari taqsimoti")
plt.xlabel("Qiymat diapazoni")
plt.ylabel("Chastotasi (Soni)")
plt.show()