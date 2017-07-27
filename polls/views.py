from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Candidate, Voter


class IndexView(generic.ListView):
    model = Candidate
    context_object_name = 'candidates'
    template_name = 'polls/index.html'


class ResultsView(generic.ListView):
    candidates=Candidate.objects.all()
    context = {'candidates': candidates}
    def get(self,request):
        return render(request,"polls/results.html",self.context)


@login_required
def votes(request):

    candidates = Candidate.objects.all()
    if Voter.objects.filter(user_id=request.user.id).exists():
        return render(request, 'polls/results.html',{'candidates':candidates,'error_message': "Sorry, but you have already voted."})

    try:
        selected_choice = candidates.get(pk=request.POST['contestant'])
    except:
        return render(request,'polls/index.html',{'candidates':candidates,'error_message':"Please select a choice now"})

    # if user haven't voted yet then allow
    selected_choice.vote_count += 1
    selected_choice.save()
    v = Voter(user=request.user, choosen=selected_choice)
    v.save()
    return render(request, 'polls/results.html', {'candidates': candidates, 'contestant': selected_choice} )
