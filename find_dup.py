#!/usr/bin/python3
class find_dup():
    def __init__(self, array):
        self.length = len(array)
        self.list = array
    def swap(self, index):
        temp = self.list[index]
        self.list[index] = self.list[self.list[index]]
        self.list[self.list[index]] = temp
    def main(self):
        index = 0
        while index < self.length:
            if self.list[index] != index:
                if self.list[index] == self.list[self.list[index]]:
                    return False
                self.swap(index)
            index += 1
        return True


if __name__ == "__main__":
    array = [1, 0, 2, 3, 5, 4, 6]
    if array == None or len(array) < 1:
        raise ValueError('wrong sample of array')

    instance = find_dup(array)

    print (instance.main())
