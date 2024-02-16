distance_cm = float (input("Введите расстояние в сантиметрах: "))

distance_duim = distance_cm / 2.54
distance_fut = distance_duim / 12
distance_yard = distance_fut / 3
distance_mile = distance_yard / 1760

print("Расстояние в дюймах: ", distance_duim)
print("Расстояние в футах: ", distance_fut)
print("Расстояние в ярдах: ", distance_yard)
print("Расстояние в милях:", distance_mile)

