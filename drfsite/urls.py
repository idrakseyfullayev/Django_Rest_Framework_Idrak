"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path # 12
# from men.views import MenAPIView
from men.views import *
from rest_framework import routers


# 9 
# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list', 'post': 'create'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         routers.Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         )
#     ]    


# router = MyCustomRouter() # 9
# router.register(r'men', MenViewSet, basename='men') # 9
# print(router.urls) # 9

# router = routers.SimpleRouter() # 8
# router.register(r'men', MenViewSet) # 8
# router = routers.DefaultRouter() # 9
# router.register(r'men', MenViewSet, basename='men') # 9
# print(router.urls) # 9


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.views import TokenBlacklistView

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
token = RefreshToken()
token.blacklist()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/menlist/', MenAPIView.as_view()), # 6, # 5, # 4, # 2, # 1
    # path('api/v1/menlist/<int:pk>/', MenAPIView.as_view()), # 6, # 5
    # path('api/v1/menlist/', MenAPIList.as_view()), # 7
    # path('api/v1/menlist/<int:pk>/', MenAPIUpdate.as_view()), # 7
    # path('api/v1/mendetail/<int:pk>/', MenAPIDetailView.as_view()), # 7
    # path('api/v1/menlist/', MenViewSet.as_view({'get': 'list', 'post': 'create'})), # 8
    # path('api/v1/menlist/<int:pk>/', MenViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})), # 8
    # path('api/v1/', include(router.urls)) # 8 # 9
    path('api/v1/drf-auth/', include('rest_framework.urls')), # 11
    path('api/v1/men/', MenAPIList.as_view()), # 10
    path('api/v1/men/<int:pk>/', MenAPIUpdate.as_view()), # 10
    path('api/v1/mendelete/<int:pk>/', MenAPIDestroy.as_view()), # 10
    path('api/auth/', include('djoser.urls')), # 12
    re_path(r'auth/', include('djoser.urls.authtoken')), # 12
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #14
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 14
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'), # 14
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'), # 14
    
]


    