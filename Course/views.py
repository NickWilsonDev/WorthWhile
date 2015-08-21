from django.shortcuts import render, render_to_response, get_object_or_404

from models import Course, CourseForm
from convertImage import create_thumbnail_from_image_field

# Create your views here.
def index(request):
    return render_to_response('Course/index.html')

def listView(request):
    courses = Course.objects.order_by('pk')
    return render(request, 'Course/listView.html', {'courses': courses})


def detailView(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'Course/courseDetail.html', {'course': course})

def gallery(request):
    courses = Course.objects.order_by('pk')
    return render(request, 'Course/gallery.html', {'courses': courses})

#will need to also use this to be able to edit course
def addChangeView(request, pk=-1):
    if pk == -1:
        if request.method == "POST":
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                course = form.save(commit=False)
                course.save()
                create_thumbnail_from_image_field(course.art, course.thumbnail, 200, 200)
                course.save()
                courses = Course.objects.order_by('pk')
                return render(request, 'Course/listView.html', \
                              {'courses': courses})
        else:
            form = CourseForm()
        return render(request, 'Course/addCourse.html', {'form':form})
    # edit part
    else:
        course = get_object_or_404(Course, pk=pk)
        if request.method == "POST":
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                course = form.save(commit=False)
                course.save()
                create_thumbnail_from_image_field(course.art, course.thumbnail, 200, 200)
                course.save()
                return render(request, 'Course/courseDetail.html', {'course':course})
        else:
            form = CourseForm(instance=course)
        return render(request, 'Course/courseEdit.html', {'form': form})
