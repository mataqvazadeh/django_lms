from rest_framework.routers import DefaultRouter

from teacher_management.views import TeacherViewSet, ReportViewSet

router = DefaultRouter()
router.register('teacher', TeacherViewSet)
router.register('report', ReportViewSet)

urlpatterns = router.urls