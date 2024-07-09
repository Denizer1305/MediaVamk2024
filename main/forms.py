from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, News, ContactMessage, NewsCategory

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'image', 'summary', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'summary': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'content': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'category': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
        }


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите ваш логин'}))
    first_name = forms.CharField(label='Имя', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите ваше имя'}))
    last_name = forms.CharField(label='Фамилия', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите вашу фамилию'}))
    activity = forms.ChoiceField(label='Деятельность', choices=UserProfile.activity_choices, required=True, widget=forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите ваш email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'activity', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['username'].widget.attrs.update({'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите имя пользователя'})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'first_name', 'last_name', 'phone', 'course', 'specialty', 'group', 'address', 'activity']
        widgets = {
            'avatar': forms.FileInput( attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите вашу фамилию'}),
            'phone': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите ваш телефон'}),
            'course': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите ваш курс'}),
            'specialty': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите вашу специальность'}),
            'group': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите вашу группу'}),
            'address': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Введите ваш адрес'}),
            'activity': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'image', 'summary', 'content', 'category']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class NewsFilterForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=NewsCategory.objects.all(),
        required=False,
        label='Категория',
        widget=forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded'})
    )
    search = forms.CharField(
        required=False,
        label='Поиск',
        widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'placeholder': 'Поиск по заголовку, описанию...'})
    )