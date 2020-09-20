from casbin import persist


class DjangoAdapter(persist.Adapter):
    """the interface for Casbin adapters."""

    def __init__(self, adapter_model):
        self.adapter_model = adapter_model

    def load_policy(self, model):
        """loads all policy rules from the storage."""
        for cr in self.adapter_model.objects.all():
            values = [x for x in cr.serializer().values() if x]
            # 'p, xiaoming, /api/v1/user/info, GET'
            persist.load_policy_line(', '.join(values), model)

    def save_policy(self, model):
        """saves all policy rules to the storage."""
        pass

    def add_policy(self, sec, ptype, rule):
        """adds a policy rule to the storage."""
        pass

    def remove_policy(self, sec, ptype, rule):
        """removes a policy rule from the storage."""
        pass

    def remove_filtered_policy(self, sec, ptype, field_index, *field_values):
        """removes policy rules that match the filter from the storage.
        This is part of the Auto-Save feature.
        """
        pass