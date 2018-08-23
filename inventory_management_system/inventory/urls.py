from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^laptops$', display_laptops, name="display_laptops"),
    url(r'^desktops$', display_desktops, name="display_desktops"),
    url(r'^mobiles$', display_mobiles, name="display_mobiles"),

    url(r'^add_laptop$', add_laptop, name="add_laptop"),
    url(r'^add_desktop$', add_desktop, name="add_desktop"),
    url(r'^add_mobile$', add_mobile, name="add_mobile"),

    url(r'^laptops/edit_item/(?P<pk>\d+)$', edit_laptop, name="edit_laptop"),
    url(r'^desktops/edit_item/(?P<pk>\d+)$', edit_desktop, name="edit_desktop"),
    url(r'^mobiles/edit_item/(?P<pk>\d+)$', edit_mobile, name="edit_mobile"),

    url(r'^laptops/delete/(?P<pk>\d+)$', delete_laptop, name="delete_laptop"),
    url(r'^desktops/delete/(?P<pk>\d+)$', delete_desktop, name="delete_desktop"),
    url(r'^mobiles/delete/(?P<pk>\d+)$', delete_mobile, name="delete_mobile")

]
