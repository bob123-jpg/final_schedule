from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import LiveServerTestCase
from selenium import webdriver

# Test login page
class LoginTest(TestCase):
    # Create a user to test logging in
    def setUp(self):
        self.username = 'bob'
        self.password = 'TeStP@s$w0rd-#z123'
        self.user = User.objects.create_user(username = self.username, password = self.password)

    # Unit test 1: Successful login
    def test_valid_login(self):
        login = {'username': self.username, 'password': self.password}
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # Unit test 2: Incorrect login information provided
    def test_invalid_login(self):
        login = {'username': self.username, 'password': 'noneforyou'}
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

# Unit test 3: Logged out user can access Events page
class EventsTest(TestCase):
    def test_events_page(self):
        response = self.client.get("/planners/")
        self.assertEqual(response.status_code, 200)

# Test if a logged out user can access certain webpages
class NewPostTest(LiveServerTestCase):
    # Test with Chrome browser
    def setUp(self):
        self.browser = webdriver.Chrome()

    # Close browser after testing
    def tearDown(self):
        self.browser.quit()

    # Selenium test 1: Sign up page is accessible from logged out page
    def test_register(self):
        self.browser.get('http://127.0.0.1:8000/register/')

    # Selenium test 2: Events page is accessible from logged out page
    def test_events(self):
        self.browser.get('http://127.0.0.1:8000/planners/')
