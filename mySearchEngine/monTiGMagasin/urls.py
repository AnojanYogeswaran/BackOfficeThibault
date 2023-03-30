from django.urls import path
from monTiGMagasin import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('putonsale/<int:tig_id>/<int:newprice>/', views.PutOnSale.as_view()),
    path('removesale/<int:tig_id>/',views.RemoveSale.as_view()),
    path('incrementStock/<int:tig_id>/<int:unites>/',views.IncrementStock.as_view()),
    path('decrementStock/<int:tig_id>/<int:unites>/',views.DecrementStock.as_view()),
    path('updateStock/<int:tig_id>/<int:quantity>/',views.updateStock.as_view()),
    
]