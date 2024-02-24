from . import views
from django.urls import path

app_name = "budget"
urlpatterns = [
    path('', views.index, name='index'),
    path('budget/', views.budget, name='budget'),
    path('category/', views.category, name='category'),
    path('report/', views.reports, name='reports'),
    path('transactions/', views.transactions, name='transactions'),
    path('make_budget/', views.make_budget, name="make-budget"),
    path('make_category/<int:id>', views.make_category, name="make-category"),
    path('make_label/<int:id>', views.make_label, name="make-label"),
    path('make_transaction/', views.make_transaction, name="make-transaction"),
    path('view_category/<int:id>', views.view_category, name='view_category'),
    path('view_budget/<int:id>', views.view_budget, name='view_budget'),
]