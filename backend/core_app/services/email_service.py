import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core_app.dataclasses.user_dataclass import User
from core_app.services.jwt_service import JWTService, RecoveryPasswordToken, UserActivationToken


class EmailService:
    @staticmethod
    def __send_email(to:str, template_name:str, context:dict, subject:str) -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject=subject, from_email=os.environ.get("EMAIL_USER"), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register(cls, user:User):
        token = JWTService.create_token(user, UserActivationToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email(
            user.email,
            'activate_user.html',
            {'name':user.profile.name, 'url':url},
            'Finish your registration'
        )

    @classmethod
    def recovery_password(cls, user:User):
        token = JWTService.create_token(user, RecoveryPasswordToken)
        url = f'http://localhost:3000/recovery_password/{token}'
        cls.__send_email(
            user.email,
            'recovery_password.html',
            {'name':user.profile.name, 'url':url},
            'Recovery password'
        )