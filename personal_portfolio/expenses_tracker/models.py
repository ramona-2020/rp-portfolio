from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from personal_portfolio.expenses_tracker.validators import validate_only_chars, MaxFileSizeInMBValidator


class Profile(models.Model):

    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15

    BUDGET_MIN_VALUE = 0

    MAX_FILE_SIZE_IN_MB = 5

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
            MaxFileSizeInMBValidator(MAX_FILE_SIZE_IN_MB)
        ]
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

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
