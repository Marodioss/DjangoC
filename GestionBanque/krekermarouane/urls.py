from django.urls import path
from . import views

urlpatterns = [
     path('comptes/', views.compte_list),
     path('clients/', views.client_list),
     path('comptes/details/<int:code>', views.details),
     path('comptes/details/detailsop/<int:code>', views.detailop),
     path('forms/' , views.Clientform),
]
