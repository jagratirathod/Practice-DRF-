from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "Create random user"

    def add_arguments(self,parser):
        parser.add_argument('total',type=int)
        # Optional argument
        parser.add_argument('-p','--prefix',type=str)
    
    def handle(self,*args,**kwargs):
        total = kwargs['total']
        prefix = kwargs['prefix']

        for i in range(total):
            if prefix:
                username = '{prefix}{random_string}'.format(prefix=prefix, random_string=get_random_string(total))
            else:
                username = get_random_string(total)
            user = User.objects.create_user(username=username,email="",password="123")
            self.stdout.write("created user - %s" % user)








        