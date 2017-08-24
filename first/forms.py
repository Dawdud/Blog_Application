from django import forms
from first.models import Books, Category
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name= forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name= forms.CharField(max_length=30, required= False, help_text='Optional.')
    email=forms.EmailField(max_length=260, help_text='Required Email')
    class Meta:
        model= User
        fields= ('username','first_name','last_name','email')


class CategoryForm(forms.ModelForm):
    name= forms.CharField(max_length=128, help_text="please enter the category name.")
    slug= forms.CharField(widget=forms.HiddenInput(), required= False)
    class Meta:
        model= Category
        fields= ('name',)



class BookForm(forms.ModelForm):
    Title= forms.CharField(max_length=128,required=True, help_text="Please enter the  Book Title")
    OriginalTitle= forms.CharField(max_length=128,required=True, help_text="Please enter the Book Original Title")
    Author= forms.CharField(max_length=128,required=True, help_text="Please enter the name of Author")
    Publisher= forms.CharField(max_length=128,required=True, help_text="Please enter the publisher")
    ISBN= forms.IntegerField( initial=0,required=True, help_text="Please enter the ISBN")
    DatePublished= forms.DateField(required=True,help_text="Plesae enter  published date like this Year-Month-Day ")
    slugbook= forms.CharField(widget=forms.HiddenInput(), required= False)
    def clean(self):
        cleaned_data= self.cleaned_data
        url= cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url= 'http://'+url
            cleaned_data['url']=url

    class Meta:
        model= Books
        fields= ('Title','OriginalTitle','Author','Publisher','ISBN','DatePublished')
        exclude= ('category',)
