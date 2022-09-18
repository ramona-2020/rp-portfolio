from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from personal_portfolio.validators import validate_only_chars, validate_maximum_file_size


class Profile(models.Model):

    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    BUDGET_MIN_VALUE = 0

    budget = models.FloatField(
        default=BUDGET_MIN_VALUE,
        validators=[
            MinValueValidator(BUDGET_MIN_VALUE)
        ]
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name="First Name",
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_chars
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name="Last Name",
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_chars
        ]
    )

    image = models.ImageField(
        verbose_name='Profile Image',
        upload_to='images',
        blank=True,
        null=True,
        validators=[
            validate_maximum_file_size
        ]
    )


class Expense(models.Model):

    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )
    image = models.URLField(
        verbose_name='Link to Image'
    )
    price = models.FloatField()

    description = models.TextField(
        blank=True,
        null=True
    )

    profile = models.ForeignKey(Profile,
                                on_delete=models.CASCADE)
