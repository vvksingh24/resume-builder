from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import *
from django.core.urlresolvers import reverse
from .forms import *


class IndexView(ListView):
    template_name='cv/index.html'
    context_object_name='cv_list'

    def get_queryset(self):
        return CV.objects.all()


class CView(DetailView):
    model = CV
    template_name = 'cv/resume.html'


def CreateCV(request):
    EQFormSet = get_eq_formset(EQForm, extra=1, can_delete=True)
    SKILLSFormSet = get_skill_formset(SkillForm, extra=1, can_delete=True)
    ACHIEVEFormSet = get_achieve_formset(AchievementForm, extra=1, can_delete=True)
    WEFormSet = get_we_formset(WEForm, extra=1, can_delete=True)
    if request.POST:
        form = CVForm(request.POST or None, request.FILES or None)
        print (form.is_valid())
        if form.is_valid():
            cv = form.save(commit=False)
            eqformset = EQFormSet(request.POST or None, request.FILES or None, prefix='education_form', instance=cv)
            skillformset = SKILLSFormSet(request.POST or None, request.FILES or None, prefix='skills_form', instance=cv)
            achieveformset = ACHIEVEFormSet(request.POST or None, request.FILES or None, prefix='achievement_form', instance=cv)
            weformset = WEFormSet(request.POST or None, request.FILES or None, prefix='work_experience_form',instance=cv)

            if eqformset.is_valid() and skillformset.is_valid() and achieveformset.is_valid() and weformset.is_valid():
                cv.save()
                eqformset.save()
                skillformset.save()
                achieveformset.save()
                weformset.save()
                return redirect('cv:detail', pk=cv.id)
        else:
            return render(request, 'cv/error.html', {'form':form})
    else:
        form = CVForm()
        eqformset = EQFormSet(prefix='education_form', instance=CV())
        skillformset = SKILLSFormSet(prefix='skills_form', instance=CV())
        achieveformset = ACHIEVEFormSet(prefix='achievement_form', instance=CV())
        weformset = WEFormSet(prefix='work_experience_form', instance=CV())
    context={
            'form': form,
            'eqformset': eqformset,
            'skillformset': skillformset,
            'achieveformset': achieveformset,
            'weformset': weformset

        }
    return render(request, 'cv/create.html', context)


