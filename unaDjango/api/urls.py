from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register(r'levels', views.UserDeviceGlucoseDataView)

urlpatterns = [
    path('v1/', include(router.urls)),
]
