from django.contrib.auth.forms import AuthenticationForm
from django import forms
from . models import Recipe,RecipeDetails
from django.forms import ModelForm

class RecipeForm(ModelForm):
    # description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Recipe
        exclude = ('owner',)

class RecipeDetailsForm(ModelForm):

    extra_field_count = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        extra_fields = kwargs.pop('extra', 0)

        super(RecipeDetailsForm, self).__init__(*args, **kwargs)
        self.fields['extra_field_count'].initial = extra_fields

        for index in range(int(extra_fields)):
            # generate extra fields in the number specified via extra_fields
            self.fields['extra_field_{index}'.format(index=index)] = \
                forms.CharField()

    class Meta:

        model=RecipeDetails
        exclude = ('owner','recipe','number','recipedescription')