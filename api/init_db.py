# Example: Query all customers
from api.models import Customer
customers = Customer.query.all()