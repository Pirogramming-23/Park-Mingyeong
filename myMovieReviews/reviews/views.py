from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import MovieReview
from .forms import MovieReviewForm

class MovieReviewListView(ListView):
    model = MovieReview
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'
    paginate_by = 10

class MovieReviewDetailView(DetailView):
    model = MovieReview
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

class MovieReviewCreateView(CreateView):
    model = MovieReview
    form_class = MovieReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('reviews:review_list')
    
    def form_valid(self, form):
        return super().form_valid(form)

class MovieReviewUpdateView(UpdateView):
    model = MovieReview
    form_class = MovieReviewForm
    template_name = 'reviews/review_form.html'
    
    def get_success_url(self):
        return reverse_lazy('reviews:review_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        return super().form_valid(form)

def delete_review(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    review.delete()
    return redirect('reviews:review_list')
