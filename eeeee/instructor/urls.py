"""ee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include,path

from . import views

urlpatterns = [
	path('login/',views.login,name='login_instructor'),
	path('newinstructor/',views.newinstructor,name='newinstructor'),
    path('', views.index),
    path('logout/',views.logout),
    path('new_subjective_exam',views.new_subjective_exam,name='new_subjective_exam'),
    path('new_exam',views.new_exam,name='new_exam'),
    path('edit_exam/<int:exam_id>',views.edit_exam,name='edit_exam'),
    path('edit_question/<int:question_id>',views.edit_question,name='edit_question'),
    path('new_question/<int:exam_id>',views.new_question,name='new_question'),
    path('new_question_from_db/<int:exam_id>/<int:question_bank_qid>',views.new_question_from_db,name='new_question_from_db'),
    path('exam/<int:exam_id>',views.show_exam,name='show_exam'),
    path('topic_select/<int:exam_id>',views.ts,name='qb'),
    path('qb/<int:exam_id>',views.qb,name='qb'),
    path('look_questions/<int:topic_id>',views.show_questions_in_topic,name='show_questions_in_topic'),
    path('topics_in_qb/',views.topics_in_qb,name='topics_in_qb'), # new_question_from_d
    path('<int:exam_id>/subm_results',views.subm_results,name='subm_results'),
]
