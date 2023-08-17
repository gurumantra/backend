from django.urls import path,include
from rest_framework import routers
from katha.views import KathaViewSet
from poojabidhi.views import PoojaBidhiViewSet
from mantra.views import MantraViewSet
from chadparba.views import ChadParbaViewSet
router = routers.DefaultRouter()
router.register('katha',KathaViewSet)
router.register('poojabidhi',PoojaBidhiViewSet)
router.register('mantra',MantraViewSet)
router.register('chadparba',ChadParbaViewSet)
urlpatterns = [
    path('', include(router.urls)),

]