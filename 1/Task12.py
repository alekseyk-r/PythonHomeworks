width = 10.2
height = 8.6
consumption = 5
can_volume = 3
buffer = 0.20

area = width * height
liters_needed = area * consumption * (1 + buffer)
cans = -(-liters_needed // can_volume)

print(f"Площадь окрашивания: {area:.2f} м2")
print(f"Количество литров краски с учетом запаса: {liters_needed:.2f} л")
print(f"Количество банок: {int(cans)}")
print(f"Неиспользуемых литров краски: {cans*can_volume - liters_needed:.2f} л")
