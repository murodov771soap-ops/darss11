ombor_1 = {"olma": 20, "anor": 12, "nok": 13}
ombor_2 = {"olma": 15, "banan": 10}

natija_ombor = ombor_1.copy()

for mahsulot, miqdor in ombor_2.items():
  if mahsulot in natija_ombor:
    natija_ombor[mahsulot] += miqdor
  else:
    natija_ombor[mahsulot] = miqdor

print(natija_ombor)