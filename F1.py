matn = "Python dasturlash qiziqarli va keng imkoniyatlari bor dasturlash tili."


matn_lower = matn.lower()


for char in ".,!?;:":
  matn_lower = matn_lower.replace(char, "")

sozlar = matn_lower.split()


sozlar_soni = len(sozlar)


eng_uzun = max(sozlar, key=len) if sozlar else ""


faqat_harflar = matn_lower.replace(" ", "")
harf_sanash = {h: faqat_harflar.count(h) for h in set(faqat_harflar)}
eng_kop_harf = max(harf_sanash, key=harf_sanash.get) if harf_sanash else ""


takrorlanmaydigan = [s for s in sozlar if sozlar.count(s) == 1]

print(f"So'zlar soni: {sozlar_soni}")
print(f"Eng uzun so'z: {eng_uzun}")
print(f"Eng ko'p uchragan harf: {eng_kop_harf}")
print(f"Takrorlanmaydigan so'zlar: {', '.join(takrorlanmaydigan)}")