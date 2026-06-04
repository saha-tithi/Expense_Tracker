from Tracker.views import index,delete_transaction
from django.urls import path

urlpatterns = [
    path('', index),
     path('delete/<uuid:uuid>/',delete_transaction ,name='delete_transaction'),
]
