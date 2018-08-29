from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from qa import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404

'''
	Main page
	/?page=<num_page>
'''
#question per page
limit = 10

def list_new_questions(request):
	questions = models.Question.objects.new()
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(questions, limit)
	paginator.base_url = "/question/"
	page = paginator.page(page)
	return render_to_response(
		'list_new_questions.html',
		'page': page,
		'paginator': paginator,
		'quesitons': page.object_list,
	)




