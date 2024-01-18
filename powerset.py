from itertools import combinations
from collections.abc import Collection
from typing import TypeVar

from typing import Generator

T = TypeVar("T")


def powerset(collection: Collection[T]) -> Generator[set[T], None, None]:
    """Generates the members of the powerset of s.

    Power sets
    ------------
    
    The power set of a collections is the set of all subsets of the collection.

    * The power set includes the empty set.

    * The power set includes a set of all members of the collections.
    That is, it is not limited to the proper subsets of the collection.

    * If the collection has N elements, the power set will have 2^N elements.

    Usage notes
    -------------

    This function generators sets irrespective of the type of its input.

    In the current version, there is no enforcement of the type hinting that
    members of the input collection all be of the same type. But do not rely on
    this lax behavior.



    Example::

        a_list: list[str] = ["one", "two", "three"]
        for element in powerset(s):
            print(element)

        produces

            set()
            {'one'}
            {'three'}
            {'two'}
            {'one', 'three'}
            {'one', 'two'}
            {'three', 'two'}
            {'one', 'three', 'two'}
    """

    # explicitly start at 0 to not forget that the empty set
    # is in the powerset
    for r in range(0, len(collection) + 1):
        for result in combinations(collection, r):
            # itertools.combinations spits out tuples irrespective of type of s
            yield set(result)
