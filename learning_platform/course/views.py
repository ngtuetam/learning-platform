from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Course, Lesson, Comment
from .serializers import CourseListSerializer, CourseDetailSerializer, LessonListSerializer, CommentsSerializer



# Serve Vue Application, ref: https://github.com/gtalarico/django-vue-template/blob/master/backend/api/views.py
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


# Create your views here.
@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializers = CourseListSerializer(courses, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    data = {
        'course': course_serializer.data,
        'lessons': lesson_serializer.data
    }

    return Response(data)

@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentsSerializer(lesson.comments.all(), many=True)

    return Response(serializer.data)

@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.get('name')
    content = data.get('content')

    # get the course from the backend
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(course=course, lesson=lesson, name=name, content=content, created_by=request.user)

    # return Response({'message':'The comment was added!'})
    
    serializer = CommentsSerializer(comment)
    return Response(serializer.data)

