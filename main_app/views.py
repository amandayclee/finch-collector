from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
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
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form
    })
    
def add_feeding(request, finch_id):
  submitted_form = FeedingForm(request.POST)
  if submitted_form.is_valid:
    new_feeding = submitted_form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
    
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  
class FinchUpdate(UpdateView):
  model = Finch
  fields = ('color', 'description', 'habitat', 'region')
  
class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'