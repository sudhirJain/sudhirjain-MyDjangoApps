from django.conf.urls import url, include
from django.urls import re_path 
from django.contrib import admin
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^$',include('posts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include ('posts.urls')),
    url(r'^register',user_views.register,name="register"),
    url(r'^profile',user_views.profile,name="profile"),
    url(r'^login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    re_path(r'^password-reset/',
                auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
                name="password_reset"),
    re_path(r'^password-reset/done/',
                auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
                name="password_reset_done"),
    re_path(r'^password-reset-confirm/<uidb64>/<token>/',
                auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
                name="password_reset_confirm"),
    # url(r'^blog/', include ('blog.urls')),
    re_path(r'^blog/', include ('blog.urls')),
    re_path(r'^weather/', include ('weather.urls')),
    re_path(r'^todo_list/', include ('todo_list.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
