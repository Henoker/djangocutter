from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from django_cutter.users.api.views import UserViewSet
from django_cutter.fitness.views import SetviewSet, WorkoutviewSet, ExcerciseviewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("sets", SetviewSet)
router.register("workouts", WorkoutviewSet)
router.register("exercises",ExcerciseviewSet )


app_name = "api"
urlpatterns = router.urls
