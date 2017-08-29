from django.conf.urls import url, include
from rajnikanth import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)