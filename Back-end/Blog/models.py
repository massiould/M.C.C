
from django.db import models
from django.contrib.auth.models import User



class Question(models.Model):
    STATUS_CHOICES = ( #TODO a mettre plus tard dans un fichier avec tous les choices
        ('en_cours', 'En cours'),
        ('resolue', 'Résolue'),
        ('ferme', 'Fermé'),
    )
    CATEGORY_CHOICES = (
        ('pratique', 'Question pratique'),
        ('droit', 'Question de droit'),
    )
    TYPE_CHOICES = ( #TODO a mettre plus tard dans un fichier avec tous les choices
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
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_cours')

   

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    votes = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f"Answer to '{self.question.title}'"
    
    def upvote(self):
        self.votes += 1
        self.save()

    def downvote(self):
        self.votes -= 1
        self.save()

class ResponseVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=1, choices=(('U', 'Upvote'), ('D', 'Downvote')))



