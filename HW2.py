def data(name, surname, year_birthday, city, email, phone_number):
   return f"{name} {surname} {year_birthday} {city} {email} {phone_number}"



yname = input("Введите ваше имя: ")
ysurname = input("Введите вашу фамилию: ")
birthday = input("Введите год вашего рождения: ")
ycity = input("Введите город, в котором вы проживаете: ")
yemail = input("Введите ваш email: ")
yphone = input("Введите ваш номер телефона: ")
print(data(yname, ysurname, birthday, ycity, yemail, yphone))

