def bolish(a, b):
  
  assert b != 0, "B nolga teng bo'lishi mumkin emas!"
  return a / b


try:
  son1_str = input("Birinchi son: ")
  son2_str = input("Ikkinchi son: ")

  
  son1 = float(son1_str)
  son2 = float(son2_str)

  natija = bolish(son1, son2)
  print("Natija:", natija)

except ValueError:
  print("Xatolik: Faqat raqam kiritilishi kerak!")
except ZeroDivisionError:
  print("Xatolik: Nolga bo'lish mumkin emas.")
  print("Dastur ishlashda davom etmoqda.")
except AssertionError as e:
  print(f"Assertion xatolik: {e}")