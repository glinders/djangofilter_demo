from django.shortcuts import render
from core.models import Book
from core.filters import BookFilter
from django.views.generic.list import ListView


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['form'] = self.filterset.form
        return context
