from app.tag.models import Tag
from app.tag.serializer import TagSerializer
from common.base_api_view import BaseView


class TagView(BaseView):
    model = Tag
    serializer_model = TagSerializer
