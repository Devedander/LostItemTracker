from django.test import TestCase
import pytest
import requests
import json
# Create your tests here.
@pytest.mark.django_db
data = {
        "title": "Introduction to Django",
        "tutorial_url": "https://www.djangoproject.com",
        "image_path": "../static/images/tutorials/introDjango.png",
        "description": "A tutorial about Django",
        "published": true 
       }
response = requests.post("/AddMessage", json=json.dumps(data))
json_response = response.json()
print(json_response)