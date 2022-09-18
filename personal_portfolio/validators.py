from django.core.exceptions import ValidationError


def validate_only_chars(value: str):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters.")


def validate_maximum_file_size(value):
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError("Max file size is 5.00 MB")

