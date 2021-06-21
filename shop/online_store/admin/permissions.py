class CreationRestrictMixin:

    def has_add_permission(self, request, obj=None):
        return False


class DeleteRestrictionMixin:

    def has_delete_permission(self, request, obj=None):
        return False
