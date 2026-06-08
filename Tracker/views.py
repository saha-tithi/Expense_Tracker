from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Tracker.models import Transaction


def index(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')

        if not description.strip():
            messages.info(request, "Description cannot be blank")
            return redirect('/')

        try:
            amount = float(amount)
        except ValueError:
            messages.info(request, "Amount must be a number")
            return redirect('/')

        Transaction.objects.create(
            description=description,
            amount=amount
        )

        messages.success(request, "Transaction added")
        return redirect('/')

    transactions = Transaction.objects.all()

    income = sum(t.amount for t in transactions if t.amount > 0)
    expense = sum(abs(t.amount) for t in transactions if t.amount < 0)
    balance = income - expense

    return render(request, 'index.html', {
        'transactions': transactions,
        'income': income,
        'expense': expense,
        'balance': balance,
    })
def delete_transaction(request, uuid):
    transaction = get_object_or_404(
        Transaction,
        uuid=uuid
    )

    transaction.delete()

    messages.success(request, "Transaction deleted")
    return redirect('/')