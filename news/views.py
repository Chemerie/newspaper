from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment, Reply
from .forms import PostForm, UpdatePostForm, CategoryForm
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from . import util
from django.conf import settings

# def page(request, name):
# 	if request.method == "GET":
# 		entries = util.list_entries()

# 		# if name not in entries:
# 		# 	return render(request, "encyclopedia/error.html", {
# 		# 	"error_msg": "The page you are looking for does not exist.",
# 		# 	"form": NewTaskForm(),
# 		# })

# 		return render(request,"news/index.html",{
# 		"content": markdown2.markdown(util.get_entry(name)),
# 		"name": name,
		
			
# 		})


# def index(request):
# 	return render(request,"news/index.html")
# # Create your views here.


def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False

	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True


	return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))
	


def ReplyView(request, pk):
	# comment = get_object_or_404(Comment, id=request.POST.get('post_id'))
	comment = Comment.objects.get(id=pk)
	replies = Reply.objects.filter(comment=comment).order_by('-id')
	return render( request,'reply.html', {
		"comment": comment,
		"replies": replies,
		} )
	
def ReplyCommentView(request, pk):
	if request.method == "POST":
		comment = Comment.objects.get(id=pk)
		user = request.user
		body = request.POST["comment"]
		f = Reply(user= user, comment=comment, body=body)
		f.save()

	return HttpResponseRedirect(reverse('reply', args=[str(pk)]))

class HomeView(ListView):
 	model = Post
 	template_name= 'home.html'
 	ordering = ['-id']
 	


 	def get_context_data(self, *args, **kwargs):
 		cat_menu = Category.objects.all()
 		context = super(HomeView, self).get_context_data(*args, **kwargs)
 		context["cat_menu"] = cat_menu
 		return context

def ContactView(request):

	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(
			message_name,# subject
			message,# message
			message_email,# from
			[settings.EMAIL_HOST_USER],#to
			)

		return render(request, 'contact.html', {
			"message_name": message_name,
			})
	else:
		return render(request, 'contact.html', {})

# class ArticleView(DetailView):
#  	model = Post
#  	template_name= 'article_detail.html'


#  	def get_context_data(self, *args, **kwargs):
#  		cat_menu = Category.objects.all()
#  		context = super(ArticleView, self).get_context_data(*args, **kwargs)

#  		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
#  		total_likes = stuff.total_likes()
#  		liked = False
#  		if stuff.likes.filter(id=self.request.user.id).exists():
#  			liked = True


#  		context["liked"] = liked
#  		context["cat_menu"] = cat_menu
#  		context["total_likes"] = total_likes
#  		return context
@csrf_exempt
def ArticleView(request, pk):
	if request.method == "POST":
		comment = request.POST["comment"]
		post_id = request.POST["post_id"]
		user_id = request.POST["user_id"]
		user = User.objects.get(id=user_id)
		post = Post.objects.get(id=post_id)

		d = Comment(post=post, user=user, body=comment)
		d.save()
		return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

	post = Post.objects.get(pk=pk)
	comments = Comment.objects.filter(post=post).order_by('-id')
	stuff = get_object_or_404(Post, id=pk)
	total_likes = stuff.total_likes()
	liked = False
	if stuff.likes.filter(id=request.user.id).exists():
		liked = True

	return render(request, 'article_detail.html', {
		"post": post,
		"liked": liked,
		"total_likes": total_likes,
		"comments": comments,

		})

class AddPostView(CreateView):
 	model = Post
 	form_class = PostForm
 	template_name= 'add_post.html'
 	# fields = '__all__'

class UpdatePostView(UpdateView):
 	model = Post
 	form_class = UpdatePostForm
 	template_name= 'update_post.html'
 	# fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
 	model = Post
 	template_name= 'delete_post.html'
 	success_url = reverse_lazy('home')

class AddCategory(CreateView):
 	model = Category
 	form_class = CategoryForm
 	template_name= 'add_category.html'
 	# fields = '__all__'

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats).order_by('-id')
	return render(request, 'category.html', {
		"category_posts": category_posts,
		"cats": cats,
		})

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {
		"cat_menu_list": cat_menu_list,
		})


