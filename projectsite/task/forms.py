from django import forms
from django.forms import ModelForm
from .models import Task, Category, Priority, SubTask, Note


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Describe the task...'
            }),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'deadline': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'parent_task': forms.Select(attrs={'class': 'form-select'}),
        }


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'task': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your note here...'
            }),
        }