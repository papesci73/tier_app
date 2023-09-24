from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shorter_api import views

router = DefaultRouter()
router.register('short', views.ShorterApiView)
router.register('tier.app', views.ShorterApiPublicView)
urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]