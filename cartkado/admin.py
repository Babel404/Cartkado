"""
admin
undeuxtroissoleil
"""

from django.contrib import admin
from .models import Cartkado, Transaction

admin.site.register(Cartkado)
admin.site.register(Transaction)
