# coding: utf-8

import logging
log = logging.getLogger(__name__)


class List(object):
    pass


class Mapping(object):
    def __init__(self):
        self._children = {}
        self._validators = []  # validators or
        #self._errors = None  # TODO ???

    # children

    def __getattr__(self, attr):
        try:
            return self._children[attr]
        except KeyError:
            raise AttributeError(attr)

    def add(self, child):
        self._children[child.name] = child
        return self

    # values

    @property
    def value(self):
        return {k : child.value for k, child in self._children.items()}

    @value.setter
    def value(self, val):
        for name, child in self._children.items():
            try:
                child.value = val[name]
            except KeyError:
                pass

    @property
    def serialized_value(self):
        return {k : child.serialized_value for k, child in self._children.items()}

    @serialized_value.setter
    def serialized_value(self, val):
        for name, child in self._children.items():
            if name in val:
                child.serialized_value = val[name]

    # validation

    @property
    def valid(self):
        for validator in self._validators:
            validator(self)
            # TODO
            #if self._errors:
            #    break  # TODO

        res = all(child.valid for child in self._children.values())

        return res

    @property
    def error(self):
        return {k : child.error for k, child in self._children.items() if not child.valid}

    def validator(self, validator):
        self._validators.append(validator)  # TODO revalidate?
        return self
