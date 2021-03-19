from typing import Tuple, List

class MyClass:
    def __init__(self):
        self.__lst = [3, 5.0]

    def get_lst_as_tup(self) -> Tuple[int, float]:
        return tuple(self.__lst)

if __name__ == '__main__':
    m = MyClass()
    print(m.get_lst_as_tup())
