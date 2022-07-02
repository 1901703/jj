from django.urls import path
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name='qna'

urlpatterns=[
    path('', qna, name='qna'),
    path('<int:pk>/', posting, name='posting'),
    path('new_post/', new_post, name='new_post'),
    path('remove/<int:pk>/', remove_post, name='remove_post'),
    path('update/<int:pk>/', update_post, name='update_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)