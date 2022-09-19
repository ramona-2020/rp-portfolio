# Generated by Django 4.1.1 on 2022-09-18 17:32

from django.db import migrations, models
import personal_portfolio.expenses_tracker.validators


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_tracker', '0004_alter_expense_image_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.URLField(verbose_name='Link to Image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[
                personal_portfolio.expenses_tracker.validators.MaxFileSizeInMBValidator(5)], verbose_name='Profile Image'),
        ),
    ]
