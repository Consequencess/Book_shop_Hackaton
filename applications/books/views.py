from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status, mixins

from applications.books.models import Books, Like, Category, Comment
from applications.books.permissions import IsOwner
from applications.books.serializer import BookSerializer, CategorySerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BookAPIView(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwner]
    pagination_class = LargeResultsSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'owner']
    search_fields = ['title', 'description']
    ordering_fields = ['id']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # @action(detail=True, methods=['POST'])
    # def like(self, request, pk, *args, **kwargs): # post/id/like/
    #     like_obj, _= Like.objects.get_or_create(post_id=pk, owner=request.user)
    #     like_obj.like = not like_obj.like
    #     like_obj.save()
    #     status = 'liked'
    #     if not like_obj.like:
    #         status = 'unliked'
    #     return Response({'status': status})

    # @action(detail=True, methods=['POST'])
    # def rating(self, request, pk, *args, **kwargs):
    #     serializer = RatingSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     rating, _ = Rating.objects.get_or_create(post_id=pk, owner=request.user)
    #     rating.rating = request.data['rating']
    #     rating.save()
    #     return Response(request.data, status=status.HTTP_201_CREATED)


class CategoryAPIView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]






