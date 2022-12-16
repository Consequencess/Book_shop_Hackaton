from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.books.views import BookAPIView

router = DefaultRouter()
router.register('', BookAPIView)

urlpatterns = [
    # path('', PostAPIView.as_view({'get': 'list', 'post': 'create'})),
    # path('', include(router.urls)
]
urlpatterns += router.urls