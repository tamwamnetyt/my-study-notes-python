# 3-4. Список гостей
guests = ['Cristiano Ronaldo', 'Dmitry Ilin', 'Zine Zidane']

print("Приглашаю тебя на обед, " + guests[0] + "!")
print("Приглашаю тебя на обед, " + guests[1] + "!")
print("Приглашаю тебя на обед, " + guests[2] + "!\n")


# 3-5. Изменение списка гостей
print(guests[2] + " не сможет прийти на обед.\n")

guests[2] = 'Fede Valverde'

print("Приглашаю тебя на обед, " + guests[0] + "!")
print("Приглашаю тебя на обед, " + guests[1] + "!")
print("Приглашаю тебя на обед, " + guests[2] + "!")


# 3-6. Больше гостей
print("\nМогу пригласить ещё гостей!\n")

guests.insert(0, 'Yaya Toure')
guests.insert(2, 'Toni Kroos')
guests.append('Max Khatimov')

print("Приглашаю тебя на обед, " + guests[0] + "!")
print("Приглашаю тебя на обед, " + guests[1] + "!")
print("Приглашаю тебя на обед, " + guests[2] + "!")
print("Приглашаю тебя на обед, " + guests[3] + "!")
print("Приглашаю тебя на обед, " + guests[4] + "!")
print("Приглашаю тебя на обед, " + guests[5] + "!")


# 3-7. Сокращение списка гостей
print("\nК сожалению, не смогу пригласить больше  гостей.")
print("Теперь я могу пригласить только двух гостей.\n")

removed_guest = guests.pop()
print(removed_guest + ", к сожалению, я вынужден отменить приглашение.")

removed_guest = guests.pop()
print(removed_guest + ", к сожалению, я вынужден отменить приглашение.")

removed_guest = guests.pop()
print(removed_guest + ", к сожалению, я вынужден отменить приглашение.")

removed_guest = guests.pop()
print(removed_guest + ", к сожалению, я вынужден отменить приглашение.")

print("\nПриглашения остаются в силе:")

print(guests[0] + ", ты всё ещё приглашён на обед!")
print(guests[1] + ", ты всё ещё приглашён на обед!")

del guests[0]
del guests[0]

print("\nИтоговый список гостей:")
print(guests)
