from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("david", views.david, name="david"),
    # Saying hello to any name as string
    path("<str:name>", views.greet, name="greet")
]
    