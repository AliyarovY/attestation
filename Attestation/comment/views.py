from base.views import CommentPostViewMixin
from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(CommentPostViewMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

