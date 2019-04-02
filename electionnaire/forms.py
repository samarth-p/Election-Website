from django import forms
from captcha.fields import CaptchaField

class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()

class PostForm(forms.Form):
    image = forms.ImageField()
    caption = forms.CharField()