import unittest

from powerset_generator import powerset


class TestPowerset(unittest.TestCase):
    three_list: list[int] = [1, 2, 3]

    three_repetition: list[int] = [1, 2, 3, 1, 2, 2, 3, 3, 3]

    empty_set: set[int] = set()

    power_three: list[set[int]] = [
        empty_set,
        {1},
        {2},
        {3},
        {1, 2},
        {1, 3},
        {2, 3},
        {1, 2, 3},
    ]

    def test_powerset(self):
        result: list[set[int]] = [s for s in powerset.powerset(self.three_list)]

        # AssertCountEqual requires elements to be hashable, which they
        # aren't in our case. So we do it the slow way
        self.assertEqual(len(result), 2 ** len(self.three_list))
        self.assertTrue(
            all(result.count(i) == self.power_three.count(i) for i in result)
        )

    def test_powerset_repeated(self):
        result: list[set[int]] = [s for s in powerset.powerset(self.three_repetition)]

        # AssertCountEqual requires elements to be hashable, which they
        # aren't in our case. So we do it the slow way
        self.assertEqual(len(result), 2 ** len(self.three_list))
        self.assertTrue(
            all(result.count(i) == self.power_three.count(i) for i in result)
        )


if __name__ == "__main__":
    unittest.main()
