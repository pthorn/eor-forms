# coding: utf-8

import logging
log = logging.getLogger(__name__)

import re

from .empty import empty
from .render import Input


class ValueField(object):
    def __init__(self, name, default=empty, validators=None, renderer=None):
        self._name = name
        self._value = default
        self._serialized_value = self.serialize(default)
        self._validators = validators or []
        self._errors = None  # TODO
        self._renderer = renderer or Input()

    @property
    def name(self):
        return self._name

    # value

    @property
    def value(self):
        """
        :return: deserialized value
        """
        return self._value

    @value.setter
    def value(self, val):
        self._value = val
        self._serialized_value = self.serialize(val)

    @property
    def serialized_value(self):
        """
        :return: serialized value (as used in HTML and submitted by client)
        """
        return self._serialized_value

    @serialized_value.setter
    def serialized_value(self, val):
        self._deserialize_and_validate(val)  # TODO do we need this method

    # TODO compatibility
    @property
    def cvalue(self):
        return self.serialized_value

    # validation

    @property
    def valid(self):
        return not self._errors

    @property
    def error(self):
        return self._errors

    def validator(self, validator):
        self._validators.append(validator)  # TODO revalidate?
        return self

    def invalid(self, message):
        self._errors = message

    def _deserialize_and_validate(self, val):
        self._errors = None

        self._serialized_value = val
        self._value = self.deserialize(val)

        if self.valid:
            for validator in self._validators:
                validator(self)
                if self._errors:
                    break  # TODO

    # render

    def renderer(self, renderer):
        self._renderer = renderer
        return self

    def render(self, **kwargs):
        return self._renderer.render(self, kwargs)

    def iclass(self, invalid_class, valid_class=''):
        return valid_class if self.valid else invalid_class

    # override

    def serialize(self, val):
        return val

    def deserialize(self, val):
        return val


class String(ValueField):
    def __init__(self, name, strip=True, **kwargs):
        self._strip = strip
        #kwargs.setdefault('renderer', )
        super().__init__(name, **kwargs)

    def serialize(self, val):
        return '' if val is empty else str(val)

    def deserialize(self, val):
        if self._strip:
            val = val.strip()

        return str(val) if val else empty


PHONE_RE = re.compile(r'^(8|\+7)?\d{10}$')

class Phone(ValueField):
    def serialize(self, val):
        return '' if val is empty else str(val)

    def deserialize(self, val):
        val = val.strip()

        if not val:
            return empty

        val = re.sub(r'[ -()]', '', val)

        if PHONE_RE.match(val) is None:
            self.invalid('Неправильный формат номера телефона')

        if val.startswith('8'):
            val = '+7' + val[1:]

        if not val.startswith('+7'):
            val = '+7' + val

        return val


class Integer(ValueField):
    def __init__(self, name, message='Integer expected', **kwargs):
        self._message = message
        #kwargs.setdefault('renderer', )
        super().__init__(name, **kwargs)

    def serialize(self, val):
        return '' if val is empty else str(val)

    def deserialize(self, val):
        val = val.strip()

        try:
            return empty if len(val) == 0 else int(val)  # TODO exception -> invalid
        except ValueError:
            self.invalid(self._message)


class Boolean(ValueField):
    pass


class Date(ValueField):
    pass


class DateTime(ValueField):
    pass
