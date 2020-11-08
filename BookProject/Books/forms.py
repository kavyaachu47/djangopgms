from django import forms
from Books.models import Book
from django.forms import ModelForm
class BookCreateForm(ModelForm):
    # book_name = forms.CharField(max_length=120)
    # author = forms.CharField(max_length=120)
    # price = forms.IntegerField()
    # pages = forms.IntegerField()
    class Meta(ModelForm):
        model=Book
        model=Book
        fields="__all__"

    def clean(self):
        clean_data=super().clean()
        book_name=clean_data.get("book_name")
        price=clean_data.get("price")
        book=Book.objects.filter(book_name=book_name)

        if book:
            msg="already exist"
            self.add_error('book_name',msg)
        if price<0:
            msg="enter value greater than zero"
            self.add_error('price',msg)

class BookUpdate(ModelForm):
    class Meta(ModelForm):
        model=Book
        fields="__all__"