menu = {"lavash": 28000, "somsa": 15000, "choy": 5000}


def buyurtma(*args, **kwargs):
  
  for kalit, qiymat in kwargs.items():
    print(
        f"{kalit.capitalize()}: {qiymat}"
    )  

  jami = 0
  for mahsulot in args:
    if mahsulot in menu:
      jami += menu[mahsulot]
    else:
      print(f"Ogohlantirish: '{mahsulot}' menyuda mavjud emas!")

  print(f"Jami: {jami} so'm")


buyurtma("lavash", "choy", "somsa", mijoz="Dilshod", telefon=901234567)