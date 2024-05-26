from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register(r'levels', views.UserDeviceGlucoseDataView)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('upload-csv/', views.CSVUploadView.as_view(), name='upload-csv'),
    path('export-data/', views.ExportDataView.as_view(), name='export-data'),
]
