from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from django.forms import ModelForm




class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=200)
    note_content = RichTextField(blank=True, null=True)
    #note_content = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.note_title




class NoteForm(ModelForm):
	class Meta:
		model = Note
		fields = '__all__'