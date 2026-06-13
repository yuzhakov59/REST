from rest_framework.routers import SimpleRouter
from django.urls import path

from materials.apps import CoursConfig
from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView

app_name = CoursConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/<int:pk>/destroy/', LessonDestroyAPIView.as_view(), name='lesson-destroy'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update')
]

urlpatterns += router.urls
