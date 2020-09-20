def send_mail(publish_name, action):
    print("[{}]----send-[{}]--mail ----".format(action, publish_name))



def publisher_notice_to_dept(sender, **kwargs):
    '''
    新增一个出版社之前我要发送一封通知邮件
    :param sender:
    :param kwargs:
    :return:
    '''
    # print('sender: -----------', sender)
    # print('kwargs: -----------', kwargs)
    print(kwargs)
    instance = kwargs['instance']
    send_mail(instance, 'create')


def publisher_notice_to_dept_delete(sender, **kwargs):
    '''
    新增一个出版社之前我要发送一封通知邮件
    :param sender:
    :param kwargs:
    :return:
    '''
    # print('sender: -----------', sender)
    # print('kwargs: -----------', kwargs)
    instance = kwargs['instance']
    send_mail(instance, 'delete')


def m2m_signal_handler(sender, instance, **kwargs):
    # print(sender)
    # print(instance) # 新增的对象
    # print(kwargs)   # 'created': True 、False
    if kwargs['action'] == 'post_add':
        pk_set = kwargs['pk_set']
        from user.models import UserProfile
        users = UserProfile.objects.filter(pk__in=list(pk_set))
        print('变化的用户列表: {}'.format(users))