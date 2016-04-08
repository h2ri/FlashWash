from django.conf.urls import patterns,url,include
from rest_framework import routers
from orders import views

router = routers.DefaultRouter()
router.register(r'orders',views.OrderViewSet,)


urlpatterns = patterns(
    '',
    url(r'^',include(router.urls)),
)