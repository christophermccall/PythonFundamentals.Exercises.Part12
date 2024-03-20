from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start:
    :param stop:
    :param parity:
    :return:
    """
    # because parity.EVEN is set to an odd number and parity.ODD is set to an even number...
    # ...this list takes in x IF it's even or odd based on the OPPOSITE category(odd,even) of the parity value
    list_gen = [x for x in range(start, stop) if x % 2 != parity.value]
    return list_gen

    # another example

    # if parity == parity.ODD: -if parity value is even...
    #     list_gen = [x for x in range(start, stop) if x % 2 == 0]# ...this list takes even numbers...
    #     ...from the specified start because enum ODD is set to an even number.
    # else:...
    #     list_gen = [x for x in range(start, stop) if x % 2 != 0]# ...this list takes in odd numbers...
    #     ....from the specified start because enum EVEN is set to an odd number
    # return list gen


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    # this function takes in a key and uses a predetermined "strategy()"...
    # ...such as squaring a number or finding the factorial...
    # ...and manipulates the key via strategy(key) in order to determine and return the {key: value}
    # key == {key:      }
    #        {   : value}  == strategy(key)

    dict_gen = {key: strategy(key) for key in range(start, stop)}
    return dict_gen

def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    # this set takes only the lower case characters from a string(character list) and turns them into upper case...
    # ...while inherently eliminating doubles
    set_gen = {val.upper() for val in val_in if val.islower()}

    return set_gen
