from django import forms
from .models import Tourism
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField 

class RapistForm(forms.ModelForm):
    details = RichTextUploadingField()

    class Meta:
        model = Tourism
        fields = '__all__'

