from django.urls import path
from . import views 

urlpatterns = [
 # This associates the index view with the root URL
    path('', views.product_list, name='product_list'),  # Example path for product_list view
    path('data/', views.data, name='data'),  # Example path for product_list view
    # Add more paths for other views if needed
]
