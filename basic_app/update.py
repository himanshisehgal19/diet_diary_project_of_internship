from django import forms
from basic_app.models import food_diary

class UpdateFood(forms.ModelForm):
    class Meta:
        model = food_diary
        fields = '__all__'