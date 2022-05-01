from rest_framework.routers import DefaultRouter
from .api import CreditOffersViewSet


router = DefaultRouter()
router.register("offer", CreditOffersViewSet, "offers")

urlpatterns = router.urls
