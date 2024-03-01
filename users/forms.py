from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=15, widget=forms.PasswordInput)
    age = forms.IntegerField()
    avatar = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        password_confirm = cleaned_data["password_confirm"]
        if password != password_confirm:
            raise forms.ValidationError('Passwords are not matching')
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class SMSCodeForm(forms.Form):
    code = forms.CharField(max_length=4)


class ConfirmForm(forms.Form):
    code = forms.CharField(max_length=6, required=True)
