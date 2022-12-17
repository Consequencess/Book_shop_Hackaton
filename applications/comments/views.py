from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from applications.comments.models import Comment
from applications.comments.permissions import IsCommentOwner
from applications.comments.serializer import CommentSerializer


class CommentAPIView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
            queryset = super().get_queryset()
            queryset = queryset.filter(owner=self.request.user)
            return queryset