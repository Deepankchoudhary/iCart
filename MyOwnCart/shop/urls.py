from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("About/", views.about, name="Aboutus"),
    path("Contactus/", views.contact, name="Contactus"),
    path("Tracking/", views.track, name="TrackingStatus"),
    path("Search/", views.search, name="Search"),
    path("ProductView/<int:myid>", views.product, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("Signup/", views.practice, name="Practice"),

]
