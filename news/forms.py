from django import forms
from .models import Post, Category


# choices = [('Sports', 'Sports'), ('Entertainment','Entertainment'), ('Education', 'Education')]
choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'category', 'body', 'title_tag','header_image')

		widgets = {
				'title': forms.TextInput(attrs={'class': 'form-control'}),
				# 'author': forms.Select(attrs={'class': 'form-control'}),
				'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder', 'type':'hidden'}),
				'category': forms.Select(choices= choices, attrs={'class': 'form-control'}),
				'body': forms.Textarea(attrs={'class': 'form-control'}),
				'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
		}

class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'category', 'body', 'title_tag')

		widgets = {
				'title': forms.TextInput(attrs={'class': 'form-control'}),
				'category': forms.Select(choices= choices, attrs={'class': 'form-control'}),
				'body': forms.Textarea(attrs={'class': 'form-control'}),
				'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
		}


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name',)

		widgets = {
				'name': forms.TextInput(attrs={'class': 'form-control'}),
				
		}