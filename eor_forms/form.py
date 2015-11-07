# coding: utf-8

import logging
log = logging.getLogger(__name__)

import datetime

from .container import Mapping
from .empty import empty


class Form(Mapping):
    def __init__(self, request, **kwargs):
        self._request = request
        super().__init__(**kwargs)

    @property
    def request(self):
        return self._request

    def render_csrf_field(self):
        """
        <form>
            ${c.form.render_csrf_field() | n}
        </form
        Note: will throw an exception if request was not passed to the constructor
        """
        token = self._request.session.get_csrf_token()
        return '<input type="hidden" name="csrf_token" value="%s">' % token  # TODO use eor-htmlgen!

    def from_request(self):
        """
        my_form = my_form.from_request(request)
        Pyramid only
        """

        if self.request.content_type.startswith('application/json'):
            self.serialized_value = self.request.json_body  # TODO possible exceptions
        else:
            self.serialized_value = peppercorn.parse(list(self.request.POST.items()))

        return self

    def from_object(self, obj):
        # TODO hierarchy
        for name, child in self._children.items():
            try:
                child.value = getattr(obj, name)
            except AttributeError:
                pass

        return self

    def to_object(self, obj):
        # TODO hierarchy
        for name, child in self._children.items():
            if child.value is not empty:
                setattr(obj, name, child.value)

        return self
