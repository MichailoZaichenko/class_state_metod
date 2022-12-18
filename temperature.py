# Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт и для перевода из Фаренгейта в Цельсий. 

# Необязательное
# Также класс должен считать количество подсчетов температуры и возвращать это значение с помощью статического метода.

celsia = int(input("Введите температуру в цельсиях: "))
faringate = int(input("Введите температуру в фарингейтах: "))

class Temperature:
    def __init__(self, celsias, faringates):
        self.celsias = celsias
        self.faringates = faringates

    @staticmethod
    def Celsia(celsias):
        celsias = celsia * 1.8 + 32
        return celsias

    @staticmethod
    def Faringate(faringates):
        faringates = (faringate - 32) / 1.8
        return faringates
t = Temperature()
temeat1 = t.Celsia(faringate)
temeat2 = t.Faringate(celsia)
print(temeat1)
print(temeat2)