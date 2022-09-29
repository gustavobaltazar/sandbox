from . import views
from rest_framework_nested import routers   

router = routers.DefaultRouter()
router.register('usuarios', views.UsuarioViewSet, basename='usuarios')

urlpatterns = router.urls