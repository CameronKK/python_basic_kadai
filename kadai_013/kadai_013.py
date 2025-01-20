def calculate_total(price: float, tax: float)->int:
  total = price + price * tax / 100
  return int(total)

result = calculate_total(110, 10)
print(f"{result}円")