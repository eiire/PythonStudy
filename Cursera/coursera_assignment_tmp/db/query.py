from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from .models import User, Blog, Topic


def create():
    user_1 = User(first_name='u1', last_name='u1')
    user_2 = User(first_name='u2', last_name='u2')
    user_3 = User(first_name='u3', last_name='u3')

    user_1.save()
    user_2.save()
    user_3.save()

    blog_1 = Blog(title='blog1', author=user_1)
    blog_2 = Blog(title='blog2', author=user_1)

    blog_1.save()
    blog_2.save()

#     Подписать пользователей u1 u2 на blog1, u2 на blog2.
    blog_1.subscribers.add(user_1, user_2)
    blog_2.subscribers.add(user_2)

#     Создать топик title = topic1, blog = blog1, author = u1.
    topic_1 = Topic(title='topic1', blog=blog_1, author=user_1)
    topic_1.save()
#     Создать топик title = topic2_content, blog = blog1, author = u3, created = 2017-01-01.
    topic_2 = Topic(title='topic2_content', blog=blog_1, author=user_3, created='2017-01-01')
    topic_2.save()
#     Лайкнуть topic1 пользователями u1, u2, u3.
    topic_1.likes.add(user_2, user_1, user_3)
    # return topic_1


def edit_all():
    all_users = User.objects.all()
    for user in all_users:
        user.first_name = 'uu1'
        user.save()
    # return all_users


def edit_u1_u2():
    all_users = User.objects.all()
    for user in all_users:
        if user.first_name == 'u1' or user.first_name == 'u2':
            user.first_name = 'uu1'
            user.save()


def delete_u1():
    all_users = User.objects.all()
    for user in all_users:
        if user.first_name == 'u1':
            user.delete()


# отписать пользователя с first_name u2 от блогов
def unsubscribe_u2_from_blogs():
    # Нашел все блоги с данным пользователем
    this_user = User.objects.filter(first_name='u2')[0]  # !QS! -->obj[0]
    all_blogs = list(Blog.objects.filter(subscribers=this_user).all())  # !QS! --> list

    for blog in all_blogs:
        blog.subscribers.remove(this_user)


# Найти топики у которых дата создания больше 2018-01-01
def get_topic_created_grated():
    return Topic.objects.filter(created__gte='2018-01-01')


# Найти топик у которого title заканчивается на content
def get_topic_title_ended():
    return Topic.objects.filter(title__endswith='content')


# Получить 2х первых пользователей (сортировка в обратном порядке по id)
def get_user_with_limit():
    return User.objects.order_by('-pk')[:2]


#  Получить количество топиков в каждом блоге, назвать поле topic_count, отсортировать по topic_count по возрастанию
def get_topic_count():
    return Blog.objects.all().annotate(topic_count=Count('topic')).order_by('topic_count')



def get_avg_topic_count():
    return Blog.objects.all().annotate(topic_count=Count('topic')).order_by('topic_count')


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
