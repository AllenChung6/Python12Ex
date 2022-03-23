import math
from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    # normal method
    #     list1 = []
    #     for x in range(start, stop):
    #         if x % 2 == 0 and parity == parity.EVEN:
    #             list1.append(x)
    #         elif x % 2 == 1 and parity == parity.ODD:
    #             list1.append(x)
    #     return list1

    # List comprehension
    gen = [x for x in range(start, stop) if
           (x % 2 == 0 and parity == parity.EVEN) or (x % 2 == 1 and parity == parity.ODD)]
    return gen

    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start:
    :param stop:
    :param parity:
    :return:
    """


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    # dictionary comprehension list
    gen = {x: strategy(x) for x in range(start, stop)}
    return gen

    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    pass


def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    pass
