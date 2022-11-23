from django.urls import path
from . import views

urlpatterns = [
    path("accounts/<int:account_id>/", views.AccountView.as_view()),
]
