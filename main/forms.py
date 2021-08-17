from django import forms
from .models import Response

class ResponseForm(forms.ModelForm):
	class Meta:
		model = Response
		fields = "__all__"
		widgets = {
		'name':forms.TextInput(attrs={'class':'form-control'}),
		'email':forms.TextInput(attrs={'class':'form-control'}),
		'feedback':forms.Textarea(attrs={'class':'form-control'})
		}