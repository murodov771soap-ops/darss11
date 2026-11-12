import math

shaharlar = {"A": (0, 0), "B": (3, 4), "C": (6, 0)}

def masofa(p1, p2):
  return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

shahar_nomlari = list(shaharlar.keys())
eng_uzun_masofa = 0
eng_uzun_juftlik = ("", "")

for i in range(len(shahar_nomlari)):
  for j in range(i + 1, len(shahar_nomlari)):
    sh1 = shahar_nomlari[i]
    sh2 = shahar_nomlari[j]
    d = masofa(shaharlar[sh1], shaharlar[sh2])
    print(f"{sh1} va {sh2}: {d}")
    if d > eng_uzun_masofa:
      eng_uzun_masofa = d
      eng_uzun_juftlik = (sh1, sh2)

print(
    f"Eng uzoq yo'nalish: {eng_uzun_juftlik[0]} — {eng_uzun_juftlik[1]} ({eng_uzun_masofa})"
)