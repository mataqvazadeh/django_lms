from rest_framework.routers import DefaultRouter

from teacher_management.views import TeacherViewSet

router = DefaultRouter()
router.register('teacher', TeacherViewSet)

urlpatterns = router.urls