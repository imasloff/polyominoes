# polyominoes
Мой вариант решения задачи о доказательстве существования замощения прямоугольника прямоугольными и L-полиомино.
Решение основано на Алгоритме Х Д. Кнута

Оценочная сложность алгоритма - О(N), где N - общее количество фигур полиомино

Затраты памяти:
1) list из N объектов дочерних классов класса Polyomino, атрибуты класса: 
    - двe переменные типа int - размерность фигуры
    - трехмерный список двухместных кортежей, содержащий все возможные позиции фигуры на столе
2) двумерный список двухместных кортежей - стол
3) двумерный numpy.array из N + m1 * m2 столбцов, N - общее количество фигур полиомино, m1 * m2 - площадь стола
4) рекурсивная функция, реализующая алгоритм, при N = 4 совершает 20 вызовов

При N = 4 программа исполняется за 3,3 сек

Для запуска программы:
    1. поменять значения входных параметров (table_shape, r_input, l_input) в файле main либо оставить по умолчанию
    2. запустить проект в любой удобной среде, поддерживающей python 3 (код написан в PyCharm)
    
ENG:
My solution for the polyomino tiling problem for rectangle and L-polyominoes.
Based on the D.Knut's Algorithm X.

Estimated complexity of the algorithm - O(N), where N - general amount of polyomino-figures

Memory cost: 
1) list of N objects of child classes of Polyomino class, class attributes: 
    - two variables of type int - dimension of the figure
    - a three-dimensional list of double tuples containing all possible positions of a piece on the table
2) 2D list of double tuples - table
3) 2D numpy.array of N + m1*m2 columns, N is the total number of polyomino pieces, m1*m2 is the area of the table
4) the recursive function that implements the algorithm makes 20 calls for N = 4

With N = 4, the program is executed in 3.3

