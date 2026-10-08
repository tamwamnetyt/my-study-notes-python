# Личное сообщение
name = "Max"
print("Hello " + name + ", would you like to learn some Python today?\n")


# Регистр символов в именах
name = "max khatimov\n"

print(name.lower())
print(name.upper())
print(name.title())


# Знаменитая цитата
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."\n')


# Знаменитая цитата 2
famous_person = "Albert Einstein"
message = famous_person + ' once said, "A person who never made a mistake never tried anything new."\n'

print(message)


# Удаление пропусков
name = "\t\n  Eric  \n"

print("Имя с пропусками:\n")
print(name)

print("lstrip():\n")
print(name.lstrip())

print("rstrip():\n")
print(name.rstrip())

print("strip():\n")
print(name.strip())
