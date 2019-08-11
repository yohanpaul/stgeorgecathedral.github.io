import datetime

from youth.models import *

from django import forms  
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.forms import AuthenticationForm
from django.utils.safestring import mark_safe

class HorizontalRadioRenderer(forms.RadioSelect):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class SurveyForm(forms.ModelForm): 

    class Meta:  
        model = YouthDetails  
        exclude = ('created_on', 'updated_on', 'is_active')

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.fields['ward'] = forms.ModelChoiceField(queryset=Ward.objects.filter(is_active=True))
        self.fields['Region'] = forms.ModelChoiceField(queryset=Region.objects.filter(is_active=True))
        self.fields['blood_group'] = forms.ModelChoiceField(queryset=BloodGroup.objects.filter(is_active=True))
        self.fields['father_job'] = forms.ModelMultipleChoiceField(queryset=Profession.objects.filter(is_active=True))
        self.fields['mother_job'] = forms.ModelMultipleChoiceField(queryset=Profession.objects.filter(is_active=True))
        self.fields['job'] = forms.ModelMultipleChoiceField(queryset=Profession.objects.filter(is_active=True))
        self.fields['married'] = forms.ChoiceField(label="Married"
        , choices=((True, 'Yes'), (False, 'No')), widget=forms.RadioSelect())
        self.fields['profession'] = forms.ChoiceField(label="profession", choices=(("1","Study"),("2","Job")), widget=forms.RadioSelect())
        
        for visible in self.visible_fields():
            if visible.field.label in("Married", "profession"):
                pass
            else:
                visible.field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email_id = self.cleaned_data['email']
        if email_id:
            validate_email(email_id)
        return email_id