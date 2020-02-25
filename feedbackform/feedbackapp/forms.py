from django import forms
class feedbackForm(forms.Form):
    name=forms.CharField(
        label="enter your name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    rating=forms.IntegerField(
        label="enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your rating'
            }
        )
    )
    feedback=forms.CharField(
        label="enter the feedback",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'yourFeedback'
            }
        )
    )