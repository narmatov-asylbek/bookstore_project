from django.urls import path

from .views import BookPageView, BookDetailView, SearchListView

urlpatterns = [
    path('', BookPageView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name="book_details"),
    path('search/', SearchListView.as_view(), name='search_results')
]
