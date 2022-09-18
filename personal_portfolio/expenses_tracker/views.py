from django.http import Http404
from django.shortcuts import render, redirect

from personal_portfolio.expenses_tracker.forms.profile_form import CreateProfileForm, DeleteProfileForm
from personal_portfolio.expenses_tracker.forms.expense_form import ExpenseForm, DeleteExpenseForm
from personal_portfolio.expenses_tracker.models import Profile, Expense


def get_profile():
    return Profile.objects.first()


def homepage(request):
    has_profile = Profile.objects.count()
    form = CreateProfileForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
    elif has_profile == 0:
        form = CreateProfileForm()
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)

    profile = Profile.objects.first()
    profile_expenses = Expense.objects.filter(profile=profile).all()

    total_expenses = sum(expense.price for expense in profile_expenses)
    budget_left = profile.budget - total_expenses

    context = {
        'profile': profile,
        'budget_left': budget_left,
        'profile_expenses': profile_expenses,
    }
    return render(request, 'home-with-profile.html', context)


def profile(request):
    profile = Profile.objects.first()
    profile_expenses = Expense.objects.filter(profile=profile)

    total_expenses = sum(expense.price for expense in profile_expenses)
    budget_left = profile.budget - total_expenses

    form = CreateProfileForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        'profile': profile,
        'budget_left': budget_left,
        'profile_expenses': profile_expenses,
    }

    return render(request, 'profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()

    if profile is not None:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
        else:
            form = CreateProfileForm(instance=profile)
    else:
        return Http404('Profile not found')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        profile.delete()

        form = CreateProfileForm()
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)
    else:
        form = DeleteProfileForm()

    context = {
        'profile': profile,
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
