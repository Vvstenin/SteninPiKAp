import unittest

from рк1 import classes


class TestClass(unittest.TestCase):
    def setUp(self):
        self.many_to_many = classes.getManyToMany()
        self.one_to_many = classes.getOneToMany()

        # Ожидаемый результат для первого задания
        self.first_expected = dict(filter(lambda item: len(item[1]) > 0,
                                          {key: list(filter(lambda item: str(item[0]).startswith("Д"), val)) for
                                           key, val
                                           in classes.getOneToMany().items()}.items()))

        # Ожидаемый результат для второго задания
        self.second_expected = sorted(
            {k: min([val[1] for val in classes.getOneToMany()[k]]) for k in classes.getOneToMany().keys()}.items(),
            key=lambda item: item[1])

        # Ожидаемый результат для третьего задания
        self.third_expected = sorted(classes.getManyToMany(), key=lambda item: item[1])

    # Тест для первого задания
    def test_first(self):
        self.assertEqual(classes.first(self.one_to_many), self.first_expected)

    # Тест для второго задания
    def test_second(self):
        self.assertEqual(classes.second(self.one_to_many), self.second_expected)

    # Тест для третьего задания
    def test_third(self):
        self.assertEqual(classes.third(self.many_to_many), self.third_expected)