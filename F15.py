import csv
import matplotlib.pyplot as plt

kitoblar_data = [
    ["nom", "kategoriya", "muallif", "oqilgan"],
    ["Python asoslari", "Dasturlash", "Aliyev", "45"],
    ["Algoritmlar", "Dasturlash", "Karimov", "32"],
    ["Dunyo tarixi", "Tarix", "Ergashev", "28"],
    ["Koinot sirlari", "Ilm-fan", "Usmonov", "51"],
    ["Fizika asoslari", "Ilm-fan", "Aliyev", "19"],
]

with open("kitoblar.csv", "w", encoding="utf-8", newline="") as f:
  writer = csv.writer(f)
  writer.writerows(kitoblar_data)


def kitoblarni_korish():
  with open("kitoblar.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
      print(" | ".join(row))


def kitob_qidirish(nom_qism):
  with open("kitoblar.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    found = False
    for row in reader:
      if nom_qism.lower() in row["nom"].lower():
        print(f"Topildi: {row['nom']} ({row['muallif']}) - {row['oqilgan']} marta")
        found = True
    if not found:
      print("Bunday kitob topilmadi.")


def eng_kop_oqilgan():
  with open("kitoblar.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    max_kitob = None
    max_marta = -1
    for row in reader:
      marta = int(row["oqilgan"])
      if marta > max_marta:
        max_marta = marta
        max_kitob = row
    if max_kitob:
      print(
          f"Eng ko'p o'qilgan kitob: {max_kitob['nom']} — {max_kitob['oqilgan']}"
          " marta"
      )


def grafik_chiqarish():
  kategoriyalar_soni = {}
  with open("kitoblar.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
      kat = row["kategoriya"]
      kategoriyalar_soni[kat] = kategoriyalar_soni.get(kat, 0) + 1

  plt.bar(
      list(kategoriyalar_soni.keys()),
      list(kategoriyalar_soni.values()),
      color="purple",
  )
  plt.title("Kategoriyalar bo'yicha kitoblar soni")
  plt.xlabel("Kategoriya")
  plt.ylabel("Soni")
  plt.show()



print("1. Kitoblarni ko'rish")
print("2. Kitob qidirish")
print("3. Kategoriya bo'yicha filtrlash")
print("4. Eng ko'p o'qilgan kitob")
print("5. Grafik chiqarish")
tanlov = 4  

if tanlov == 4:
  eng_kop_oqilgan()