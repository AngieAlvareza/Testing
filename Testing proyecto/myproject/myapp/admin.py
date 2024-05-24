
from django.contrib import admin
from .models import Proveedor, Producto, Abastecimiento, Factura, DetalleFactura, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# Define un nuevo admin para el modelo de usuario
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Abastecimiento)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(UserProfile)

