from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView #used for edit the objects
from .models import Album
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_album' #used because we can not take object_list name

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album       #used because django need to know what kind of thing you create
    fields = ['artist', 'album_title', 'genre', 'album_logo']    #Attributes which you gona work

class AlbumUpdate(UpdateView):
    model = Album
    fields =  ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index',)