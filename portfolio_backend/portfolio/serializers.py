from rest_framework import serializers
from .models import Profile, BlogPost, Contact, Portfolio, Service, User, Badge
from django.utils.safestring import mark_safe
import markdown

class UserSerializer(serializers.ModelSerializer):
    
    date_joined = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y")
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    #about = serializers.SerializerMethodField()  # Handle markdown rendering
    about = serializers.CharField()
    photo = serializers.ImageField()
    resume = serializers.FileField()

    class Meta:
        model = Profile
        fields = ['id', 'about', 'photo', 'resume', 'github', 'linkedln', 'twitter']

    def get_about(self, obj):
        # Convert markdown to HTML using the get_about method
        return mark_safe(markdown.markdown(obj.about))

"""
class BlogPostSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()  # Handle markdown rendering
    created_at = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y", read_only=True)  # Custom date formatting

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'photo', 'content', 'created_at']

    def get_content(self, obj):
        # Convert markdown to HTML using the get_content method
        return obj.get_content()
"""
class BlogPostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y", read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'photo', 'content', 'created_at']


class ContactSerializer(serializers.ModelSerializer):
    submitted_at = serializers.DateTimeField(format="%I:%M %p, %a %d %B %Y")  # Custom date formatting

    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message', 'submitted_at']


class PortfolioSerializer(serializers.ModelSerializer):
    #discription = serializers.SerializerMethodField()  # Handle markdown rendering
    photo = serializers.ImageField()

    class Meta:
        model = Portfolio
        fields = ['id', 'title', 'discription', 'photo', 'website', 'github']

    def get_discription(self, obj):
        # Convert markdown to HTML using the get_discription method
        return obj.get_discription()


class ServiceSerializer(serializers.ModelSerializer):
    #content = serializers.SerializerMethodField()  # Handle markdown rendering
    photo = serializers.ImageField()

    class Meta:
        model = Service
        fields = ['id', 'title', 'photo', 'content']

    def get_content(self, obj):
        # Convert markdown to HTML using the get_content method
        return obj.get_content()

class BadgeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Badge
        fields = ['id', 'name', 'image', 'url', 'created_at']
