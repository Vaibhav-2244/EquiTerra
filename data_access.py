# import os
# import django

# # ✅ Set your Django settings module
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpulRent.settings')  # replace 'OpulRent' if you renamed it

# # ✅ Setup Django
# django.setup()

# # Now safely import your models
# from django.contrib.auth.models import User
# from users.models import UserProfile  # adjust path if needed

# user = User.objects.get(username="vaibhav@gmail.com")
# UserProfile.objects.create(user=user, wallet_address="45b8729250f2f6f7052dff47013c3c30d3ad0e4f0bab2e91404082fa613856c9")
# print(user.email)
# print(user.userprofile.wallet_address)

# import os
# import django

# # ✅ Set Django settings
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpulRent.settings')
# django.setup()

# # ✅ Import your models
# from django.contrib.auth.models import User
# from users.models import UserProfile
# from property.models import PropertyForSale, PropertyForRent

# # ✅ Get the user and ensure profile exists
# user = User.objects.get(username="ksjdblihsdbfds@gmail.com")
# UserProfile.objects.get_or_create(user=user, defaults={
#     'wallet_address': '45b8729250f2f6f7052dff47013c3c30d3ad0e4f0bab2e91404082fa613856c9'
# })

# # ✅ Print user data
# print("User Email:", user.email)
# print("Wallet Address:", user.userprofile.wallet_address)

# # ✅ Print properties for sale
# print("\n🏠 Properties for Sale:")
# for prop in PropertyForSale.objects.all():
#     print(f"{prop.house_type} in {prop.locality}, {prop.city}")
#     print(f"  Total Units: {prop.total_units}, Units Sold: {prop.units_sold}")
#     print(f"  Sale Price: {prop.sale_price} ETH, Price/Unit: {prop.unit_price:.2f} ETH")

# # ✅ Print properties for rent
# print("\n🏠 Properties for Rent:")
# for prop in PropertyForRent.objects.all():
#     print(f"{prop.house_type} in {prop.locality}, {prop.city}")
#     print(f"  Rent: {prop.rent} ETH/month")


import os
import django

# ✅ Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpulRent.settings')
django.setup()

# ✅ Import models
from django.contrib.auth.models import User
from users.models import UserProfile
from property.models import PropertyForSale, PropertyForRent
from dashboard.models import Transaction

# ✅ Get the user and ensure UserProfile exists
user = User.objects.get(username="ksjdblihsdbfds@gmail.com")
UserProfile.objects.get_or_create(user=user, defaults={
    'wallet_address': '45b8729250f2f6f7052dff47013c3c30d3ad0e4f0bab2e91404082fa613856c9'
})

print("User Email:", user.email)
print("Wallet Address:", user.userprofile.wallet_address)

# ✅ Properties listed for sale by the user
print("\n🏠 Properties LISTED FOR SALE by user:")
sale_listings = PropertyForSale.objects.filter(owner=user)
for prop in sale_listings:
    print(f"{prop.house_type} in {prop.locality}, {prop.city}")
    print(f"  Units Available: {prop.units_available}, Price/Unit: {prop.unit_price:.2f} ETH")

# ✅ Properties listed for rent by the user
print("\n🏠 Properties LISTED FOR RENT by user:")
rent_listings = PropertyForRent.objects.filter(owner=user)
for prop in rent_listings:
    print(f"{prop.house_type} in {prop.locality}, {prop.city}")
    print(f"  Rent: {prop.rent} ETH/month")

# ✅ Properties bought by the user (Transaction record)
print("\n🛒 Properties BOUGHT by user:")
bought = Transaction.objects.filter(buyer=user, transaction_type='sale')
for tx in bought:
    print(f"{tx.property_sale.house_type} in {tx.property_sale.locality}, {tx.property_sale.city}")
    print(f"  Units Bought: {tx.units}, Total Paid: {tx.amount} ETH")

# ✅ Properties rented by the user (optional)
print("\n🏠 Properties RENTED by user:")
rented = Transaction.objects.filter(buyer=user, transaction_type='rent')
for tx in rented:
    print(f"{tx.property_rent.house_type} in {tx.property_rent.locality}, {tx.property_rent.city}")
    print(f"  Monthly Rent: {tx.amount} ETH")

# ✅ (Optional) Show properties in a specific city, e.g., Mumbai
print("\n🏙️ All Properties FOR SALE in Mumbai:")
mumbai_sale = PropertyForSale.objects.filter(city="Mumbai")
for prop in mumbai_sale:
    print(f"{prop.house_type} in {prop.locality} - {prop.unit_price:.2f} ETH/unit")

