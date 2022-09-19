from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = "Ensure this value contains only letters."


def validate_only_chars(value: str):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)


@deconstructible
class MaxFileSizeInMBValidator:

    def __init__(self, max_size: int):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        max_size_in_mb = self.__megabytes_to_bytes(filesize)
        if filesize > max_size_in_mb:
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f"Max file size is {self.max_size:.2f} MB"
