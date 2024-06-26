from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .forms import FeedingForm

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {
    'finches': finches
  })
  
def finches_detail(request, finch_id):
    # we need to communicate with the database here
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.toys.all().values_list('id')
    toys_that_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form,
        'toys': toys_that_finch_doesnt_have
    })
    
def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id=finch_id)
    
def add_feeding(request, finch_id):
  submitted_form = FeedingForm(request.POST)
  if submitted_form.is_valid:
    new_feeding = submitted_form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
    
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = ('color', 'description', 'habitat', 'region')
  
class FinchUpdate(UpdateView):
  model = Finch
  fields = ('color', 'description', 'habitat', 'region')
  
class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'
  
class ToyList(ListView):
  model = Toy
  
class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = ('name', 'color')
  
class ToyUpdate(UpdateView):
  model = Toy
  fields = ('name', 'color')
  
class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'