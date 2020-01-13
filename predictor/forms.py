from django import forms


class ApprovalForm(forms.Form):
    Obtainmarks = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter obtain marks'}))
    Time = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter how much time it take to solve questions'}))

