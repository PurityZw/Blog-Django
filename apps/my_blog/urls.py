from django.conf.urls import url
from my_blog.views import IndexView, DetailView

urlpatterns = [
    # 首页
    url(r'^index$', IndexView.as_view(), name='index'),
    # 文章详情页
    url(r'^post/(?P<pk>\d+)$', DetailView.as_view(), name='detail'),
]