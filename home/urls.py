from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    path('about-us', views.AboutView.as_view(),name="about_us"),
    path('terms-of-use', views.TermsUseView.as_view(),name="terms_of_use"),
    path('privacyp-policy', views.PrivacypPolicyView.as_view(),name="privacyp_policy"),
    path('career', views.CareerView.as_view(),name="career"),
    path('send-mail', views.SendMailVIew,name="send_mail"),
]