from django.urls import path
from .views import IndexView
from adopt_animals import views
from accounts import views
from adopt_animals.views import (CreatePostView, PostDoneView, PostDetailView, PostUpdateView, 
                                    PostDeleteView, MyPostListView, MyFavoritePostListView, MessageRoomView, MessageRoomListView,
                                    ContactFormView, ContactResultView, AboutView)
from . import views


app_name = 'adopt_animals'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('post/new/', CreatePostView.as_view(), name='post_new'), 
    path('post/done/', PostDoneView.as_view(), name='post_done'),

    path('post_detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'), 

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('my_post_list/', MyPostListView.as_view(), name='my_post_list'),

    path('like', views.LikeView, name='like'),

    path('my_fav_post_list/', MyFavoritePostListView.as_view(), name='my_fav_post_list'),

    path('message_room/<int:pk>/', MessageRoomView.as_view(), name='message_room'),

    path('message_room_list/', MessageRoomListView.as_view(), name='my_messages'),

    path('contact/', ContactFormView.as_view(), name='contact_form'),
    path('contact/result/', ContactResultView.as_view(), name='contact_result'),

    path('about/', AboutView.as_view(), name='about'),
]

