from django.urls import include, path

from rest_framework import routers

from bank_app.views import TransactionViewSet

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet)

urlpatterns = [
   path('', include(router.urls)),
]