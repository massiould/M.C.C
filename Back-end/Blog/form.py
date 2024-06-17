from django import forms
from .models import Question

class CategoryForm(forms.Form):
    CATEGORY_CHOICES = (
        ('pratique', 'Question pratique'),
        ('droit', 'Question de droit'),
    )
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Choisissez une catégorie')

class TypeForm(forms.Form):
    TYPE_CHOICES = (
        ('constitutionnel', 'Droit constitutionnel'),
        ('administratif', 'Droit administratif'),
        ('fiscal', 'Droit fiscal'),
        ('pénal', 'Le droit pénal et procédure pénale'),
        ('judiciaire', 'Droit judiciaire'),
        ('civil', 'Droit civil'),
        ('commercial', 'Droit commercial'),
        ('social', 'Droit social'),
        ('sécurité_sociale', 'Droit de la sécurité sociale et droit international privé'),
    )
    type = forms.ChoiceField(choices=TYPE_CHOICES, label='Choisissez un type')

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content']
        labels = {
            'title': 'Titre de la question',
            'content': 'Contenu de la question',
        }

class AnswerForm(forms.Form):
    content = forms.CharField(label='Contenu de la réponse', widget=forms.Textarea)