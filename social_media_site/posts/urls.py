from django.urls import path
from . import views

app_name="posts"

urlpatterns=[
    path('',views.PostList.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name='create'),
    path('by/<username>/',views.UserPosts.as_view(),name='for_user'),
    path('post/<username>/<pk>/',views.PostDetail.as_view(),name='single'),
    path('delete/<pk>/',views.DeletePost.as_view(),name='delete'),
    path('post/<pk>/',views.add_comment_to_post,name='add_comment_post'),
    path('comment/<pk>/remove/',views.remove_comment,name='remove_comment'),
    path('group_post/<pk>/',views.add_post_from_group,name='group_posts')
]
