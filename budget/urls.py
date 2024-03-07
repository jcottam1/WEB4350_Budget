from . import views
from django.urls import path

app_name = "budget"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.dashboard, name='dashboard'),
    path('budget/', views.budget, name='budget'),
    path('report/', views.reports, name='reports'),
    path('transactions/', views.transactions, name='transactions'),
    path('make_budget/', views.make_budget, name="make-budget"),
    path('make_category/<int:id>', views.make_category, name="make-category"),
    path('make_label/<int:id>', views.make_label, name="make-label"),
    path('make-month', views.make_month, name='make-month'),
    path('make_transaction/', views.make_transaction, name="make_transaction"),
    path('view_category/<int:id>', views.view_category, name='view_category'),
    path('view_budget/<int:id>', views.view_budget, name='view_budget'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('delete/<int:id>', views.delete_category, name="delete_category"),
    path('edit_budget/<int:id>', views.edit_budget, name='edit_budget'),
    path('delete_budget/<int:id>', views.delete_budget, name='delete_budget'),
    path('edit_label/<int:id>', views.edit_label, name='edit_label'),
    path('delete_label/<int:id>', views.delete_label, name='delete_label'),
    path('edit_transaction/<int:id>', views.edit_transaction, name='edit_transaction'),
    path('delete_transaction/<int:id>', views.delete_transaction, name='delete_transaction')
]
