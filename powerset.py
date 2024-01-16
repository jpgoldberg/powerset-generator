from itertools import combinations
from collections.abc import Hashable

from typing import Generator


def powerset[T: Hashable](s: set[T]) -> Generator[set[T], None, None]:
    """Generates the members of the powerset of s.

    Output includes the empty set. Order of output is not defined.

    Example:
        s: set[str] = {"one", "two", "three"}
        for element in powerset({"one"}):
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
    for r in range(0, len(s) + 1):
        for result in combinations(s, r):
            # itertools.combinations spits out tuples irrespective of type of s
            yield set(result)
