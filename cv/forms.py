from django import forms
from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from django.forms import fields, models, formsets, widgets
from .models import CV,EQ,Skill,Achieve,WE

class CVForm(forms.ModelForm):
	class Meta:
		model=CV
		fields =['name','phone_no','email_id','profile','about_you','photo','address','hobbies_and_intrests']
		widgets={
		'name':forms.TextInput(attrs={'placeholder':'Enter your Full Name here'}),
		'phone_no':forms.TextInput(attrs={'placeholder':'Enter your Phone No here'}),
		'email_id':forms.TextInput(attrs={'placeholder':'Enter your email id here'}),
		'hobbies_and_intrests':forms.Textarea(attrs={'placeholder':'Enter your hobbies here'}),
		}
class EQForm(forms.ModelForm):
	class Meta:
		model=EQ
		fields=['course','instute_name','stream','percentage']
		widgets={
		'course':forms.Select(attrs={'class':'form-control'}),
		'instute_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name of institution here'}),
		'stream':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Stream'}),
		'percentage':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your percentages here'}),
		}
class SkillForm(forms.ModelForm):
	class Meta:
		model=Skill
		fields=['skill','level']
		widgets={
		'skill':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter skill'}),
		'level':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your level in percentage'}),
		}

class AchievementForm(forms.ModelForm):
	class Meta:
		model=Achieve
		fields=['achievements']
		widgets={
		'achievements':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your achievement'}),
		}

class WEForm(forms.ModelForm):
	class Meta:
		model=WE
		fields =['organisation','designation','location','years']
		widgets={
		'organisation':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter organisation Name here'}),
		'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter designation here'}),
		'location':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter location of company here'}),
		'years':forms.TextInput(attrs={'class':'form-control','placeholder':'years of experience there'}),
		}


def get_eq_formset(form, formset=models.BaseInlineFormSet, **kwargs):
	return models.inlineformset_factory(CV, EQ, form, formset, **kwargs)

def get_skill_formset(form, formset=models.BaseInlineFormSet, **kwargs):
	return models.inlineformset_factory(CV, Skill, form, formset, **kwargs)

def get_achieve_formset(form, formset=models.BaseInlineFormSet, **kwargs):
	return models.inlineformset_factory(CV, Achieve, form, formset, **kwargs)

def get_we_formset(form, formset=models.BaseInlineFormSet, **kwargs):
	return models.inlineformset_factory(CV, WE, form, formset, **kwargs)
