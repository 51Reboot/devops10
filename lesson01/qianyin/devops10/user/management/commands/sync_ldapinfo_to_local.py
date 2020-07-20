from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "从ldap同步数据到本地db"

    def add_arguments(self, parser):
        """
        Entry point for subclassed commands to add custom arguments.
        """
        parser.add_argument('-u', '--username', type=str, help='指定用户邮箱账号')

    def handle(self, *args, **options):
        """
        The actual logic of the command. Subclasses must implement
        this method.
        """
        print(args)
        print(options)
        if options.get('username'):
            #  自定义控制台输出的内容
            self.stdout.write(
                self.style.SUCCESS(
                    '{} Successfully {}'.format(
                        '接受成功',
                        options['username']
                    )
                )
            )
