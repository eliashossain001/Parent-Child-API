from . import views
from django.urls import path
from .views import ParentList, ParentDetail, ChildList, ChildDetail

urlpatterns = [
    path('parents/', ParentList.as_view(), name='parent-list'),
    path('parents/<int:pk>/', ParentDetail.as_view(), name='parent-detail'),
    path('children/', ChildList.as_view(), name='child-list'),  # Add this line
    path('children/<int:pk>/', ChildDetail.as_view(), name='child-detail'),
]
