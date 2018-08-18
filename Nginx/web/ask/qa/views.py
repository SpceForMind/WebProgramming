from django.http import HttpResponse

#simple controller
def test(request, *args, **kwargs):
	return HttpResponse('OK')
