from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductRetriveUpdateDeleteAPIView
)

urlpatterns = [
    path('',ProductListCreateAPIView.as_view(),name="products"),
    path('<int:pk>/',ProductRetriveUpdateDeleteAPIView.as_view()),
]

for i in urlpatterns:
    print(i)