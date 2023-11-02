from rest_framework.permissions import BasePermission


class IsOwnerOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        """
        Проверка, является ли пользователь создателем привычки или администратором
        :param request: Запрос
        :param view: Контроллер
        :return: Bool
        """
        if request.user.is_superuser:
            return True
        return request.user == view.get_object().owner
