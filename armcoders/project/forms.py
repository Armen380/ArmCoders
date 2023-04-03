from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"nameFormInput",'placeholder': 'Գրեք ձեր անունը'}),max_length=100,label="")
    comment_text = forms.CharField(widget=forms.Textarea(attrs={"class":"commentFormInput",'placeholder': 'Գրեք Մեկնաբանությունը'}),label="")

class SearchForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"search",'placeholder': 'Գտեք ձեր Նախընտրած Գիրքը,Ծրագիրը'}),max_length=100,label="")