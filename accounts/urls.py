from django.urls import path
from django.utils.translation import templatize
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'


urlpatterns = [
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('password/change/',auth_views.PasswordChangeView.as_view(template_name='change_password.html'),name='password_change'),
    path('password/change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),name='password_change_done'),
    path('signup/', views.signup, name='signup'),
    path('password/reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html', 
        email_template_name='password_reset_email.html', 
        subject_template_name='password_reset_subject.txt',
        success_url='/password/reset/done/'), name='password_reset_form'),
    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html', 
        success_url='/password/reset/complete/'), name='password_reset_confirm'),
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('profile/<slug:slug>', views.profile, name='profile'),
    path('re_send/', views.re_send, name = 're_send'),
    path('edit/profile', views.profile_edit, name='edit_profile'),

]