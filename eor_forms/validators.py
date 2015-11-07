# coding: utf-8

import logging
log = logging.getLogger(__name__)

import datetime
import re

from .empty import empty


def Required(message='Field is required'):
    def validate(field):
        if field.value is empty:
            field.invalid(message)

    return validate


class Range(object):

    def __init__(self, min=None, max=None, message='Range Error'):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, field):
        if field.value is empty:
            return

        if self.min is not None:
            if field.value < self.min:
                field.invalid(self.message)

        if self.max is not None:
            if field.value > self.max:
                field.invalid(self.message)


class Length(object):

    def __init__(self, min=None, max=None, message='Length Error'):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, field):
        if field.value is empty:
            return

        if self.min is not None:
            if len(field.value) < self.min:
                field.invalid(self.message)

        if self.max is not None:
            if len(field.value) > self.max:
                field.invalid(self.message)


EMAIL_RE = re.compile("(?i)^[A-Z0-9._%!#$%&'*+-/=?^_`{|}~()]+@[A-Z0-9]+([.-][A-Z0-9]+)*\.[A-Z]{2,22}$")

def Email(message='Bad email address'):
    def validate(field):
        if field.value is empty:
            return

        if EMAIL_RE.match(field.value) is None:
            field.invalid(message)

    return validate

