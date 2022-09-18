from io import BytesIO

from PIL import Image
from django.core.files import File


class BootstrapFormMixin:

    fields = {}

    def _init_bootstrap_form_controls(self):
        for name, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})

            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'

            if name == 'image':
                field.widget.attrs['class'] += ' form-file'


def compress(image: Image, compress_level=90):
    image = Image.open(image)
    image_io = BytesIO()
    image.save(image_io, image.format, quality=compress_level)

    new_image = File(image_io, name=image.name)
    return new_image
