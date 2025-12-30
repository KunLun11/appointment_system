from unfold.admin import ModelAdmin


class BaseAdmin(ModelAdmin):
    list_per_page = 20
    save_on_top = True

    def get_list_display(self, request):
        base_list = ["__str__"]
        if hasattr(self.model, "created_at"):
            base_list.append("created_at")
        if hasattr(self.model, "updated_at"):
            base_list.append("updated_at")
        return base_list

    def get_readonly_fields(self, request, obj=None):
        readonly = list(super().get_readonly_fields(request, obj))
        if hasattr(self.model, "created_at"):
            readonly.append("created_at")
        if hasattr(self.model, "updated_at"):
            readonly.append("updated_at")
        return readonly
