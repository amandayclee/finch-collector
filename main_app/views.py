from django.shortcuts import render

finches = [
  {'name': 'Zebra Finch', 'color': 'black and white stripes', 'description': 'small and sociable', 'habitat': 'grassy areas', 'region': 'Australia'},
  {'name': 'Gouldian Finch', 'color': 'brightly colored plumage', 'description': 'highly prized for its beauty', 'habitat': 'woodlands and savannas', 'region': 'Australia'},
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })