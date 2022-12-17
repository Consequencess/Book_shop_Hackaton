from rest_framework.routers import DefaultRouter
from .views import BookAPIView, CategoryAPIView
from ..comments.views import CommentAPIView

router = DefaultRouter()
router = DefaultRouter()
router.register('category', CategoryAPIView)
router.register('comment', CommentAPIView)
router.register('', BookAPIView)
# URLs настраиваются автоматически роутером
urlpatterns = router.urls