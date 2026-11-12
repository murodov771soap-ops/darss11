import csv


talabalar_data = [
    ["ism", "yosh", "yonalish", "ball"],
    ["Aziza", "19", "Python", "88"],
    ["Jasur", "20", "Web", "76"],
    ["Madina", "18", "Python", "95"],
    ["Sardor", "21", "Web", "82"],
    ["Malika", "19", "Python", "79"],
]

with open("talabalar.csv", "w", encoding="utf-8", newline="") as f:
  writer = csv.writer(f)
  writer.writerows(talabalar_data)
  
tanlangan_yonalish = "Python"
filtrlangan_talabalar = []

with open("talabalar.csv", "r", encoding="utf-8") as f:
  reader = csv.DictReader(f)
  for row in reader:
    if row["yonalish"] == tanlangan_yonalish:
      row["ball"] = int(row["ball"])
      filtrlangan_talabalar.append(row)


filtrlangan_talabalar.sort(key=lambda x: x["ball"], reverse=True)


yangi_fayl = "filtrlangan_talabalar.csv"
with open(yangi_fayl, "w", encoding="utf-8", newline="") as f:
  fieldnames = ["ism", "yosh", "yonalish", "ball"]
  writer = csv.DictWriter(f, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(filtrlangan_talabalar)

print(f"{len(filtrlangan_talabalar)} ta talaba topildi.")
print(f"Natijalar {yangi_fayl} fayliga saqlandi.")