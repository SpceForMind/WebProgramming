from django.http import HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from qa import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404

#question per page
limit = 10

def paginate(request, qs):
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	page = paginator.page(page)
	return paginator, page

'''
	Main page
	/?page=<num_page>
'''
def list_new_questions(request):
	questions = models.Question.objects.new()
	paginator, page = paginate(request, questions)
	paginator.base_url = "/question/"
	return render_to_response(
		'list_questions.html',
                {
		    'paginator': paginator,
	    	    'quesitons': page.object_list,
                },
	)   
'''
    Page with popular posts
    /popular/?page=<page_num>
'''
def popular_questions(request):
    questions = models.Question.objects.popular()
    paginator, page = paginate(request, questions)
    paginator.base_url = "/question/"
    return render_to_response(
                'list_questions.html',
                {
                    'paginator': paginator, 
                    'questions': questions[0:],
                },
    )

'''
    Page of one question
    /question/<question_id>
'''
def question(request, pk):
    question = get_object_or_404(question_id = pk)
    try:
        answers = models.Answer.objects.filter(question = question)[0:]
    except :
        answers = []
    return render_to_response(
        'question.html',
        {
            'question': question,
            'answers': answers, 
        },
    )
