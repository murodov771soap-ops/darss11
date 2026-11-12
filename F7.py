natijalar = [
    {"ism": "Aziza", "ball": 82},
    {"ism": "Jasur", "ball": 64},
    {"ism": "Madina", "ball": 91},
    {"ism": "Sardor", "ball": 70},
]

yuqori_70 = list(filter(lambda x: x["ball"] > 70, natijalar))
yuqori_ism = [x["ism"] for x in yuqori_70]


oshirilgan_ballar = list(map(lambda x: round(x["ball"] * 1.1, 1), yuqori_70))

saralangan_oborot = sorted(yuqori_70, key=lambda x: x["ball"], reverse=True)
saralangan_ismlar = [x["ism"] for x in saralangan_oborot]

print(f"70 dan yuqori: {', '.join(yuqori_ism)}")
print(f"10% oshirilgan ballar: {oshirilgan_ballar}")
print(f"Saralangan: {', '.join(saralangan_ismlar)}")