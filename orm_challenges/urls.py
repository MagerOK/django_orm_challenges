from django.urls import path

from challenges.views.level_1.a_create_book import create_book_handler
from challenges.views.level_1.b_book_details import book_details_handler
from challenges.views.level_1.c_delete_book import delete_book_handler
from challenges.views.level_1.d_update_book import update_book_handler
from challenges.views.level_2.a_laptops import laptop_details_view, laptop_in_stock_list_view, laptop_filter_view, \
    last_laptop_details_view
from challenges.views.level_2.b_blog import last_posts_list_view, posts_search_view, untagged_posts_list_view, \
    categories_posts_list_view, last_days_posts_list_view

urlpatterns = [
    # level 1
    path('book/create/', create_book_handler),
    path('book/<int:book_id>/', book_details_handler),
    path('book/<int:book_id>/delete/', delete_book_handler),
    path('book/<int:book_id>/update/', update_book_handler),

    # level 2
    path('laptops/<int:laptop_id>/', laptop_details_view),
    path('laptops/in-stock/', laptop_in_stock_list_view),
    path('laptops/', laptop_filter_view),
    path('laptops/last/', last_laptop_details_view),
    path('posts/latest/', last_posts_list_view),
    path('posts/search/', posts_search_view),
    path('posts/untagged/', untagged_posts_list_view),
    path('posts/by-categories/', categories_posts_list_view),
    path('posts/last-published/', last_days_posts_list_view),
]
