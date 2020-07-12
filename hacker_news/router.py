from api.viewsets import PostViewset, CommentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register("post", PostViewset)
router.register("comment", CommentViewset)
