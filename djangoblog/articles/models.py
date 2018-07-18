from django.db import models

# Create your models here. Database
# python manage.py makemigrations
# python manage.py migrate

max_snippet_length = 50

class Article(models.Model): # DB Table name
  title = models.CharField(max_length=101)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True) # automatically without user input


  def __str__(self): # makes getting self print its own title instead
    return self.title

  def snippet(self): # show only first XX letters of body
    if len(self.body) <= max_snippet_length:
      return self.body
    else:
      return self.body[:50] + '...'
    