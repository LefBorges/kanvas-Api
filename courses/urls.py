from django.urls import path
from courses.views import CreateCourseView, UpdateDestroyCourseView
from contents.views import CreateContentView, UpdateDestroyContentView
from students_courses.views import StudentCourseView


urlpatterns = [
    path("courses/", CreateCourseView.as_view()),
    path("courses/<uuid:course_id>/", UpdateDestroyCourseView.as_view()),
    path("courses/<uuid:course_id>/contents/", CreateContentView.as_view()),
    path("courses/<uuid:course_id>/contents/<uuid:content_id>/",  UpdateDestroyContentView.as_view()),
    path("courses/<uuid:course_id>/students/", StudentCourseView.as_view()),
]
