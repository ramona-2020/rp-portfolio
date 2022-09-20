from django.shortcuts import render, redirect

from personal_portfolio.expenses_tracker.forms.profile_form import CreateProfileForm, EditProfileForm, DeleteProfileForm
from personal_portfolio.expenses_tracker.forms.expense_form import ExpenseForm, DeleteExpenseForm
from personal_portfolio.expenses_tracker.models import Profile, Expense


def get_profile():
    return Profile.objects.first()


def homepage(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    profile = Profile.objects.first()
    profile_expenses = Expense.objects.filter(profile=profile)

    total_expenses = sum(expense.price for expense in profile_expenses)
    budget_left = profile.budget - total_expenses

    context = {
        'profile': profile,
        'profile_expenses': profile_expenses,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context)


def show_profile(request):
    profile = Profile.objects.first()
    if profile:
        profile_expenses = Expense.objects.filter(profile=profile)

        total_expenses = sum(expense.price for expense in profile_expenses)
        budget_left = profile.budget - total_expenses

        expenses_count = len(profile_expenses)

    else:
        return redirect(request, '404.html')

    context = {
        'profile': profile,
        'budget_left': budget_left,
        'expenses_count': expenses_count,
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()

    if profile:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('show profile')
        else:
            form = EditProfileForm(instance=profile)
    else:
        return redirect(request, '404.html')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    if profile:
        if request.method == 'POST':
            form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
            return redirect('homepage')
        else:
            form = DeleteProfileForm()
    else:
        return render(request, '404.html')

    context = {
        'form': form
    }
    return render(request, 'profile-delete.html', context)


def expense_create(request):
    profile = get_profile()
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=Expense(profile=profile))
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ExpenseForm()

    context = {
        'form': form
    }
    return render(request, 'expense-create.html', context)


def expense_edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,
    }
    return render(request, 'expense-edit.html', context)


def expense_delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense.delete()
            return redirect('homepage')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,
    }
    return render(request, 'expense-delete.html', context)
