from django.shortcuts import render
from .forms import StudentForm


def index(request):

	form = StudentForm()

	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			
	context = {'form':form}
	return render(request, 'app/index.html', context)