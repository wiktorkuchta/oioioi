from django.utils.translation import ugettext_lazy as _

from oioioi.base.menu import MenuRegistry, side_pane_menus_registry

teacher_menu_registry = MenuRegistry(_("Teacher Menu"),
    lambda request: request.user.has_perm('teachers.teacher'))
side_pane_menus_registry.register(teacher_menu_registry, order=50)
