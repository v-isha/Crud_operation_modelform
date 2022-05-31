from django.core import validators
from django import forms
from .models import customer

class customerregistration(forms.ModelForm):
    
    class Meta:
      model = customer
      fields = ['customer_id','name','email','password']
      error_messages={
                    "customer_id":{"required":"please enter numeric data"},
                    "name":{"required":"please enter alphabates"},
                    "email":{"required":"please enter vaild email"},
                    }
      labels = {'customer_id':'ID','name':"Enter Name",'email':'Enter Email','password':"Enter Password"}
      widgets = {
            'customer_id':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),

                }
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valid= self.cleaned_data['customer_id']
    #     valname =self.cleaned_data['name']
    #     if valid.isalpha():
    #         raise forms.ValidationError("pls enter numeric value")
    #     if valname.isdigit():
    #         raise forms.ValidationError("pls enter Alphabates value")