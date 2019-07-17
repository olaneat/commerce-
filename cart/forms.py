from django import forms

class ProductAdminForm(forms.Form):
    quantity = forms.IntegerField(widget = forms.TextInput(attrs = {'size': '2', 'value': '1',\
            'class' : 'quantity', 'maxlength' : '7' }),
            error_messages = {'invalid': 'kindly make an entry'},
            min_value = 1)
    product_slug = forms.CharField(widget = forms.HiddenInput())

    def __init__(self, request = None, *args, **kwargs):
        self,request = request
        super(ProductAdmin, self).__init__(*args, **kwargs)
    
    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError('Your cookie must be enabled')
        return self.cleaned_data()

         
