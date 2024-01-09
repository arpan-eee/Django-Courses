from django.urls import path,include
from . import views

urlpatterns = [
    path('buy/<int:id>', views.buy,name="buy"),
    # path('user/', include('user.urls')),
    # path('brand/', include('brand.urls')),
    # path('car/', include('car.urls')),
]