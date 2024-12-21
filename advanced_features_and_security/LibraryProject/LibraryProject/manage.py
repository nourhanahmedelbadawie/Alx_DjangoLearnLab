#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.contrib.auth.models import Group, Permission
from myapp.models import Book

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# Create groups
admin_group, created = Group.objects.get_or_create(name='Admins')
editor_group, created = Group.objects.get_or_create(name='Editors')
viewer_group, created = Group.objects.get_or_create(name='Viewers')

# Assign permissions to groups
view_permission = Permission.objects.get(codename='can_view', content_type__model='book')
create_permission = Permission.objects.get(codename='can_create', content_type__model='book')
edit_permission = Permission.objects.get(codename='can_edit', content_type__model='book')
delete_permission = Permission.objects.get(codename='can_delete', content_type__model='book')

admin_group.permissions.add(view_permission, create_permission, edit_permission, delete_permission)
editor_group.permissions.add(create_permission, edit_permission)
viewer_group.permissions.add(view_permission)
