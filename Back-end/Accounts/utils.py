from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from .models import Lawyer_identification


def send_password_reset_email(request, email):
    user = User.objects.get(email=email)
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_link = f"http://example.com/reset-password/{uid}/{token}/"
    
    send_mail(
        'Password Reset',
        f'Click the following link to reset your password: {reset_link}',
        'from@example.com',
        [email],
        fail_silently=False,
    )


    
#TODO: creer en 1 fois avec un script la base de donnée










def validate(Siren, Barreau, author):
    # Récupérer l'utilisateur avec le nom d'auteur spécifié
    author_user = User.objects.filter(username=author).first()
    

    # Vérifier si l'utilisateur existe
    if author_user :
        check = Lawyer_identification.objects.filter(name=author_user.last_name)
        for info in check:
            if info.barreau == Barreau or info.siren == Siren:
                print ("true")
                return True
            
        else:
            print("False")
            return False


    
