from django.urls import path
from . import views

urlpatterns=[

    path('',views.login_as,name="login_as"),
    path('',views.login,name="login")
]