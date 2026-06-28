import re
from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        youtube_regex = re.compile(r'(https?://)?(www\.)?(youtube.com)/')
        tmp_val = dict(value).get(self.field)
        if not youtube_regex.match(tmp_val):
            raise ValidationError(f"Значение {value} не является допустимым URL")

        return True