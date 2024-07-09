from django.db import models
from django.contrib.auth.models import User

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_images/')
    summary = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    activity_choices = [
        ('welder', 'Сварщик'),
        ('firefighter', 'Пожарный'),
        ('mechanic', 'Мастер по ремонту и обслуживанию автомобилей'),
        ('computer_systems', 'Компьютерные системы и комплексы'),
        ('information_systems', 'Информационные системы и программирование'),
        ('electrical_equipment', 'Эксплуатация и обслуживание электрического и электромеханического оборудования (по отраслям)'),
        ('engineering', 'Технология машиностроения'),
        ('maintenance', 'Техническое обслуживание и ремонт двигателей, систем и агрегатов автомобилей'),
        ('accounting', 'Экономика и бухгалтерский учет (по отраслям)'),
        ('law_enforcement', 'Правоохранительная деятельность'),
        ('jurisprudence', 'Юриспруденция'),
        ('design', 'Дизайн (по отраслям)')
    ]
    activity = models.CharField(max_length=50, choices=activity_choices)
    phone = models.CharField(max_length=20, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    specialty = models.CharField(max_length=200, null=True, blank=True)
    group = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Slider(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='slider_images/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else "Слайд без заголовка"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"