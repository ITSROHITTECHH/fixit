from django.urls import path
from .views import test_api, signup, login_api,contact_api,create_booking,my_bookings


urlpatterns = [
    path('api/test/', test_api),
    path('api/signup/', signup),
    path('api/login/',login_api),
    path('api/contact/', contact_api),
    path('api/booking/', create_booking),
    path("api/my-bookings/", my_bookings),
    
]






