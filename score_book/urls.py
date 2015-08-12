from score_book import views
from django.conf.urls import url


urlpatterns = [
	url(r'^$', views.user_landing, name='user_landing')
]

