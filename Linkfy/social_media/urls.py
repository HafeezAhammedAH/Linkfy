from django.urls import path
from social_media import views


urlpatterns=[
     path("register",views.SignUpView.as_view(),name="registered")
]
   