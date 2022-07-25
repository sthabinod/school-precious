
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('/login',views.login_user, name="login"),
    path('/register-entrance',views.register_entrance, name="register_entrance"),
    path('/my-leave',views.my_leave, name="my_leave"),
    path('/email-bus',views.send_mail_bus_user, name="email_bus"),
    path('/email-form',views.email_form, name="email_form"),
    path('/scholarship-register',views.scholarship, name="scholarship_register"),
    path('/apply-leave',views.apply_leave, name="apply_leave"),
    path('/edit/<int:id>',views.edit, name="edit"),
    path('/activate',views.activate,name="activate"),
    path('/logout',views.logout_user,name="logout"),
    path('/reset', auth_views.PasswordResetView.as_view(template_name="account/reset_password.html"), name="reset"),
    path('/reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(template_name="account/reset_password_sent.html"),
         name="password_reset_done"),
    path('/reset_password/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name="account/reset_password_enter_form.html"),
         name="password_reset_confirm"),
    path('/reset_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name="account/reset_password_done.html"),
         name="password_reset_complete"),

    path('/unauthorized',views.unauthorized, name="unauthorized"),
     path('/chat',views.chat, name="chat"),
     

]
