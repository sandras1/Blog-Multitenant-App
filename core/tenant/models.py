from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import DomainMixin, TenantMixin


class Tenant(TenantMixin):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog_name = models.CharField(max_length=50)
    blog_image = models.ImageField(null=True, blank=True, upload_to="profile")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False, blank=True)
    created_on = models.DateField(auto_now_add=True)
    # default true, schema will be automatically created and
    # synced when it is saved
    auto_create_schema = True
    auto_drop_schema = True

    class Meta:
        def __str__(self):
            return f"{self.blog_name}"


class Domain(DomainMixin):
    pass
