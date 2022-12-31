from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from models.models import Artist
from . forms import ArtistForm, ImageForm, SongForm, ClipForm 

class SingleReleaseFormView(LoginRequiredMixin, View):
    '''
    View for Single Release Form. Client will enter the data for a single release in this form.
    '''
    template_name = 'client/single-form.html'
    success_template = 'client/dashboard.html'

    def get(self, request):
        '''Handles GET method'''
        artist_form = ArtistForm()
        song_form = SongForm()
        image_form = ImageForm()
        clip_form = ClipForm()

        context = {
                'artist_form': artist_form,
               'song_form': song_form,
                'image_form': image_form,
                'clip_form': clip_form,
                }
        return render(request, self.template_name, context=context)

    def post(self, request):
        '''Handles POST method'''

        context = {
                'user':request.user,
                }

        song_form = SongForm(request.POST)
        image_form = ImageForm(request.POST)
        clip_form = ClipForm(request.POST)
        artist_form = ArtistForm(request.POST)

        songvalid = song_form.is_valid()
        imagevalid = image_form.is_valid()
        clipvalid = clip_form.is_valid()
        artistvalid = artist_form.is_valid()

        if artistvalid and imagevalid and songvalid:
            artist = artist_form.save()

            image = image_form.save(commit=False)
            image_file = request.POST['image_file']
            image.file = image_file
            image.save()

            song = song_form.save(commit=False)
            song.image = image
            song.save()

            clip = clip_form.save(commit=False)
            clip.song = song
            clip.save()
            return render(request, self.success_template, context)





class DashboardView(LoginRequiredMixin, TemplateView):
    '''
    Dashboard view for client. Will be able to access it once the client logs in and is authenticated and authorized.
    '''
    template_name = "client/plan-page.html"

    def get(self, request):
        '''Handles GET method'''
        context = {
                'user': request.user,
                }
        return render(request, self.template_name, context=context)
