# coding: utf-8

from eor_htmlgen import Tag, Text, RawText


class Input(object):
    """
    <input type="<type>">
    """

    def __init__(self, type='text'):
        self.type = type

    def render(self, field, rargs):
        rargs.setdefault('type', self.type)
        return Tag('input', name=field.name, value=field.cvalue, **rargs).render()


class Textarea(object):
    """
    <textarea>
    """

    def render(self, field, rargs):
        return Tag('textarea', field.cvalue, name=field.name, **rargs).render()


class Select(object):
    """
    <select>
      <option>
    </select>
    """

    def __init__(self, options, multiple=False):
        """
        :param options: array of tuples (value, label)
        :param multiple: boolean
        """
        self.multiple = multiple
        self.options = options

    def render(self, field, rargs):
        r_options = [Tag('option', opt[1], value=opt[0], selected=(opt[0] == field.cvalue))
                     for opt in self.options]

        rargs.setdefault('multiple', self.multiple)

        select = Tag('select', name=field.name, **rargs).add(r_options)
        return select.render()


class MultiSelect(object):
    """
     options = [html.option(value=val, selected = unicode(val) in cstruct)(text) for val, text in choices]
    return html.select(multiple=True, name=field.name, **(attrs or {}))(options)
    """
    pass


class RadioButtons(object):

    def __init__(self, options):
        """
        :param options: array of tuples (value, label)
        """
        self.options = options

    def render(self, field, rargs):
        inputs = [Tag('li').add([
            Tag('input', type='radio', name=field.name, value=opt[0], checked=(opt[0] == field.cvalue)),
            Text(opt[1])
        ]) for opt in self.options]

        return Tag('ul', **rargs).add(inputs).render()


class Checkbox(object):
    """
    """

    def render(self, field, rargs):
        return Tag('input', type='checkbox', name=field.name,
                   value='true', checked=(field.cvalue == 'true'), **rargs).render()


class CheckBoxes(object):
    """
    checkboxes = [[
                      html.input(type="checkbox", name=field.name, value=val, checked = cstruct == val),
                      html.span(text),
                      html.br] for val, text in choices]
    return html.div(**kwargs)(checkboxes)
    """
    # TODO
    pass


class File(object):
    pass
    # TODO
    #attrs = attrs or dict()
    #if field.readonly: # does it make sense for file fields?
    #    attrs['readonly'] = True
    #return html.input(name=field.name, type="file", **attrs)


if __name__ == '__main__':

    class C(object):
        def __init__(self, val, text):
            self.val = val
            self.text = text

    options = [C(1, 'one'), C(2, 'two'), C(3, 'th"r<e>e')]
    current_val = 2

    for x in range(100):
        select = Tag('select', multiple=True).add(
            [Tag('option', opt.text, value=opt.val, selected=opt.val == current_val) for opt in options]
        )

    print(select.render())
