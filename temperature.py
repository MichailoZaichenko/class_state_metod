# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. 

# Необязательное
# Также класс должен считать количество подсчетов температуры и возвращать это значение с помощью статического метода.

celsia = int(input("Введите температуру в цельсиях: "))
faringate = int(input("Введите температуру в фарингейтах: "))

class Temperature:
    def __init__(self, celsias, faringates):
        self.celsias = celsias
        self.faringates = faringates
