import unittest
from unittest.mock import MagicMock

from eor_forms import ValueField, empty


class TestValueField(unittest.TestCase):

    def test_defaults(self):
        f = ValueField('foo')

        self.assertEqual(f.name, 'foo')
        self.assertIs(f.value, empty)
        self.assertIs(f.serialized_value, empty)
        self.assertEqual(f.valid, True)
        self.assertIsNone(f.error)

    def test_default_value(self):
        f = ValueField('foo', default=42)

        self.assertEqual(f.value, 42)
        self.assertEqual(f.serialized_value, 42)

    def test_set_value(self):
        f = ValueField('foo')
        f.value = 10

        self.assertEqual(f.value, 10)
        self.assertEqual(f.serialized_value, 10)

        f = ValueField('foo', default=42)
        f.value = 10

        self.assertEqual(f.value, 10)
        self.assertEqual(f.serialized_value, 10)

    def test_set_serialized_value(self):
        f = ValueField('foo')
        f.serialized_value = 20

        self.assertEqual(f.serialized_value, 20)
        self.assertEqual(f.value, 20)

    def test_serialize(self):
        mock_serialize = MagicMock(return_value=2)

        class ValueFieldSubclass(ValueField):

            def serialize(self, val):
                return mock_serialize(val)

        f = ValueFieldSubclass('aaa')

        mock_serialize.assert_called_once_with(empty)
        self.assertEqual(f.serialized_value, 2)

        mock_serialize.reset_mock()

        f.value = 1

        self.assertEqual(f.value, 1)
        self.assertEqual(f.serialized_value, 2)
        mock_serialize.assert_called_once_with(1)

    def test_deserialize(self):
        mock_deserialize = MagicMock(return_value=1)

        class ValueFieldSubclass(ValueField):

            def deserialize(self, val):
                return mock_deserialize(val)

        f = ValueFieldSubclass('aaa')

        mock_deserialize.assert_not_called()

        f.serialized_value = 2

        self.assertEqual(f.value, 1)
        self.assertEqual(f.serialized_value, 2)
        mock_deserialize.assert_called_once_with(2)

    def test_render(self):
        pass

    def test_validate(self):
        pass


if __name__ == '__main__':
    unittest.main()
