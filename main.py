#Завдання: Реалізуйте клас FileManager, який використовує дескриптори для управління правами доступу до файлів.
# Права доступу мають бути рядком з одним із значень: "read", "write" або "execute".
print("Task 1".center(40, "="))
class FileManager:
    def __init__(self, permissions):
        if permissions in ("read", "write", "execute"):
            self.__permissions = permissions
        else:
            raise ValueError
    @property
    def permissions(self):
        return (self.__permissions)

    @permissions.setter
    def permissions(self, value):
        if value in ("read", "write", "execute"):
            self.__permissions = value
        else:
            print('Incorrect data. You must enter "read", "write" or "execute".')
            raise ValueError
            #self.permissions = input()

filemanage = FileManager("read")
print(filemanage.permissions)
filemanage.permissions="write"
print(filemanage.permissions)
#Завдання 2: Реалізуйте клас Car, який використовує властивості property() для керування
#швидкістю автомобіля (від 0 до 240 км/год) та типом пального (бензин, дизель, електро).
print("Task 2".center(40, "="))
class Car:
    def __init__(self, speed, type_fuel):
        if 0 <= speed <=240:
            self.__speed = speed
        else:
            raise Exception("Speed must be between 0 and 240.")

        if type_fuel in ("petrol", "gasoline", "diesel", "electric"):
            self.__type_fuel = type_fuel

        else:
            raise Exception(f"{type_fuel} is incorrect value for type of fuel.")

    @property
    def type_fuel(self):
        return self.__type_fuel

    @type_fuel.setter
    def type_fuel(self, value):
        if value in ("petrol", "gasoline", "diesel", "electric"):
            self.__type_fuel = value
        else:
            raise Exception(f"{value} is incorrect value for type of fuel.")

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 240:
            self.__speed = value
        else:
            raise Exception("Speed must be between 0 and 240.")

car = Car(100, 'diesel')
print(car.speed)
#car.speed=300

#Завдання 3: Реалізуйте клас UserProfile, який використовує дескриптори для перевірки валідності електронної пошти
#та телефонного номера. Електронна пошта повинна містити "@" і ".", телефонний номер повинен містити 10 цифр
print("Task 3".center(40, "="))
class UserProfile:
    def __init__(self, email, phone):
        if email.find("@") != -1 and email.find("."):
            self.__email = email
        else:
            raise Exception(f"{email} is not valid email.")
        if phone.isdigit() and len(phone) == 10:
            self.__phone = phone
        else:
            raise Exception(f"{phone} is not valid phone number.")

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if value.find("@") != -1 and value.find("."):
            self.__email = value
        else:
            raise Exception(f"{value} is not valid email.")

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if value.isdigit() and len(value) == 10:
            self.__phone = value
        else:
            raise Exception(f"{value} is not valid phone number.")

user = UserProfile("kfjgkfdjg@jvcjvb.", "3809912345")
print(user.phone)
print(user.email)