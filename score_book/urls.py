from score_book import views
from django.conf.urls import url


urlpatterns = [
	url(r'^$', views.landing, name='landing'),
	url(r'^student$', views.student_landing, name='student_landing'),
	url(r'^instructor$', views.instructor_landing, name='instructor_landing'),
]

