"""jts_website URL Configuration
"""

from django.contrib import admin
from django.urls import include, path
from index import views as home_view
from about import views as about_view
from contact import views as contact_view


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Simple routes
urlpatterns += [
    path('', home_view.index, name='index'),
    path('contact/', contact_view.jts_contact, name='contact'),
    path('about/', about_view.jts_about, name='about')
]