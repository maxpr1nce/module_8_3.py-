
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__validate_vin(vin)
        self.__numbers = self.__validate_numbers(numbers)

    def __validate_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return vin_number

    def __validate_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return numbers


# Пример использования
try:
    car = Car("Toyota", 1234567, "ABC123")
    print("Автомобиль создан успешно!")
except (IncorrectVinNumber, IncorrectCarNumbers) as e:
    print(e.message)