from profile_app.models import User
import os

def create_first_user():
    user = os.getenv('FIRST_USER').split(' ');
    username, password = user

    try:
        u = User.objects.get(username=username)
        u.user_type = User.User_Type.AD
        u.set_password(password)
        u.save()
    except User.DoesNotExist:
        u = User.objects.create(username=username, user_type=User.User_Type.AD)
        u.set_password(password)
        print('created first_user')
        u.save()


if __name__ == '__main__':
    create_first_user()
