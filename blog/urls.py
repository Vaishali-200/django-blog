from django.conf.urls import url
from .views import (BlogListView,
                    SelfBlogListView,
                    CreateBlogAPIView,
                    UpdateBlogStatusAPIView
                    )

urlpatterns = [
    url('createBlog', CreateBlogAPIView.as_view()),
    url('getBlogList',BlogListView.as_view()),
    url('getSelfBlogList',SelfBlogListView.as_view()),
    url('updateBlog/(?P<pk>.+)',UpdateBlogStatusAPIView.as_view())
]
