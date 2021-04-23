from django import forms
from .models import  Book, Category, Isbin, Tag
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = "__all__"
        exclude =("Isbin",)

    

    def clean(self):
        super(BookForm, self).clean()
        content = self.cleaned_data.get('content')
        title = self.cleaned_data.get('title')
        Categories=self.cleaned_data.get('categories')


        if len(title) < 10 :
            raise ValidationError("title must be bigger than 10 chars")
        if len(title) > 50 :
            raise ValidationError("title must be smaller than 50 chars")
        

        
        

        return self.cleaned_data



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category 
        fields = "__all__"

    def clean(self):
        super(CategoryForm, self).clean()
        name = self.cleaned_data.get('name')

        if len(name) <= 2 :
            raise ValidationError(" Category name must be bigger than 2 chars")

        return self.cleaned_data
        

