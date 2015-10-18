# -*- coding: utf-8 -*-

from zhihu import Question
from zhihu import User
from zhihu import Answer
from zhihu import Search

def user_test(user_url):
    user = User(user_url)
    # 获取用户ID
    user_id = user.get_user_id()
    # 获取该用户的关注者人数
    followers_num = user.get_followers_num()
    # 获取该用户关注的人数
    followees_num = user.get_followees_num()
    # 获取该用户提问的个数
    asks_num = user.get_asks_num()
    # 获取该用户回答的个数
    answers_num = user.get_answers_num()
    # 获取该用户收藏夹个数
    collections_num = user.get_collections_num()
    # 获取该用户获得的赞同数
    agree_num = user.get_agree_num()
    # 获取该用户获得的感谢数
    thanks_num = user.get_thanks_num()

    # 获取该用户关注的人
    followees = user.get_followees()
    # 获取关注该用户的人
    followers = user.get_followers()
    # 获取该用户提的问题
    asks = user.get_asks()
    # 获取该用户回答的问题的答案
    answers = user.get_answers()
    # 获取该用户的收藏夹
    collections = user.get_collections()

    print user_id  # 黄继新
    print followers_num  # 614840
    print followees_num  # 8408
    print asks_num  # 1323
    print answers_num  # 786
    print collections_num  # 44
    print agree_num  # 46387
    print thanks_num  # 11477

    print followees
    # <generator object get_followee at 0x7ffcac3af050>
    # 代表所有该用户关注的人的生成器对象
    i = 0
    for followee in followees:
        print followee.get_user_id()
        i = i + 1
        if i == 41:
            break

    print followers
    # <generator object get_follower at 0x7ffcac3af0f0>
    # 代表所有关注该用户的人的生成器对象
    i = 0
    for follower in followers:
        print follower.get_user_id()
        i = i + 1
        if i == 41:
            break

    print asks
    # <generator object get_ask at 0x7ffcab9db780>
    # 代表该用户提的所有问题的生成器对象
    print answers
    # <generator object get_answer at 0x7ffcab9db7d0>
    # 代表该用户回答的所有问题的答案的生成器对象
    print collections
    # <generator object get_collection at 0x7ffcab9db820>
    # 代表该用户收藏夹的生成器对象


def main():
    user_url = "http://www.zhihu.com/people/jixin"
    user_test(user_url)

if __name__ == '__main__':
    main()