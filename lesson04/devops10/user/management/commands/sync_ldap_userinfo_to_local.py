from django.core.management.base import BaseCommand

import requests


class Command(BaseCommand):
    """
    Sync Ldap UserInfo to Local database.
    """
    help = "sync ldap user info to local database."

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', type=str, help='指定用户邮箱账号')

    def handle(self, *args, **options):
        # print(args)
        # print(options)
        if options.get('username'):
            print("同步{}单条数据".format(options.get('username')))

            req = requests.get(url='ldap url', params={'username' : ''})
            if req.ok and req.status_code == 200:
                jsondata = req.json()
                # 把数据取出来之后保存到本地的数据 orm.save

            # 可以自定制在控制台输出的内容
            self.stdout.write(
                self.style.SUCCESS(
                    '{} Successfully {}'.format(
                        '接收成功',
                        options['username'])))
        else:
            print("同步全量数据")