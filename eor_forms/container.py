# coding: utf-8

import logging
log = logging.getLogger(__name__)


class List(object):
    def __init__(self, name, child_factory):
        self._name = name
        self._child_factory = child_factory
        self._children = []
        self._validators = []  # validators or

    @property
    def name(self):
        return self._name

    # children

    def __len__(self):
        return len(self._children)

    def __getitem__(self, key):
        return self._children[key]  # will raise IndexError as expected

    def append(self, child):
        assert self._child is None  # TODO
        self._child = child
        return self

    def removeAt(self, idx):
        pass

    # values

    @property
    def value(self):
        return [child.value for child in self._children]

    @value.setter
    def value(self, val):
        def child_with_value(val):
            child = self._child_factory()
            child.value = val
            return child

        self._children = [child_with_value(i) for i in val]

    @property
    def serialized_value(self):
        return [child.serialized_value for child in self._children]

    @serialized_value.setter
    def serialized_value(self, val):
        def child_with_value(val):
            child = self._child_factory()
            child.serialized_value = val
            return child

        self._children = [child_with_value(i) for i in val]

    # validation

    @property
    def valid(self):
        for validator in self._validators:
            validator(self)
            # TODO
            # if self._errors:
            #    break  # TODO

        return all(child.valid for child in self._children)

    @property
    def error(self):
        return {k: child.error for k, child in self._children.items() if not child.valid}

    def validator(self, validator):
        self._validators.append(validator)  # TODO revalidate?
        return self


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
            try:
                child.serialized_value = val[name]
            except KeyError:
                pass

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
