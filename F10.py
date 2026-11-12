
fayl_satrlari = ["Ali 36", "Vali 42", "Malika trente", "Sardor 38"]

jami_soat = 0
eng_kop_soat = -1
eng_kop_xodim = ""

for satr in fayl_satrlari:
  qismlar = satr.rsplit(" ", 1)
  xodim = qismlar[0]
  soat_str = qismlar[1]

  if soat_str.isdigit():
    soat = int(soat_str)
    jami_soat += soat
    if soat > eng_kop_soat:
      eng_kop_soat = soat
      eng_kop_xodim = xodim
  else:
    print(f"Ogohlantirish: {xodim} uchun soat qiymati noto'g'ri ({soat_str})")

print(f"Jami ish soati: {jami_soat}")
print(f"Eng ko'p ishlagan: {eng_kop_xodim} — {eng_kop_soat} soat")