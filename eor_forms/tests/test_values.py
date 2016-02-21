import unittest
from unittest.mock import MagicMock

from eor_forms import String, Integer, Decimal, empty

import decimal


class TestString(unittest.TestCase):

    def test_defaults(self):
        f = String('foo')

        self.assertIs(f.value, empty)
        self.assertIs(f.serialized_value, '')

    def test_default_value(self):
        f = String('foo', default='foobar')

        self.assertEqual(f.value, 'foobar')
        self.assertEqual(f.serialized_value, 'foobar')

    def test_set_empty_value(self):
        f = String('foo')
        f.value = empty

        self.assertEqual(f.serialized_value, '')

    def test_set_empty_serialized_value(self):
        f = String('foo')
        f.serialized_value = ''

        self.assertTrue(f.valid)
        self.assertEqual(f.serialized_value, '')
        self.assertEqual(f.value, empty)

    def test_set_serialized_value(self):
        f = String('foo')
        f.serialized_value = '  a b    '

        self.assertTrue(f.valid)
        self.assertEqual(f.serialized_value, '  a b    ')
        self.assertEqual(f.value, 'a b')


class TestInteger(unittest.TestCase):

    def test_defaults(self):
        f = Integer('foo')

        self.assertIs(f.value, empty)
        self.assertIs(f.serialized_value, '')

    def test_set_empty_value(self):
        f = Integer('foo')
        f.value = empty

        self.assertEqual(f.serialized_value, '')

    def test_set_empty_serialized_value(self):
        f = Integer('foo')
        f.serialized_value = ''

        self.assertTrue(f.valid)
        self.assertEqual(f.serialized_value, '')
        self.assertEqual(f.value, empty)

    def test_set_value(self):
        f = Integer('foo')
        f.value = 42

        self.assertEqual(f.value, 42)
        self.assertEqual(f.serialized_value, '42')

    def test_set_serialized_value(self):
        f = Integer('foo')
        f.serialized_value = '  42 '

        self.assertTrue(f.valid)
        self.assertEqual(f.serialized_value, '  42 ')
        self.assertEqual(f.value, 42)

    def test_set_bad_serialized_value(self):
        f = Integer('foo')
        f.serialized_value = 'meow'

        self.assertFalse(f.valid)
        self.assertEqual(f.serialized_value, 'meow')


class TestDecimal(unittest.TestCase):

    def test_defaults(self):
        f = Decimal('foo')

        self.assertIs(f.value, empty)
        self.assertIs(f.serialized_value, '')

    def test_set_empty_value(self):
        f = Decimal('foo')
        f.value = empty

        self.assertEqual(f.serialized_value, '')

    def test_set_empty_serialized_value(self):
        f = Decimal('foo')
        f.serialized_value = ''

        self.assertTrue(f.valid)
        self.assertEqual(f.serialized_value, '')
        self.assertEqual(f.value, empty)

    def test_set_value(self):
        f = Decimal('foo')
        f.value = decimal.Decimal('123.45')

        self.assertEqual(f.value, decimal.Decimal('123.45'))
        self.assertEqual(f.serialized_value, '123.45')

    def test_set_serialized_value(self):
        f = Decimal('foo')
        f.serialized_value = '  123.45 '

        self.assertTrue(f.valid)
        self.assertEqual(f.serialized_value, '  123.45 ')
        self.assertEqual(f.value, decimal.Decimal('123.45'))

    def test_set_bad_serialized_value(self):
        f = Decimal('foo')
        f.serialized_value = 'meow'

        self.assertFalse(f.valid)
        self.assertEqual(f.serialized_value, 'meow')


if __name__ == '__main__':
    unittest.main()
