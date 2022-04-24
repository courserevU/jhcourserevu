# import json
from .models import CustomUser

def create_custom_user(strategy, details, response, user, *args, **kwargs):
    """
    Create a custom user associated with the social account.
    Affiliated with authentication pipeline in settings.py
    """
    # backend_name = kwargs["backend"].name
    custom_user, _ = CustomUser.objects.get_or_create(user=user)
    custom_user.email = user.email
    # social_user = user.social_auth.filter(provider=backend_name).first()
    # if backend_name == "google-oauth2":
    # update_user_google(custom_user, social_user)
    custom_user.save()
    return kwargs

# def update_user_google(social_user):
#     try:
#         access_token = social_user.extra_data["access_token"]
#     except TypeError:
#         access_token = json.loads(social_user.extra_data)["access_token"]
