"""
URL configuration for hotelProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from hotel_app import views
from hotelProject import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HotelListView.as_view()),
    path("booking/", views.BookingListView.as_view()),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("<str:hotel_city>/rooms/<str:room_type>/review", views.leave_review),
    path("<str:hotel_city>/rooms/<str:room_type>/", views.booking_view, name="book"),
    path("<str:hotel_city>/rooms/", views.RoomListView.as_view()),
    path("index", views.index),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
