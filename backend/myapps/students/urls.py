from django.urls import path
from . import views
from rest_framework import routers

app_name = 'students'

router = routers.DefaultRouter()
router.register('students', views.StudentsViewSet)

urlpatterns = router.urls
