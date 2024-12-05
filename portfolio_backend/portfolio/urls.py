from rest_framework.authtoken.views import obtain_auth_token
#need to be able to upload images
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from portfolio import views
from markdownx import urls as markdownx_urls

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('profile/', views.profile_detail, name='profile-detail'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('blogposts/', views.blogpost_list, name='blogpost-list'),
    path('blogposts/<int:pk>/', views.blogpost_detail, name='blogpost-detail'),
    path('contact/', views.contact_create, name='contact-create'),
    path('portfolio/', views.portfolio_list, name='portfolio-list'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio-detail'),
    path('services/', views.service_list, name='service-list'),
    path('services/<int:pk>/', views.service_detail, name='service-detail'),
    path('send-email/', views.send_contact_email, name='send-email'),
    path('markdownx/', include(markdownx_urls)),
    path('create_portfolio/', views.create_portfolio, name='create_portfolio'),
    path('delete_portfolio/<int:pk>/', views.delete_portfolio, name='delete_portfolio'),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('delete_blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('create_service/', views.create_service, name='create_service'),
    path('badges/', views.badges, name='badges'),
    path('create_badge/', views.create_badge, name='create_badge'),
    path('delete_badge/<int:id>/', views.delete_badge, name='delete_badge'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)