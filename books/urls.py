from django.urls import path

from .views import BookPageView, BookDetailView

urlpatterns = [
    path('', BookPageView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name="book_details")
]
