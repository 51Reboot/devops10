from django.db import models
import jsonfield

# Create your models here.


# 基表
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="变更时间")

    class Meta:
        abstract = True


# 流程分类
class Classify(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='分类名称')
    create_user = models.CharField(max_length=32, verbose_name='创建者')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "p_process_classify"
        verbose_name_plural = verbose_name = '流程分类'


# 工单
class WorkOrderInfo(BaseModel):
    title = models.CharField(max_length=255, unique=True, verbose_name='工单标题')
    priority = models.CharField(max_length=255, unique=True, verbose_name='工单优先级 1，正常 2，紧急 3，非常紧急')
    process = models.CharField(max_length=255, unique=True, verbose_name='流程ID')
    classify = models.ForeignKey(to=Classify, on_delete=models.CASCADE, verbose_name="分类ID")
    IsEnd = models.IntegerField(default=0, verbose_name='是否结束， 0 未结束，1 已结束')
    IsDenied = models.IntegerField(default=0, verbose_name='是否被拒绝， 0 没有，1 有')
    state = jsonfield.JSONField(verbose_name='状态信息')
    related_person = jsonfield.JSONField(verbose_name='工单所有处理人')
    create_user = models.CharField(max_length=128, unique=True, verbose_name='创建者')

    urge_count = models.IntegerField(default=0, verbose_name='催办次数')
    urge_last_time = models.IntegerField(default=0, verbose_name='上一次催促时间')

    class Meta:
        db_table = "p_work_order_info"
        verbose_name_plural = verbose_name = '工单'


# 任务
class History(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='任务名称')
    task_type = models.CharField(max_length=100, unique=True, verbose_name='任务类型, python, shell')
    execute_time = models.CharField(max_length=128, unique=True, verbose_name='执行时间')
    result = models.CharField(max_length=250, unique=True, verbose_name='执行结果')

    class Meta:
        db_table = "p_task_history"
        verbose_name_plural = verbose_name = '历史'


# 模板 -> 模板管理
class TplInfo(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='模板名称')
    form_structure = jsonfield.JSONField(verbose_name='表单结构')
    create_user = models.CharField(max_length=128, unique=True, verbose_name='创建者')
    remarks = models.CharField(max_length=250, unique=True, verbose_name='备注')

    class Meta:
        db_table = "p_tpl_info"
        verbose_name_plural = verbose_name = '模板管理'


# 工单绑定模版数据
class TplData(BaseModel):
    form_structure = jsonfield.JSONField(verbose_name='表单结构')
    form_data = models.CharField(max_length=128, unique=True, verbose_name='表单数据')

    class Meta:
        db_table = "p_work_order_tpl_data"
        verbose_name_plural = verbose_name = '工单绑定模版数据'


# 任务
class TaskInfo(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='任务名称')
    task_type = models.CharField(max_length=100, verbose_name='任务类型')
    content = models.CharField(max_length=255, verbose_name='任务内容')
    create_user = models.CharField(max_length=128, unique=True, verbose_name='创建者')
    remarks = models.CharField(max_length=250, unique=True, verbose_name='备注')

    class Meta:
        db_table = "p_task_info"
        verbose_name_plural = verbose_name = '任务'


# 工单流转历史
class CirculationHistory(BaseModel):
    title = models.CharField(max_length=255, unique=True, verbose_name='工单标题')
    work_order = models.ForeignKey(to=WorkOrderInfo, on_delete=models.CASCADE, verbose_name='工单ID')
    state = models.CharField(max_length=100, verbose_name='工单状态')
    source = models.CharField(max_length=100, verbose_name='源节点ID')
    target = models.CharField(max_length=100, verbose_name='目标节点ID')
    circulation = models.CharField(max_length=100, verbose_name='流转ID')
    processor = models.CharField(max_length=100, verbose_name='处理人')
    processor_id = models.CharField(max_length=100, verbose_name='处理人ID')
    cost_duration = models.CharField(max_length=100, verbose_name='处理时长')
    remarks = models.CharField(max_length=250, unique=True, verbose_name='备注')

    class Meta:
        db_table = "p_work_order_circulation_history"
        verbose_name_plural = verbose_name = '工单流转历史'


# 流程
class Info(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name='任务名称')
    structure = jsonfield.JSONField(verbose_name='流程结构')
    classify = models.ForeignKey(to=Classify, on_delete=models.CASCADE, verbose_name="分类ID")
    tpls = jsonfield.JSONField(verbose_name='模版')
    task = jsonfield.JSONField(verbose_name='模任务ID, array, 可执行多个任务，可以当成通知任务，每个节点都会去执行版')
    submit_count = models.IntegerField(default=0, verbose_name='提交统计')
    create_user = models.CharField(max_length=128, unique=True, verbose_name='创建者')
    notice = jsonfield.JSONField(verbose_name="绑定通知")

    class Meta:
        db_table = "p_process_info"
        verbose_name_plural = verbose_name = '流程'