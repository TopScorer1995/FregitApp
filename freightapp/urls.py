from django.urls import path
from django.contrib.auth import views as auth_views

from freightapp import views as freightapp_view

urlpatterns = [

    path('', freightapp_view.home, name='home'),
    path('dashboard/', freightapp_view.dashboard, name='dashboard'),
    path('add_new_tab/', freightapp_view.add_new_tab, name='add_new_tab'),
    path('showtab/', freightapp_view.showtab, name='showtab'),
    # path('clearance/', freightapp_view.haulage, name='clearance'),
    path('clearance/page', freightapp_view.clearance_page, name='clearance_page'),
    path('clearance/input', freightapp_view.clearance_input, name='clearance_input'),
    path('client_registration/', freightapp_view.client_registration, name='client_registration'),
    path('shipment_page/', freightapp_view.shipment_page, name='shipment_page'),
    # path('haulage/', freightapp_view.haulage, name='haulage'),
    path('haulage/registerverhicle', freightapp_view.haulage_registervehicle, name='haulage_registervehicle'),
    path('haulage/deliverydetails', freightapp_view.haulage_deliverydetails, name='haulage_deliverydetails'),
    path('haulage/packaging', freightapp_view.haulage_packaging, name='haulage_packaging'),
    path('reports/', freightapp_view.reports, name='reports'),
    path('shipment_registration/', freightapp_view.shipment_registration, name='shipment_registration'),
    path('shipment_registration/air', freightapp_view.shipment_registration_air, name='shipment_registration_air'),
    path('shipment_registration/ocean', freightapp_view.shipment_registration_ocean, name='shipment_registration_ocean'),
    path('payment/', freightapp_view.payment, name='payment'),
    path('documentation/', freightapp_view.documentation, name='documentation'),
]