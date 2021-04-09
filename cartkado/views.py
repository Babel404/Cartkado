from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from datetime import datetime
from .models import Cartkado, Transaction
from .forms import CreateNewGiftcard, DebitGiftcard

def index(response, id):
	card = Cartkado.objects.get(id=id)
	return render(response, "cartkado/card.html", {"amount":card.amount})

def home(response):
	return render(response, "cartkado/home.html", {})

def create(response):
	if not response.user.is_authenticated:
		return redirect('/login')
	if response.method == "POST":
		form = CreateNewGiftcard(response.POST)

		if form.is_valid():
			unique_key = uuid.uuid4()
			amount = form.cleaned_data["amount"]
			giftcard = Cartkado(unique_key=unique_key, amount=amount, created_at=datetime.now())
			giftcard.save()
			return render(response, "cartkado/new_giftcard.html", {"unique_key":unique_key,"amount":amount})

	else:
		form = CreateNewGiftcard()
	return render(response, "cartkado/create.html", {"form":form})

def debit(response):
	if not response.user.is_authenticated:
		return redirect('/login')
	user = response.user
	if response.method == "POST":
		form = DebitGiftcard(response.POST)

		if form.is_valid():
			card = Cartkado.objects.get(unique_key=form.cleaned_data["unique_key"])
			amount_debit = form.cleaned_data["amount"]
			if amount_debit <= card.amount :
				card.amount-=amount_debit
				card.save()
				transaction = Transaction(name=user.username, amount = amount_debit, card_key = card.unique_key, created_at=datetime.now())
				transaction.save()
				return render(response, "cartkado/debit_giftcard.html", {"unique_key":card.unique_key,"amount_debit":amount_debit})
	else:
		form = DebitGiftcard()
	return render(response, "cartkado/debit.html", {"form":form})
