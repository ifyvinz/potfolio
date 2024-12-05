from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Profile, BlogPost, Portfolio, Service, Badge


class TestUserAuthentication(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
    
    def test_login_valid_user(self):
        # Test valid login
        response = self.client.post('/api/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logout(self):
        # Test logout
        response = self.client.post('/api/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            about="This is a test about me",
            github="https://github.com/testuser",
            linkedln="https://linkedin.com/in/testuser",
            twitter="https://twitter.com/testuser"
        )
    
    def test_profile_creation(self):
        # Test profile creation
        self.assertEqual(self.profile.about, "This is a test about me")
    
    def test_profile_detail(self):
        # Test profile detail retrieval
        response = self.client.get(f'/api/profile/{self.profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'about')


class BlogPostTestCase(TestCase):
    def setUp(self):
        self.blog_post = BlogPost.objects.create(
            title="Test Blog Post",
            content="This is a test content.",
            created_at="2024-12-05T00:00:00Z"
        )
    
    def test_blogpost_creation(self):
        # Test blog post creation
        self.assertEqual(self.blog_post.title, "Test Blog Post")
    
    def test_blogpost_list(self):
        # Test blog post listing
        response = self.client.get('/api/blogposts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Blog Post')


class PortfolioTestCase(TestCase):
    def setUp(self):
        self.portfolio = Portfolio.objects.create(
            title="Test Portfolio",
            discription="This is a test description",
            website="https://testportfolio.com",
            github="https://github.com/testportfolio"
        )
    
    def test_portfolio_creation(self):
        # Test portfolio creation
        self.assertEqual(self.portfolio.title, "Test Portfolio")
    
    def test_portfolio_list(self):
        # Test portfolio listing
        response = self.client.get('/api/portfolios/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Portfolio')


class ServiceTestCase(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            title="Test Service",
            content="This is a test service description"
        )
    
    def test_service_creation(self):
        # Test service creation
        self.assertEqual(self.service.title, "Test Service")
    
    def test_service_list(self):
        # Test service listing
        response = self.client.get('/api/services/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Service')


class BadgeTestCase(TestCase):
    def setUp(self):
        self.badge = Badge.objects.create(
            name="Test Badge",
            url="https://badge.com"
        )
    
    def test_badge_creation(self):
        # Test badge creation
        self.assertEqual(self.badge.name, "Test Badge")
    
    def test_badge_list(self):
        # Test badge listing
        response = self.client.get('/api/badges/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Test Badge')
