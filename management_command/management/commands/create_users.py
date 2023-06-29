from django.core .management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = "Create random user"

    def add_arguments(self, parser):
        parser.add_argument('total',type=int)
    
    def handle(self,*args,**kwargs):
        total = kwargs['total']
        for i in range(total):
            user=User.objects.create_user(username = get_random_string(total), email = '' , password='123')
            self.stdout.write("created user - %s" % user)


