from django.shortcuts import render
from .models import Finch

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
    return render(request, 'finches/detail.html', {
        'finch': finch
    })