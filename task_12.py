class Dessert:
    def __init__(self, name: str = " ", calories: int = 0) -> None:
        self.__name = name
        self.__calories = calories

    @property
    def get_name(self) -> str:
        return self.__name

    @get_name.setter
    def get_name(self, value: str) -> None:
        self.__name = value

    @property
    def get_calories(self) -> int:
        return self.__calories

    @get_calories.setter
    def get_calories(self, value: int) -> None:
        self.__calories = value

    def is_healthy(self) -> bool:
        return self.__calories < 200

    @staticmethod
    def is_delicious() -> bool:
        return True


class JellyBean(Dessert):
    def __init__(self, name: str = " ", calories: int = 0, flavor: str = '') -> None:
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def get_flavor(self) -> str:
        return self.__flavor

    @get_flavor.setter
    def get_flavor(self, value: str) -> None:
        self.__flavor = value

    def is_delicious(self) -> bool:
        if self.__flavor == "black licorice":
            return False
        return True


def tests():
    while True:
        dessert_name_input = input("Введите название десерта: ")
        try:
            calories_input = int(input("Введите колличество калорий: "))
            flavor_input = input("Введите flavor: ")
            if calories_input < 0:
                print("Значение калорий не может быть отрицательным")
                break
            test = JellyBean(dessert_name_input, calories_input, flavor_input)

            print(test.get_name)
            print(test.get_calories)
            print(test.get_flavor)

            print(test.is_healthy())
            print(test.is_delicious())
            print()
        except ValueError:
            print("Значение калорий должно быть целочисленным")
            break


tests()
