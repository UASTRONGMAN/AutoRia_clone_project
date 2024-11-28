from typing import Type

from django.contrib.auth import get_user_model

from rest_framework.generics import get_object_or_404

from rest_framework_simplejwt.tokens import BlacklistMixin, Token

from core_app.dataclasses.user_dataclass import User
from core_app.enums.action_token_enum import ActionTokenEnum
from core_app.exceptions.jwt_exception import JWTException

UserModel: User = get_user_model()

ActionTokenClassType = Type[BlacklistMixin | Token]

class ActionToken(BlacklistMixin, Token):
    pass

class UserActivationToken(ActionToken):
    token_type = ActionTokenEnum.ACTIVATE.token_type
    lifetime = ActionTokenEnum.ACTIVATE.lifetime
    
class RecoveryPasswordToken(ActionToken):
    token_type = ActionTokenEnum.RECOVERY_PASSWORD.token_type
    lifetime = ActionTokenEnum.RECOVERY_PASSWORD.lifetime

class JWTService:
    @staticmethod
    def create_token(user, token_class:ActionTokenClassType):
        return token_class.for_user(user)

    @staticmethod
    def verify_token(token, token_class:ActionTokenClassType):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except Exception:
            return JWTException

        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)