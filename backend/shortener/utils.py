import base64
from io import BytesIO

from django.conf import settings
from random import choice
from string import ascii_letters, digits
import qrcode

SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVALIABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVALIABLE_CHARS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):
    random_code = create_random_code()
    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)

    return random_code


def create_qr_code(result):
    result = qrcode.make(result)
    stream = BytesIO()
    result.save(stream)
    img_str = base64.b64encode(stream.getvalue()).decode("utf-8")
    return img_str
