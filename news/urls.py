from django.urls import path

from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, AddCategory,ContactView, ReplyCommentView, ReplyView, CategoryView, CategoryListView, LikeView

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	# path("article/<int:pk>", ArticleView.as_view(), name="article_detail"),
	path("article/<int:pk>", ArticleView, name="article_detail"),
	path("addpost", AddPostView.as_view(), name="add_post"),
	path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update_post"),
	path("article/delete/<int:pk>", DeletePostView.as_view(), name="delete_post"),
	path("addcategory", AddCategory.as_view(), name="add_category"),
	# path("news/<str:name>", views.page, name="page"),
	path('category/<str:cats>', CategoryView, name='category'),
	path('categorylist', CategoryListView, name='category_list'),
	path('likes/<int:pk>', LikeView, name="like_post"),
	path('comment<int:pk>', ReplyView, name="reply"),
	path('reply_comment/<int:pk>', ReplyCommentView, name="reply_comment"),
	path('contact/', ContactView, name="contact"),
	# path('comments', comments, name="comments")


]
