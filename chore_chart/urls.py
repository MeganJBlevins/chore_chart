from django.urls import include, re_path, path
from . import views

app_name = 'chore_chart'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^add-chore/', views.add_chore_form, name='add_chore_form'),
    re_path(r'^chore-index/', views.chore_index, name='chore_index'),
    re_path(r'^register/', views.register, name='register'),
    re_path(r'^user_login/$',views.user_login, name="user_login"),
    re_path(r'^success/$', views.success, name="success"),
    re_path(r'^goals/$', views.goals, name="goals")

]
