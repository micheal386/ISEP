from django import forms

class AddForm_OTP(forms.Form):
	usr_ans = forms.CharField(max_length = 1000)

class AddForm_Cas(forms.Form):
	a = forms.IntegerField()
	b = forms.IntegerField()

