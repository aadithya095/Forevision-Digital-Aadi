from django.contrib.auth import login, logout, authenticate
from models.user_models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView, FormView
from forms.single_release_form import SingleReleaseForm
# from .auth_forms import SignUpForm
from django.contrib import messages
from models.ddex_models import (Party, Song, Album,)


"""
TODO:
    - Refactor view class to have appropriate Views such as FormViews
"""


def singleRelease(request):
    if request.method == 'POST':
        form = SingleReleaseForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Successfully created")
    else:
        form = SingleReleaseForm()

    return render(request, 'single-release.html', {'form': form})


# class LandingPage(TemplateView):
    # """
    # View for landing page that will be shown to the users when they visit
    # the website.
    # """
    # template_name = "landing.html"

    # def get(self, request):
        # return render(request, self.template_name)


# class LoginPage(FormView):
    # """
    # View for login page.
    # Currently it does not have the post method to handle login logic.
    # TODO: Need to add post method
    # """
    # template_name = "client/login.html"
    # form = AuthenticationForm

    # def get(self, request):
        # return render(request, self.template_name)

    # def post(self, request):
        # form = self.form(request.POST)
        # if form.is_valid():
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user = authenticate(username=username, password=password)
            # if user:
                # login(request, user)
                # context = {"user": user}
                # return render(request, 'client/dashboard.html', context)
            # else:
                # redirect('client:user_login')




# class RegisterPage(TemplateView):
#     """
#     View for register page.
#     Currently does not handle post method.
#     TODO:
#         - Need to add post method
#         - Need to extend User Model and create Profile Model
#     """
#     template_name = 'client/register.html'

#     def get(self, request):
#         return render(request, self.template_name)

# class SignUpView(CreateView, SuccessMessageMixin):
    # template_name = "client/sign-up.html"
    # success_url = reverse_lazy('login')
    # form_class = SignUpForm
    # success_message = "Account was created successfully."


# class OrderFormPage(TemplateView):
#     template_name = 'client/order-form.html'
#     success_template_name = "client/party-form.html"

#     def get(self, request):
#         order_form = OrderForm()
#         context = {
#             'form': order_form,
#         }
#         # Renders order-form.html
#         return render(request, self.template_name, context=context)

#     def post(self, request):
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             # Just keeping the data in a variable if in case
#             # I might need it to set a conditional option
#             # for single or album release
#             new_order = order_form.save()
#             # when the order is saved the client goes to the next form
#             # party_form and renders the form as per the plan choice
#             order_pk = new_order.pk
#             # Saving the pk of the order in the session
#             request.session['order_pk'] = order_pk
#             plan_choice = new_order.plan_choice
#             party_form = PartyForm()
#             context = {
#                 'form': party_form,
#                 'order_pk': order_pk,
#                 'plan_choice': plan_choice,
#             }
#             # Renders party-form.html
#             return render(request, self.success_template_name, context=context)
#         # TODO: Need to return error message as well
#         return redirect('client:order_form')


# class PartyFormPage(TemplateView):
#     template_name = 'client/party-form.html'
#     success_template_name = 'client/song-form.html'

#     def post(self, request):
#         party_form = PartyForm(request.POST)
#         if party_form.is_valid():
#             new_party = party_form.save()

#             # Go to Song Form
#             song_form = SongForm()
#             # Getting order_pk from session
#             order_pk = request.session['order_pk']
#             context = {
#                 "form": song_form,
#                 "order_pk": order_pk,
#             }
#             return render(request, self.success_template_name, context=context)
#         # TODO: Need to return error message as well
#         return redirect('client:party_form')


# class SongFormPage(TemplateView):
#     template_name = 'client/song-form.html'
#     success_template_name = 'client/image-form.html'

#     def post(self, request):
#         song_form = SongForm(request.POST)
#         if song_form.is_valid():
#             new_song = song_form.save(commit=False)
#             order_pk = request.session['order_pk']
#             order = Order.objects.get(pk=order_pk)
#             # For now I have added all the parties in the song
#             # But the choices will be automatically added if
#             # ModelChoiceForm is used in form
#             # TODO: Add ModelChoiceForm in forms and remove the for loop
#             for party in order.party_set.all():
#                 new_song.party.add(party)


# class DashboardView(TemplateView):
#     """
#     Dashboard view for client. Will be able to access it once the client logs in and is authenticated and authorized.
#     Currently does not require login, in future LoginRequiredMixin will be added
#     """
#     template_name = "client/plan-page.html"

#     def get(self, request):
#         return render(request, self.template_name)
