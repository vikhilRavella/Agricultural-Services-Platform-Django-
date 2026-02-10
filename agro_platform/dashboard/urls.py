from django.urls import path
from . import views

urlpatterns = [
    # PLATFORM PAGES (public / overview)
    path('farmer/', views.farmer_platform, name='farmer_platform'),
    path('supplier/', views.supplier_platform, name='supplier_platform'),
    path('provider/', views.provider_platform, name='provider_platform'),

    # DASHBOARDS (logged-in users)
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('supplier/dashboard/', views.supplier_dashboard, name='supplier_dashboard'),
    path('provider/dashboard/', views.provider_dashboard, name='provider_dashboard'),

    path('farmer/fertilizers/', views.farmer_fertilizers, name='farmer_fertilizers'),
    path('farmer/equipment/', views.farmer_equipment, name='farmer_equipment'),
    path('farmer/workers/', views.farmer_workers, name='farmer_workers'),
    path('farmer/schedule/', views.farmer_schedule, name='farmer_schedule'),
    path('supplier/products/', views.supplier_products, name='supplier_products'),
    path('supplier/orders/', views.supplier_orders, name='supplier_orders'),
    path('supplier/inventory/', views.supplier_inventory, name='supplier_inventory'),
    path('supplier/regions/', views.supplier_regions, name='supplier_regions'),
    path('provider/equipment/', views.provider_equipment, name='provider_equipment'),
    path('provider/workers/', views.provider_workers, name='provider_workers'),
    path('provider/schedule/', views.provider_schedule, name='provider_schedule'),
    path('provider/earnings/', views.provider_earnings, name='provider_earnings'),
]


