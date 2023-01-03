
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/v1/', include('mainapp.urls', namespace='products')),
    # path('api/v1/product-list/', ProductViewSet.as_view({'get': 'list'})),
    # path('api/v1/product-list/<int:pk>/',
    #      ProductViewSet.as_view({'put': 'update'})),
]
