from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def get_task_content(task):
  form=TaskForm()
  count_tasks=task.count()
  return {
      'form':form,
      'all_tasks':task,
      'count_tasks':count_tasks
  } 
  
@login_required
def index(request):
  tasks=request.user.tasks.all().values()
  context=get_task_content(tasks)
  return render(request,"tasks/index.html",context)

@login_required  
def filter_task(request,filter_type):
  tasks = request.user.tasks.all()
  if filter_type=='all': 
     return redirect('tasks:index')
    
  elif filter_type=='active':
    
    tasks=tasks.values().filter(is_completed=False)
    
     
  elif filter_type=='completed':
     
     tasks=tasks.values().filter(is_completed=True)
      
  context=get_task_content(tasks)
  return render(request,"tasks/index.html",context)
      
 
@login_required
def add_task(request):
  if request.method=="POST":
    form=TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False) 
        task.user = request.user    
        task.save()       
        return redirect('tasks:index')
    else:
      return redirect('tasks:index')
    
  return redirect('tasks:index')
  
@login_required    
def delete_task(request,task_id):
  if request.method=='POST':
      deletedTask=get_object_or_404(Task,id=task_id,user_id=request.user)
      deletedTask.delete()
      return redirect('tasks:index')
    
  return redirect('tasks:index')

@login_required
def complete_task(request,task_id):
  if request.method=='POST':
       task = get_object_or_404(Task,id=task_id,user_id=request.user)
       task.is_completed = not task.is_completed
       task.save()
       return redirect('tasks:index')
   
  return redirect('tasks:index')

@login_required        
def update_task(request,task_id):
     if request.method=='POST':
       task = get_object_or_404(Task,id=task_id,user_id=request.user)
       task.task=request.POST['update_task']
       task.save()
       return redirect('tasks:index')
     else:
       return redirect('tasks:index')
 
 
 
    