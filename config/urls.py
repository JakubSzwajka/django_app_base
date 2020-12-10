from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from register import views as register_views

urlpatterns = [
    path('', include('main_app.urls')), 
    path('', include('register.urls')),
    path('admin/', admin.site.urls),
    path('register/', register_views.register, name="register" ),
    path('', include('django.contrib.auth.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

