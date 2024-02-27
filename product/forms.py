from django import forms
from product.models import Product, Review, Category


class ProductForm(forms.Form):
    name_of_product = forms.CharField(max_length=100, min_length=3)
    description = forms.CharField(widget=forms.Textarea)
    image_of_product = forms.ImageField(required=False)


    def clean_name_of_product(self):
        name_of_product = self.cleaned_data['name_of_product']
        if "python" in name_of_product.lower():
            raise forms.ValidationError("Python is not allowed")

        return name_of_product.capitalize()

    def clean_description(self):
        description = self.cleaned_data['description']
        if "django" in description.lower():
            raise forms.ValidationError("Django is not allowed")

        return description

    def clean(self):
        cleaned_data = super().clean()
        name_of_product = cleaned_data.get('name_of_product')
        description = cleaned_data.get('description')
        if name_of_product and description:
            if name_of_product.lower() == description.lower():
                raise forms.ValidationError("Title and content must be different")

        return cleaned_data


class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name_of_product', 'description', 'image_of_product', 'categories']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'