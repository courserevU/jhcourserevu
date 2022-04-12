# from django.conf.urls import url
from django.urls import path
from .views import UserList
from django.conf.urls import include

urlpatterns = [
    path("", UserList.as_view()),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft'))
]

# TODO: FIGURE OUT WHAT THIS FOR AND WHERE IT'S FROM
# def callback(request):
#     # Get the state saved in session
#     expected_state = request.session.pop('auth_state', '')
#     # Make the token request
#     token = get_token_from_code(request.get_full_path(), expected_state)
#     # Get the user's profile
#     user = get_user(token)

#     # Get user info
#     # user attribute like displayName,surname,mail etc. are defined by the
#     # institute incase you are using single-tenant. You can get these
#     # attribute by exploring Microsoft graph-explorer.

#     username = user['jhed_id']
#     password = user['surname'] # need to modify this
#     email = user['jhed_email']

#     try:
#         # if use already exist
#         user = User.objects.get(jhed_id=username)

#     except User.DoesNotExist:
#         # if user does not exist then create a new user
#         #user = User.objects.create_user(username, email, password)
#         #user.save()
#         pass

#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request,user)
#         messages.success(request,"Success: You were successfully logged in.")
#         return redirect('home') # need to modify this
#     return redirect('home') # need to modify this

# def sign_out(request):
#     logout(request)
#     messages.success(request, "Successfully Logged Out")

#     return redirect('home') # need to modify this
