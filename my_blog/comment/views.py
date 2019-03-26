from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from article.models import ArticlePost
from .forms import CommentForm

@login_required(login_url='/userprofile/login/')
def post_comment(request,article_id):
	article = get_object_or_404(ArticlePost,id=article_id)

	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.article = article
			new_comment.user = request.user
			new_comment.save()
			return redirect(article)
		else:
			return HttpResponse("表单内容有误，请重新填！")
	else:
		return HttpResponse("请求方法不被允许！")



