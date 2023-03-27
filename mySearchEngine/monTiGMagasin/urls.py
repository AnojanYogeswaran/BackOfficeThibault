from django.urls import path
from monTiGMagasin import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:id>/', views.InfoProductDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('putonsale/<int:id>/<int:newprice>/', views.PutOnSale.as_view()),
    path('removesale/<int:id>/',views.RemoveSale.as_view()),
    path('incrementStock/<int:id>/<int:unites>/',views.IncrementStock.as_view()),
    path('decrementStock/<int:id>/<int:unites>/',views.DecrementStock.as_view()),
    
]