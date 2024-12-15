from django.contrib.auth.models import Permission

class AdministratorPermissions(Permission):
    permissions = [
        Permission('view', Permission.VIEW_STYLE, 'Администратор может просматривать любую информацию.'),
        Permission('change', Permission.CHANGE_STATUS, 'Администратор может менять статус записи.'),
        Permission('delete', Permission.DELETE, 'Администратор может удалять записи.'),
        Permission('create', Permission.CREATE, 'Администратор может создавать записи.'),
        Permission('edit', Permission.EDIT, 'Администратор может редактировать записи.'),
    ]

    def has_permission(self, user):
        if user.is_superuser:
            return True
        elif user.groups.filter(lambda group: group == self.group()).exists():
            return True
        else:
            return False