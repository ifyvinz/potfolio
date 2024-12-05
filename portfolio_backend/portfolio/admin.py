from django.contrib import admin
from .models import Profile, BlogPost, Contact, Portfolio, Service, User, Badge

# Register your models here.


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(BlogPost)
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(Service)
admin.site.register(Badge)

