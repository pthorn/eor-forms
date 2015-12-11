import unittest
from unittest.mock import MagicMock

from eor_forms import ValueField, Mapping, empty


class TestMapping(unittest.TestCase):

    def test_defaults(self):
        f = Mapping()

        self.assertEqual(f.value, {})
        self.assertEqual(f.serialized_value, {})
        self.assertEqual(f.valid, True)
        self.assertEqual(f.error, {})

    def test_add_children(self):
        child = ValueField('foo')
        f = Mapping()

        self.assertIs(f, f.add(child))
        self.assertIs(f.foo, child)

        child2 = ValueField('bar')

        self.assertIs(f, f.add(child2))
        self.assertIs(f.bar, child2)
        self.assertIs(f.foo, child)

    def test_child_values(self):
        f = Mapping().add(ValueField('foo')).add(ValueField('bar'))

        self.assertEqual(f.value, {'foo': empty, 'bar': empty})
        self.assertEqual(f.serialized_value, {'foo': empty, 'bar': empty})
        self.assertEqual(f.valid, True)
        self.assertEqual(f.error, {})


if __name__ == '__main__':
    unittest.main()
