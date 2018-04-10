from django.shortcuts import render, reverse
from django.views.generic import View
from my_blog.models import Post
from django.http import HttpResponse
import markdown


# Create your views here.
class IndexView(View):
    """首页"""

    def get(self, request):
        post_list = Post.objects.all()
        content = {
            'post_list': post_list,
        }
        return render(request, 'my_blog/index.html', content)


class DetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        content = {
            'post': post,
        }
        return render(request, 'my_blog/detail.html', content)
