from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .decorators import role_required, demo_block_post

# DB MODELS (real users)
from services.models import (
    Fertilizer, Equipment, Worker,
    Product, Order,
    ProviderEquipment, ProviderWorker
)

# DEMO DATA
from dashboard.demo_data import (
    FERTILIZERS,
    EQUIPMENT,
    WORKERS,
    PRODUCTS,
    ORDERS,
    PROVIDER_EQUIPMENT,
    PROVIDER_WORKERS,
    EARNINGS
)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorators import role_required, demo_block_post

# ---------------- HOME ----------------
def home(request):
    return render(request, 'home.html', {
        'demo': request.session.get('demo', False)
    })

# ---------------- DASHBOARDS ----------------
@login_required
@role_required('farmer')
def farmer_dashboard(request):
    return render(request, 'dashboard/farmer_dashboard.html')

@login_required
@role_required('supplier')
def supplier_dashboard(request):
    return render(request, 'dashboard/supplier_dashboard.html')

@login_required
@role_required('provider')
def provider_dashboard(request):
    return render(request, 'dashboard/provider_dashboard.html')

# ---------------- PLATFORM (PUBLIC) ----------------
def farmer_platform(request):
    return render(request, 'platform/farmer.html', {'demo': request.session.get('demo')})

def supplier_platform(request):
    return render(request, 'platform/supplier.html', {'demo': request.session.get('demo')})

def provider_platform(request):
    return render(request, 'platform/provider.html', {'demo': request.session.get('demo')})


# ================= FARMER =================
@demo_block_post
@role_required("farmer")
def farmer_fertilizers(request):
    demo = request.session.get("demo")
    data = FERTILIZERS if demo else Fertilizer.objects.all()
    return render(request, "platform/farmer_platform/farmer_fertilizers.html", {
        "fertilizers": data,
        "demo": demo
    })


@demo_block_post
@role_required("farmer")
def farmer_equipment(request):
    demo = request.session.get("demo")
    data = EQUIPMENT if demo else Equipment.objects.filter(available=True)
    return render(request, "platform/farmer_platform/farmer_equipment.html", {
        "equipment": data,
        "demo": demo
    })


@demo_block_post
@role_required("farmer")
def farmer_workers(request):
    demo = request.session.get("demo")
    data = WORKERS if demo else Worker.objects.all()
    return render(request, "platform/farmer_platform/farmer_workers.html", {
        "workers": data,
        "demo": demo
    })
@demo_block_post
@role_required("farmer")
def farmer_schedule(request):
    """
    Farmer service scheduling page
    Demo: view only
    Real user: future POST logic
    """
    return render(
        request,
        "platform/farmer_platform/farmer_schedule.html",
        {
            "demo": request.session.get("demo", False)
        }
    )


# ================= SUPPLIER =================
@demo_block_post
@role_required("supplier")
def supplier_products(request):
    demo = request.session.get("demo")
    data = PRODUCTS if demo else Product.objects.filter(supplier=request.user)
    return render(request, "platform/supplier_platform/supplier_products.html", {
        "products": data,
        "demo": demo
    })


@demo_block_post
@role_required("supplier")
def supplier_orders(request):
    demo = request.session.get("demo")
    data = ORDERS if demo else Order.objects.filter(supplier=request.user)
    return render(request, "platform/supplier_platform/supplier_orders.html", {
        "orders": data,
        "demo": demo
    })
@demo_block_post
@role_required("supplier")
def supplier_inventory(request):
    demo = request.session.get("demo", False)

    if demo:
        products = PRODUCTS   # demo_data
    else:
        products = Product.objects.filter(supplier=request.user)

    return render(
        request,
        "platform/supplier_platform/supplier_inventory.html",
        {
            "products": products,
            "demo": demo
        }
    )
@role_required("supplier")
def supplier_regions(request):
    """
    Static informational page
    Demo + real users can view
    """
    return render(
        request,
        "platform/supplier_platform/supplier_regions.html",
        {
            "demo": request.session.get("demo", False)
        }
    )



# ================= PROVIDER =================
@demo_block_post
@role_required("provider")
def provider_equipment(request):
    demo = request.session.get("demo")
    data = PROVIDER_EQUIPMENT if demo else ProviderEquipment.objects.filter(provider=request.user)
    return render(request, "platform/provider_platform/provider_equipment.html", {
        "equipment": data,
        "demo": demo
    })


@demo_block_post
@role_required("provider")
def provider_workers(request):
    demo = request.session.get("demo")
    data = PROVIDER_WORKERS if demo else ProviderWorker.objects.filter(provider=request.user)
    return render(request, "platform/provider_platform/provider_workers.html", {
        "workers": data,
        "demo": demo
    })


@role_required("provider")
def provider_earnings(request):
    demo = request.session.get("demo")
    data = EARNINGS if demo else {}
    return render(request, "platform/provider_platform/provider_earnings.html", {
        "earnings": data,
        "demo": demo
    })
@demo_block_post
@role_required("provider")
def provider_schedule(request):
    """
    Provider booking schedule
    Demo: view only
    """
    return render(
        request,
        "platform/provider_platform/provider_schedule.html",
        {
            "demo": request.session.get("demo", False)
        }
    )
def demo_login(request):
    request.session.flush()        # clear auth + old session
    request.session['demo'] = True
    return redirect('/')           # ✅ go to HOME, not login
