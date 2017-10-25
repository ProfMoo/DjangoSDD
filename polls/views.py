from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice, Quarterback

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	
	def get_queryset(self):
		"""return the last five published questions"""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView): 
	model = Question
	template_name = 'polls/detail.html' #check template for details, assigning template here

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html' #check template for details, assigning template here

class AyyLmao(generic.ListView):
	template_name = 'polls/ayylmao.html'
	context_object_name = 'player_list'
	def get_queryset(self):
		"""return the last five published questions"""
		return Quarterback.objects.order_by('name')

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#to prevent a double post from "BACK" button...
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
