from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static


# variavel urlspatterns é uma lista com as paths
# chama a funcão da views que recebe uma request e retorna uma response

urlpatterns = [
    path('', views.home_view, name='home'),

    path('genre/', views.genre_list_view, name='genre_list'),
    path('genre/create/', views.genre_create_view, name='genre_create'),
    path('genre/<int:id>/', views.genre_detail_view, name='genre_detail'),
    path('genre/<int:id>/update/', views.genre_update_view, name='genre_update'),
    path('genre/<int:id>/delete/', views.genre_delete_view, name='genre_delete'),
    #path('genre/counter/', views.genre_counter_view, name='genre_counter'),

    path('author/', views.author_list_view, name='author_list'),
    path('author/create/', views.author_create_view, name='author_create'),
    path('author/<int:id>/', views.author_detail_view, name='author_detail'),
    path('author/<int:id>/update/', views.author_update_view, name='author_update'),
    path('author/<int:id>/delete/', views.author_delete_view, name='author_delete'),

    path('publisher/', views.publisher_list_view, name='publisher_list'),
    path('publisher/create/', views.publisher_create_view, name='publisher_create'),
    path('publisher/<int:id>/', views.publisher_detail_view, name='publisher_detail'),
    path('publisher/<int:id>/update/', views.publisher_update_view, name='publisher_update'),
    path('publisher/<int:id>/delete/', views.publisher_delete_view, name='publisher_delete'),

    path('book/', views.book_list_view, name='book_list'),
    path('book/create/', views.book_create_view, name='book_create'),
    path('book/<int:id>/', views.book_detail_view, name='book_detail'),
    path('book/<int:id>/update/', views.book_update_view, name='book_update'),
    path('book/<int:id>/delete/', views.book_delete_view, name='book_delete'),
    path('book/<int:id>/image/', views.book_image_upload_view, name='book_image')

    #path('user/', views.user_list_view, name='user_list'),
    #path('user/create/', views.user_create_view, name='user_create'),
    #path('user/<int:id>/', views.user_detail_view, name='user_detail'),
    #path('user/login/', views.user_login_view, name='user_detail' ),
    #path('user/logout/', views.user_logout_view, name='user_logout'),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

