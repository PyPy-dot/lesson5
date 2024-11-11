from functools import total_ordering


@total_ordering
class House:
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


h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(h1)

print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__

print(h1)

print(h1 == h2)

h1 += 10  # __iadd__

print(h1)

h2 = 10 + h2  # __radd__

print(h2)

print(h1 > h2)  # __gt__

print(h1 >= h2)  # __ge__

print(h1 < h2)  # __lt__

print(h1 <= h2)  # __le__

print(h1 != h2)  # __ne__
