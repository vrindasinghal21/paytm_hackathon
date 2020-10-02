from django.conf.urls import url
from .views import Signup,login,user_data,govt_data
# from . import views

urlpatterns=[
	url(r'^Signup/$',Signup),
	url(r'^login/$',login),
	url(r'^user_data/$',user_data),
	url(r'^govt_data/$',govt_data)
]