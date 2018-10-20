from protorpc import messages


class JsonField(messages.StringField):
    type = dict


class ListField(messages.StringField):
    type = list
