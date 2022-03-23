from utils import *

class Polyomino:
    def __init__(self, shape):
        self.height = shape[0]
        self.width = shape[1]
        self.positions = []


class RPolyomino(Polyomino):
    def set_positions(self, table, square=False):
        if square:
            rotations = [table]
        else:
            rotations = [table, rotate(table)]
        for rot in rotations:
            for i in range(len(rot) - self.height + 1):
                for j in range(len(rot[i]) - self.width + 1):
                    self.positions.append([row[j: self.width + j] for row in rot[i: self.height + i]])


class LPolyomino(Polyomino):
    def set_positions(self, table):
        if self.width == self.height:
            rotations = [
                table,
                rotate(table),
                rotate(rotate(table)),
                rotate(rotate(rotate(table)))
            ]
        else:
            rotations = [
                table,
                rotate(table),
                rotate(rotate(table)),
                rotate(rotate(rotate(table))),
                reflect(table),
                rotate(reflect(table)),
                rotate(rotate(reflect(table))),
                rotate(rotate(rotate(reflect(table))))
            ]
        for rot in rotations:
            for i in range(len(rot) - self.height + 1):
                for j in range(len(rot[i]) - self.width + 1):
                    tmp = []
                    for row in rot[i: self.height + i - 1]:
                        tmp.append([row[j]])
                    tmp.append(rot[self.height + i - 1][j: self.width + j])
                    self.positions.append(tmp)