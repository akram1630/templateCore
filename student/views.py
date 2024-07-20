from django.shortcuts import render
#from django.http.response import HttpResponse
# Create your views here.


def all_students(request):
  myVars = {
      'fname': 'Akram',
      'lname': 'Boutoutaou',
      'mylist': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      'mydict': {
          'python': 'django'
      },
      'smallWord': 'hello small world',
      'myEmptylist': []
  }  #context passes dictionary
  return render(request, 'student.html', context=myVars)


def add_student(request):

  return render(request, 'add.html')


def edit_student(request):
  return render(request, 'edit.html')
