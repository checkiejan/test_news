from django.urls import path
from stories.views import *

app_name = 'stories'
urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('single/', single, name='single'),
    path('contact/', contact, name='contact'),
]