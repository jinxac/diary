from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogList, BlogDetail

urlpatterns = [
    path('blog/', BlogList.as_view()),
    path('blog/<int:pk>/', BlogDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)