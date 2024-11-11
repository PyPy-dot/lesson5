from functools import total_ordering


@total_ordering
class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name: str, number_of_floors: int) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self) -> int:
        return self.number_of_floors

    def go_to(self, new_floor: int) -> None:
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __add__(self, other: int) -> object:
        if isinstance(other, int):
            return House(self.name, self.number_of_floors + other)
        return NotImplemented

    def __radd__(self, other: int) -> object:
        if isinstance(other, int):
            return self.__add__(other)
        return NotImplemented

    def __iadd__(self, other: int) -> object:
        if isinstance(other, int):
            self.number_of_floors += other
            return self
        return NotImplemented

    def __sub__(self, other: int) -> object:
        if isinstance(other, int):
            return House(self.name, self.number_of_floors - other)
        return NotImplemented

    def __rsub__(self, other: int) -> object:
        if isinstance(other, int):
            return self.__sub__(other)
        return NotImplemented

    def __isub__(self, other: int) -> object:
        if isinstance(other, int):
            self.number_of_floors -= other
            return self
        return NotImplemented

    def __del__(self) -> None:
        print(f"{self.name} снесён, но он останется в истории")
        del self.name


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

# Удаление объектов

del h2

del h3

print(House.houses_history)
