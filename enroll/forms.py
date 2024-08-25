from django import forms
from .models import Registration

class UserRegistration(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('id','name','email','password','reenter_Password')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'reenter_Password': forms.PasswordInput(attrs={'class':'form-control'})
        }
    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get("password")
        reenter_Password = self.cleaned_data.get("reenter_Password")

        if password != reenter_Password:
            raise forms.ValidationError("Password Does not match Re enter your password")
        return cleaned_data
    

            



