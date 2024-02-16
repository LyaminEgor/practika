flight_number = input("номер рейса: ")
airline_name_ru = input("название авиакомпании (на русском языке): ")
airline_name_en = input("название авиакомпании (на английском языке): ")
destination_ru = input("город прилета (на русском языке): ")
destination_en = input("город прилета (на английском языке): ")

announcement_ru = "Заканчивается посадка на рейс "+ flight_number +" авиакомпании "+ airline_name_ru +" до "+ destination_ru +""

announcement_en = "This is the final boarding call for "+ airline_name_en +" flight "+ flight_number +" to "+ destination_en +""

print(announcement_ru)
print(announcement_en)
