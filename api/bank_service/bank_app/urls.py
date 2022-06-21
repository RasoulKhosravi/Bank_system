from django.urls import include, path

from rest_framework import routers

from bank_app.views import AccountViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet)
router.register(r'account', AccountViewSet)

urlpatterns = [
   path('', include(router.urls)),
]