from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta, date

import markdown
from django.utils.safestring import mark_safe
from markdownx.models import MarkdownxField

# Create your models here.
class User(AbstractUser):
    pass
   

class Profile(models.Model):
    #about = models.TextField(blank=True, null=True)
    about = MarkdownxField()  # Markdown content field
    #joined_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, upload_to='images/')
    resume = models.FileField(upload_to='pdfs/')
    github = models.URLField()
    linkedln = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return f"{self.about}"
    
    def get_about(self): #def get about as markdown
      return mark_safe(markdown.markdown(self.about))


class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post, limited to 200 characters.
    photo = models.ImageField(blank=True, null=True, upload_to='images/')  # Optional image for the post, uploaded to the 'images/' folder.
    #content = models.TextField()  # Main content of the blog post, using a TextField for long text.
    content = MarkdownxField()  # Markdown content field
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the post is created, automatically set.

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
         return f"Title: {self.title}\nCreated At: {self.created_at}\ncontent: {self.content}\n"
    
    """def get_content_as_markdown(self):
        # Convert content from Markdown to HTML
        return mark_safe(markdown.markdown(self.content))
    """
    def get_content(self): #get content as markdown
        return mark_safe(markdown.markdown(self.content))
        

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.name}n\email: {self.email}\nSubmitted At: {self.submitted_at}\nMessage: {self.message}\n"

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    #discription = models.TextField()
    discription = MarkdownxField()
    photo = models.ImageField(blank=True, null=True, upload_to='images/')
    website = models.URLField()
    github = models.URLField()

    def get_discription(self): #get discription as markdown
        return mark_safe(markdown.markdown(self.discription))
    
    def __str__(self):
        return f"Title: {self.title}n\Discription: {self.discription}\nPhoto: {self.photo}\n"

class Service(models.Model):
    title = models.CharField(max_length=200)  
    photo = models.ImageField(blank=True, null=True, upload_to='images/')
    content = MarkdownxField()  

    def get_content(self): #get content as markdown
        return mark_safe(markdown.markdown(self.content))

    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}\n"


class Badge(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Badge name: {self.name} Url: {self.url} and created on {self.created_at}\n"
