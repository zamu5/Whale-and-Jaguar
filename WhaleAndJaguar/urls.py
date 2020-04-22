from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView, logout_then_login
from django.conf import settings
from django.conf.urls.static import static
from .views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('user/', include('apps.user.urls')),
    path('analysis/', include('apps.analysis.urls')),
    path('accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('reset/password_reset', PasswordResetView.as_view(template_name='Registration/password_reset_form.html',
                                                           email_template_name='Registration/password_reset_email.html'),
         name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='Registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name= 'Registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done', PasswordResetCompleteView.as_view(template_name='Registration/password_reset_complete.html'), name='password_reset_complete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
