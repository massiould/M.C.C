from django.shortcuts import render
from django.shortcuts import render, redirect
from .form import CategoryForm, TypeForm, QuestionForm
from .models import  Question, Answer, ResponseVote
from .form import AnswerForm
from rest_framework import generics
from .serializer import AnswerSerializer, QuestionSerializer

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def choose_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category = category_form.cleaned_data['category']
            request.session['chosen_category'] = category
            if category == "pratique":
                return redirect('ask_question')
            else:
                return redirect('choose_type')
            
    else:
        category_form = CategoryForm()
    return render(request, 'choose_category.html', {'category_form': category_form})

@login_required
def choose_type(request):
    if request.method == 'POST':
        type_form = TypeForm(request.POST)
        if type_form.is_valid():
            type = type_form.cleaned_data['type']
            request.session['chosen_type'] = type
            return redirect('ask_question')
    else:
        type_form = TypeForm()
    return render(request, 'choose_type.html', {'type_form': type_form})

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            category = request.session.get('chosen_category')
            type = request.session.get('chosen_type')
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = request.user
            question = Question.objects.create(title=title, category=category, type=type, content=content, author=author)
            request.session.pop('chosen_category', None)
            request.session.pop('chosen_type', None)
            form.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = QuestionForm()
    return render(request, 'ask_question.html', {'form': form})

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'question_detail.html', {'question': question})



@login_required
def create_response(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question_id = question_id
            content = form.cleaned_data['content']
            question = get_object_or_404(Question, pk=question_id)
            response = Answer.objects.create(question=question, content=content, author=request.user)
            return redirect('question_detail', question_id=question_id)
    else:
        form = AnswerForm()
    return render(request, 'create_response.html', {'form': form})


@login_required
def response_vote(request, response_id, vote_type):
    response = Answer.objects.get(pk=response_id)
    user = request.user
    existing_vote = ResponseVote.objects.filter(user=user, response=response).exists()
    if not existing_vote:
        ResponseVote.objects.create(user=user, response=response, vote_type=vote_type)
        if vote_type == 'U':
            response.upvotes += 1
        elif vote_type == 'D':
            response.downvotes += 1
        response.save()
    return redirect('question_detail', question_id=response.question.id)


class AnswerListByQuestionAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        queryset = Answer.objects.filter(question_id=question_id)
        return queryset
    
class QuestionListAll(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        return queryset

class QuestionListById(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        queryset = Question.objects.filter(id=question_id)
        return queryset

class QuestionListByAuthor(generics.ListAPIView):
    serializer_class = QuestionSerializer
    def get_queryset(self):
        author_id = self.kwargs['author_id']
        queryset = Question.objects.filter(author__id=author_id)
        return queryset


    
