from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostList, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, upgrade_me


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('upgrade/', upgrade_me, name = 'upgrade')
]
