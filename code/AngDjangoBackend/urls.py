from os import name
from django.conf.urls import url
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    url(r'^api/tutorials$',views.tutorial_list ),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published),
    url(r'api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
