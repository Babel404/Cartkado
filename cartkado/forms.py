from django import forms

class CreateNewGiftcard(forms.Form):
	amount = forms.FloatField(label="Amount")

class DebitGiftcard(forms.Form):
	unique_key = forms.CharField(label="Key")
	amount = forms.FloatField(label="Amount")