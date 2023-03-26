from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

from base.views import CommentPostViewMixin
from .serializers import PostSerializer
from .models import Post


class PostViewSet(CommentPostViewMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
