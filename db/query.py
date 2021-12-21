import os, sys

import pytz
from pytz import UTC

sys.path.append(r'C:\Users\tcyganov_sa\PycharmProjects\untitled6\Django\Course')
os.environ['DJANGO_SETTINGS_MODULE'] = 'coursera.settings'
import django
from django.db.models import Q, Count, Avg, Sum
django.setup()
from db.models import User, Blog, Topic
from datetime import datetime


def create():
    date = datetime(2017, 1, 1, tzinfo=pytz.UTC)

    u1 = User.objects.create(first_name='u1', last_name='u1')
    u2 = User.objects.create(first_name='u2', last_name='u2')
    u3 = User.objects.create(first_name='u3', last_name='u3')

    blog1 = Blog.objects.create(title='blog1', author=u1)
    blog2 = Blog.objects.create(title='blog2', author=u1)

    blog1.subscribers.add(u1, u2)
    blog2.subscribers.add(u2)

    topic1 = Topic.objects.create(title='topic1', blog=blog1, author=u1)
    topic2 = Topic.objects.create(title='topic2', blog=blog1, author=u3, created=date)
    topic1.likes.add(u1, u2, u3)


def edit_all():
    User.objects.all().update(first_name='uu1')


def edit_u1_u2():
    User.objects.filter(Q(first_name='u1') | Q(first_name='u2')).update(first_name='uu1')


def delete_u1():
    User.objects.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    u = User.objects.get(first_name='u2')
    b = Blog.objects.filter(subscribers__first_name='u2')
    for i in b:
        i.subscribers.remove(u)


def get_topic_created_grated():
    date = datetime(2018, 1, 1, tzinfo=pytz.UTC)
    res = Topic.objects.filter(created__gt=date)
    return res


def get_topic_title_ended():
    res = Topic.objects.filter(title__endswith='content')
    return res


def get_user_with_limit():
    res = User.objects.order_by('-id')[0:2]
    return res


def get_topic_count():
    topic_count = Blog.objects.values('title').annotate(count=Count('topic__title', distinct=True)).order_by('count')
    return topic_count


def get_avg_topic_count():
    res = Blog.objects.annotate(topic_count=Count('topic')).aggregate(avg=Avg('topic_count'))
    return res


def get_blog_that_have_more_than_one_topic():
    res = Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gt = 1)
    return res


def get_topic_by_u1():
    res = Topic.objects.filter(author__first_name='u1')
    return res


def get_user_that_dont_have_blog():
    res = User.objects.exclude(blog__author=User.objects.all()).order_by('id')
    return res


def get_topic_that_like_all_users():
    user = User.objects.count()
    res = Topic.objects.annotate(count_likes=Count('likes')).filter(count_likes = user)
    return res

def get_topic_that_dont_have_like():
    res = Topic.objects.exclude(likes=User.objects.all())
    return res



    # 13. Найти топики, у которых нет лайков (функция get_topic_that_dont_have_like).




if __name__ == '__main__':
    # t = Topic.objects.all()
    # t.delete()
    # b = Blog.objects.all()
    # b.delete()
    # a = User.objects.all()
    # a.delete()
    # User.objects.filter(pk=31).update(first_name='u1')
    # User.objects.filter(pk=32).update(first_name='u2')
    # User.objects.filter(pk=33).update(first_name='u3')
    # edit_u1_u2()
    # blog1 = Blog.objects.get(title='blog1')
    # # blog2 = Blog.objects.get(title='blog2')
    # u1 = User.objects.get(first_name='u1')
    # # u2 = User.objects.get(first_name='u2')
    # # blog1.subscribers.add(u1, u2)
    # # blog2.subscribers.add(u2)
    # # unsubscribe_u2_from_blogs()
    # topic1 = Topic.objects.create(title='content topik', author=u1, blog=blog1)
    print(get_topic_that_like_all_users())