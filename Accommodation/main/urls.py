from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name='home'),
    path('admin-dashboard', views.admin_dashboard, name='dashboard'),
    path('apply', views.apply, name='apply'),
    path('apply/<str:id>',views.apply_room, name='apply-accommodation'),
    path('allocate', views.allocate_rooms, name='allocate'),
    path('view', views.view_allocated, name='view'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('applications', views.applications, name='applications'),
    path('housing', views.housing, name='housing'),
    path('contact', views.contact, name='contact'),
    path('about',  views.about, name='about'),
    path('unallocate', views.unallocate_rooms, name='unallocate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)