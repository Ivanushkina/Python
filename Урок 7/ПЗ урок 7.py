from abc import ABC, abstractmethod


# Задание 1

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        m1 = " ".join(str(self.matrix[0]))
        m2 = " ".join(str(self.matrix[1]))
        return f'{m1}\n{m2}'
        # res = ""
        # for row in self.matrix:
        #     res += f'{" ".join([str(l) for l in row])}\n'
        # return res

    def __add__(self, other):
        new_matrix = [[] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(new_matrix)


Matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
Matrix2 = Matrix([[1, 2, 3], [4, 5, 6]])
m3 = Matrix1 + Matrix1
print(f'сумма матриц:\n{m3}')


# Задание 2

class Clothes(ABC):
    @abstractmethod
    def material_cost(self):
        pass


class Coat(Clothes):
    def __init__(self, cl_name, V):
        self.cl_name = cl_name
        self.V = V
        self.type = "Пальто"

    def material_cost(self):
        self.cost = self.V / 6.5 + 0.5
        return round(self.cost, 2)


class Suit(Clothes):
    def __init__(self, cl_name, H):
        self.cl_name = cl_name
        self.H = H
        self.type = "Костюм"

    def material_cost(self):
        self.cost = 2 * self.H + 0.3
        return round(self.cost, 2)


Coat = Coat("Пальтишко кожаное", 60)
coat_cost = float(Coat.material_cost())
print(f'Стоимость ткани для костюма {coat_cost}')

Suit = Suit("Костюмчик, который сидит", 60)
Suit_cost = float(Suit.material_cost())
print(f'Стоимость ткани для пальто {Suit_cost}')

whole_cost = coat_cost + Suit_cost
print(f'Всего ткани нужно - {whole_cost}')


# Задание 3

class Cell:
    def __init__(self, cells_count):
        self.cells_count = int(cells_count)

    def __add__(self, other):
        return Cell(self.cells_count + other.cells_count)

    def __sub__(self, other):
        sub_cells = 0
        if self.cells_count > other.cells_count:
            sub_cells = Cell(self.cells_count - other.cells_count)
        else:
            print("Разность меньше нуля")
        return sub_cells

    def __mul__(self, other):
        return Cell(self.cells_count * other.cells_count)

    def __truediv__(self, other):
        div_cells = Cell(self.cells_count // other.cells_count)
        return div_cells

    def make_order(self, row_count):
        list = ['*' for _ in range(self.cells_count)]
        return '\n'.join([''.join(list[i:i+row_count]) for i in range(0, len(list), row_count)])

cell1 = Cell(4)
cell2 = Cell(5)
row_count = Cell.make_order(6)
sumc = cell1 + cell2
mulc = cell1 * cell2
subc = cell1 - cell2
divc = cell1 / cell2
print(sumc)
print(mulc)
print(subc)
print(divc)