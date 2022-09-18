from django import template
from personal_portfolio.expenses_tracker.models import Profile

register = template.Library()


@register.simple_tag
def has_profile():
    return Profile.objects.count() > 0
