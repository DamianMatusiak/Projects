from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Entry


def index(request):
    if request.user.is_authenticated:
        entries = (Entry.objects
                   .exclude(tags__id__in=request.user.userprofile
                            .get_entries_for_tags().values_list('id'))
                   .order_by("-pub_date"))
    else:
        entries = Entry.objects.order_by("-pub_date")

    post_count = Entry.objects.count()

    return render(request, "blog/index.html",
                  {"entries": entries, "post_count": post_count})


class EntryDetailView(DetailView):
    model = Entry
    context_object_name = "entry"


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ["title", "body_text"]
    success_url = reverse_lazy("index")


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ["title", "body_text"]
    success_url = reverse_lazy("index")


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("index")
