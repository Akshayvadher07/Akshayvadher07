# simple_api/urls.py
from django.urls import path
from .views import ItemListCreateView, ItemRetrieveView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<uuid:pk>/', ItemRetrieveView.as_view(), name='item-retrieve'),
    path('items/<uuid:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<uuid:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]



