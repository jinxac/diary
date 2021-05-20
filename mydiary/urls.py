from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mydiary import views

urlpatterns = [
    path('content/', views.ContentList.as_view()),
    path('content/<int:pk>/', views.ContentDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)