fayllar = [
    "Hisobot 2026.pdf",
    "profil_rasmi.jpg",
    "video.mp4",
    "jadval.xlsx",
    "diagramma.png",
]

yaroqli_formatlar = (".pdf", ".jpg", ".png")
yaroqli = []
yaroqsiz = []

for fayl in fayllar:
  if fayl.lower().endswith(yaroqli_formatlar):
    
    yangi_nom = fayl.replace(" ", "_")
    yaroqli.append(yangi_nom)
  else:
    yaroqsiz.append(fayl)

print("Yaroqli:")
for y in yaroqli:
  print(y)

print("\nYaroqsiz:")
for y in yaroqsiz:
  print(y)