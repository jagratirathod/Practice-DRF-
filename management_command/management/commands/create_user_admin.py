from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from  django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create user"
    
    def add_arguments(self, parser):
        parser.add_argument('total',type=int)
        parser.add_argument('-p','--prefix' , type=str)
        parser.add_argument('-a', '--admin' , action='store_true')

    def handle(self, *args,**kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']
        admin = kwargs['admin']

        for i in range(total):
            if prefix:
                username = '{prefix}_{random_string}'.format(
                            prefix=prefix,random_string=get_random_string(total))
            else:
                username = get_random_string(10)
            if admin:
                user=User.objects.create_superuser(username=username, email="" 
                                                   , password="123")
            else:
                user=User.objects.create_user(username = username, email=""
                                              , password="123")
            self.stdout.write("created user - %s" % user)

    








