from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('gmopi.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')),
    path('estoque/', include('estoque.urls')),

]
