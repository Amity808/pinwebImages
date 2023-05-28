from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    # # path('login/', views.user_login, name='login'),
    # path('login/', auth_view.LoginView.as_view(), name='login'),
    # path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    # # templates/registration/ password_change_form.html.
    # path('password-change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    # # # templates/registration/ password_change_done.html. dir for templates
    # path('password-change/done/', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # # use reset password
    # path('password-reset/', auth_view.PasswordResetView.as_view(), name='password_reset'),
    # # password resent done
    # path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # # password reset confirm
    # path('password-reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_view.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls'), name='dashboard'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
