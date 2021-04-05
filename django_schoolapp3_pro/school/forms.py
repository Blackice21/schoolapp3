from .models import School
from django.forms import ModelForm

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = '__all__'