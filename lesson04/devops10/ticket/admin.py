from django.contrib import admin

# Register your models here.
from .models import Classify
from .models import History
from .models import TplInfo
from .models import TplData
from .models import WorkOrderInfo
from .models import TaskInfo
from .models import CirculationHistory
from .models import Info


class ClassifyAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "create_user",
        "create_time",
        "update_time",
    )


class HistoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "task_type",
        "execute_time",
        "result",
        "create_time",
        "update_time",
    )


class TplInfoAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "form_structure",
        "create_user",
        "remarks",
        "create_time",
        "update_time",
    )


class TplDataAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "form_structure",
        "form_data",
        "create_time",
        "update_time",
    )


class WorkOrderInfoAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "priority",
        "process",
        "classify",
        "IsEnd",
        "IsDenied",
        "state",
        "related_person",
        "create_user",
        "urge_count",
        "urge_last_time",
        "create_time",
        "update_time",
    )


class TaskInfoAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "task_type",
        "content",
        "create_user",
        "remarks",
        "create_time",
        "update_time",
    )


class CirculationHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "work_order",
        "state",
        "source",
        "target",
        "circulation",
        "processor",
        "processor_id",
        "cost_duration",
        "remarks",
        "create_time",
        "update_time",
    )


class InfoAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "structure",
        "classify",
        "tpls",
        "task",
        "submit_count",
        "create_user",
        "notice",
        "create_time",
        "update_time",
    )


admin.site.register(Classify, ClassifyAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(TplInfo, TplInfoAdmin)
admin.site.register(TplData, TplDataAdmin)
admin.site.register(WorkOrderInfo, WorkOrderInfoAdmin)
admin.site.register(TaskInfo, TaskInfoAdmin)
admin.site.register(CirculationHistory, CirculationHistoryAdmin)
admin.site.register(Info, InfoAdmin)
