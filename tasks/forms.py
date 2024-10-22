from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        widgets = {
            'complete_before': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'complete_before')
        widgets = {
            'complete_before': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'