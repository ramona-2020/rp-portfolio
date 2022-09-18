from django.urls import path

from personal_portfolio.expenses_tracker.views import homepage, profile, profile_edit, profile_delete, expense_create, expense_edit, expense_delete

urlpatterns = [
    path('', homepage, name='homepage'),
    path('create/', expense_create, name='expense create'),
    path('edit/<pk>/', expense_edit, name='expense edit'),
    path('delete/<pk>/', expense_delete, name='expense delete'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete')
]
