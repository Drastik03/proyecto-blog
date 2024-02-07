from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from posts.views import (
    PostCreate,
    PostListView, 
    PostDetailView, 
    PostUpdate,
    PostDelete,
    like
    )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',PostListView.as_view(),name='post_list'),
    path('create/',PostCreate.as_view(),name='post_create'),
    path('<slug>/',PostDetailView.as_view(),name='detail_post'),
    path('<slug>/update/',PostUpdate.as_view(),name='post_update'),
    path('<slug>/delete/',PostDelete.as_view(),name='post_delete'),
    path('like/<slug>/',like,name='like')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_ROOT, document_root=settings.MEDIA_ROOT)
    
