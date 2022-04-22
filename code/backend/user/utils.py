# import json
from .models import CustomUser

def create_custom_user(strategy, details, response, user, *args, **kwargs):
    """
    Part of the Python Social Auth pipeline which creates a student upon
    signup. If student already exists, updates information from Facebook
    or Google (depending on the backend).
    Saves friends and other information to fill database.
    """
    # backend_name = kwargs["backend"].name
    custom_user, _ = CustomUser.objects.get_or_create(user=user)
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
