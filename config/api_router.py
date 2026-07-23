from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from studious_octo_goggles.incidents.views import IncidentReportViewSet
from studious_octo_goggles.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("incidents", IncidentReportViewSet)


app_name = "api"
urlpatterns = router.urls
