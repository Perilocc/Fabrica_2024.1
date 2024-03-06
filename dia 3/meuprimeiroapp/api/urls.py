from rest_framework.routers import DefaultRouter # ver os routers no django rest
from .viewsets import PessoaViewSet
from django.urls import include, path

router = DefaultRouter()

router.register(prefix="pessoa" , viewset = PessoaViewSet)

urlpatterns = [
    path("api/", include(router.urls))
]
