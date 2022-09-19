from django.contrib import admin

from personal_portfolio.expenses_tracker.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
