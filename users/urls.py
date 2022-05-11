from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, RegisterView
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/', views.MyObtainTokenPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    # path('follow/', views.FollowView.as_view(), name='follow'),
    # path('unfollow/', views.UnfollowView.as_view(), name='unfollow'),
]
