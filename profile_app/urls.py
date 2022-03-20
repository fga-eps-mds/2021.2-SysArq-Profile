from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from profile_app import views

urlpatterns = [
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path('users/get-users/', views.GetUsersViewSet.as_view({'get': 'list'})),
    path('users/register/', views.CreateUserViewSet.as_view({'post': 'create'}))
]

urlpatterns = format_suffix_patterns(urlpatterns)
