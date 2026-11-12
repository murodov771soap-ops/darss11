tadbir_1 = {"Ali", "Vali", "Sami"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}


barchasida = tadbir_1 & tadbir_2 & tadbir_3


barcha_qatnashchilar = tadbir_1 | tadbir_2 | tadbir_3
faqat_bittada = set()
for ism in barcha_qatnashchilar:
  qatnashdi_soni = (
      (ism in tadbir_1) + (ism in tadbir_2) + (ism in tadbir_3)
  )
  if qatnashdi_soni == 1:
    'faqat_bittada.add'(ism)


kamida_ikkitada = set()
for ism in barcha_qatnashchilar:
  qatnashdi_soni = (
      (ism in tadbir_1) + (ism in tadbir_2) + (ism in tadbir_3)
  )
  if qatnashdi_soni >= 2:
    kamida_ikkitada.add(ism)

print(f"Barcha tadbirlarda: {', '.join(barchasida)}")
print(f"Faqat bitta tadbirda: {', '.join(faqat_bittada)}")
print(f"Kamida ikkita tadbirda: {', '.join(kamida_ikkitada)}")