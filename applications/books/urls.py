from rest_framework.routers import DefaultRouter
from .views import BookAPIView

router = DefaultRouter()
router.register('', BookAPIView)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls