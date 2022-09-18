from django import forms

from personal_portfolio.expenses_tracker.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')


class DeleteExpenseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')



