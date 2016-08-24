from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add-report', views.add_report_view, name='add_report_view'),
    url(r'^report-one$', views.report_one_view, name='report_one_view'),
    

    url(r'^editdatabase$', views.editdatabase_view, name='editdatabase_view'),
    url(r'^lifecycle$', views.lifecycle_view, name='lifecycle_view'),
    url(r'^weights$', views.weights_view, name='weights_view'),
    url(r'^supplier_specific$', views.supplier_specific_view, name='supplier_specific_view'),
    url(r'^travelingmethods$', views.travelingmethods_view, name='travelingmethods_view'),
    url(r'^editdata$', views.editdata_view, name='editdata_view'),
    url(r'^dataabc$', views.dataabc_view, name='dataabc_view'),


]