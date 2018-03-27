from django.conf.urls import url
from my_blog.views import IndexView

urlpatterns = [
    url(r'^', IndexView.as_view(), name='index'),
]