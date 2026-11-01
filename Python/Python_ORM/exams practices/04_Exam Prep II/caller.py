import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
from populate_db import populate_model_with_data
# Import your models here
from main_app.models import Profile, Product, Order
from django.db.models import Count, Q, F, Sum


# Create queries within functions
def populate_db():
    populate_model_with_data(Profile)
    populate_model_with_data(Product)
    populate_model_with_data(Order)

def get_profiles(search_string=None) ->str:
    result_objects = (Profile.objects
                       .annotate(num_of_orders=Count('order'))
                       .filter(Q(full_name__icontains=search_string)
                               |
                               Q(email__icontains=search_string)
                               |
                               Q(phone_number__icontains=search_string))
                       .order_by('full_name')
                       )
    if not result_objects.exists():
        return ""
    return '\n'.join(f"Profile: {ro.full_name},"
                     f" email: {ro.email},"
                     f" phone number: {ro.phone_number},"
                     f" orders: {ro.num_of_orders}"
                     for ro in result_objects
                     )


def get_loyal_profiles() ->str:
    profile_objects = Profile.objects.get_regular_customers()
    if not profile_objects.exists():
        return ""
    return '\n'.join(f"Profile: {p.full_name},"
                     f" orders: {p.number_of_orders}"
                     for p in profile_objects
                     )


def get_last_sold_products() ->str:
    order_object = Order.objects.last()

    if order_object is None:
        return ""
    last_order_products = order_object.products.order_by('name')

    if not last_order_products.exists():
        return ""

    return f"Last sold products: " + ', '.join(o.name for o in last_order_products)


def get_top_products() ->str:
    product_sets = (Product.objects
                    .annotate(num_orders=Count('order'))
                    .order_by('-num_orders', 'name')
                    )[:5]
    if not product_sets.exists():
        return ""

    return (f"Top products:\n" +
            f"\n".join(f"{p.name}, sold {p.num_orders} times"
            for p in product_sets))


def apply_discounts() ->str:
    num_of_updated_orders = (Order.objects
                  .annotate(count_products=Count('products'))
                  .filter(count_products__gt=2, is_completed=False)
                  .update(total_price=F('total_price') * 0.9)
                  )

    return f"Discount applied to {num_of_updated_orders} orders."

def complete_order() ->str:
    first_order = (Order.objects
                   .filter(is_completed=False)
                   .first()
                   )
    if first_order is None:
        return ""

    for product in first_order.products.all():
        product.in_stock -= 1
        if product.in_stock == 0:
            product.is_available = False
        product.save()
    first_order.is_completed = True
    first_order.save()
    return f"Order has been completed!"



