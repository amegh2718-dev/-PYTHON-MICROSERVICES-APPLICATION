from django.urls import path
from .views import GenerateAPIKeyView, UserRegistrationView, UserLoginView,LogRegistrationView, LogLoginView, LogGenerateAPIKeyView, PublicActivityLogListView


urlpatterns = [
    path('', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('generate-api-key/', GenerateAPIKeyView.as_view(), name='generate-api-key'),
     path('log-registration/', LogRegistrationView.as_view(), name='log-registration'),
    path('log-login/', LogLoginView.as_view(), name='log-login'),
    path('log-generate-api-key/', LogGenerateAPIKeyView.as_view(), name='log-generate-api-key'),
    path('public-logs/', PublicActivityLogListView.as_view(), name='public-logs'),
]
