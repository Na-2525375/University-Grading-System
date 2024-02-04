
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signupPage/', signupPage,name='signupPage'),
    path('', loginPage,name='loginPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('dashboardPage/', dashboardPage,name='dashboardPage'),
    path('createStudenPage/', createStudenPage,name='createStudenPage'),
    path('viewStudentPage/', viewStudentPage,name='viewStudentPage'),
    path('createSubjectPage/', createSubjectPage,name='createSubjectPage'),
    path('viewSubjectPage/', viewSubjectPage,name='viewSubjectPage'),
    path('inputMarksPage/<str:student_id>', inputMarksPage,name='inputMarksPage'),
    path('viewMarksPage/<str:student_id>', viewMarksPage,name='viewMarksPage'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
