""" URLConf """


from django.urls import path

from users.views import UserCreateView, UserDetailView, UserListView, UserUpdateView, UserDeleteView


# Create your patterns here.
urlpatterns = [
    path(
        '',
        UserListView.as_view(),
        name='user_list'
    ),
    path(
        'register/',
        UserCreateView.as_view(),
        name='create_user'
    ),
    path(
        '<int:id>/',
        UserDetailView.as_view(),
        name='user_detail'
    ),
    path(
        '<int:id>/update/',
        UserUpdateView.as_view(),
        name='update_user'
    ),
    path(
        '<int:id>/delete/',
        UserDeleteView.as_view(),
        name='delete_user'
    ),
]
