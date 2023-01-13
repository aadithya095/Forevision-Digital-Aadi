from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView

from .auth_forms import SignUpForm
from .forms import SingleReleaseForm


class SignUpView(CreateView, SuccessMessageMixin):
    template_name = "client/sign-up.html"
    success_url = reverse_lazy('login')
    form_class = SignUpForm
    success_message = "Account was created successfully."


class SingleReleaseFormView(LoginRequiredMixin, View):
    """
    View for Single Release Form. Client will enter the data for a single release in this form.
    """
    template_name = 'client/single-form.html'
    success_template = 'client/dashboard.html'

    def get(self, request):
        """Handles GET method"""
        form = SingleReleaseForm()

        context = {
            'form': form
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        """Handles POST method"""

        context = {
            'user': request.user,
        }

        form = SingleReleaseForm(request.POST)
        if form.is_valid():
            song_name = form.cleaned_data['song_name']
            song_id_type = form.cleaned_data['song_id_type']
            song_id = form.cleaned_data['song_id']
            territory = form.cleaned_data['territory']
            artist_name = form.cleaned_data['artist_name']
            artist_role = form.cleaned_data['artist_role']
            pline_year = form.cleaned_data['pline_year']
            pline_text = form.cleaned_data['pline_text']
            cline_year = form.cleaned_data['cline_year']
            cline_text = form.cleaned_data['cline_text']
            genre = form.cleaned_data['genre']
            record_label_name = form.cleaned_data['record_label_name']
            codec = form.cleaned_data['codec']
            bitrate = form.cleaned_data['bitrate']
            channels = form.cleaned_data['channels']
            sampling = form.cleaned_data['sampling']
            duration = form.cleaned_data['duration']
            uri = form.cleaned_data['uri']
            hash_algorithm = form.cleaned_data['hash_algorithm']
            hash_value = form.cleaned_data['hash_value']
            parental_warning = form.cleaned_data['parental_warning']
            image_id = form.cleaned_data['image_id']
            image_id_type = form.cleaned_data['image_id_type']
            image_type = form.cleaned_data['image_type']



class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Dashboard view for client. Will be able to access it once the client logs in and is authenticated and authorized.
    """
    template_name = "client/plan-page.html"

    def get(self, request):
        """Handles GET method"""
        context = {
            'user': request.user,
        }
        return render(request, self.template_name, context=context)
