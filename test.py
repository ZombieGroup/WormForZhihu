# -*- coding: utf-8 -*-

from zhihu import Question
from zhihu import User
from zhihu import Answer
from zhihu import Search

def question_test(url):
    question = Question(url)

    # 获取该问题的标题
    title = question.get_title()
    # 获取该问题的详细描述
    detail = question.get_detail()
    # 获取回答个数
    answers_num = question.get_answers_num()
    # 获取关注该问题的人数
    followers_num = question.get_followers_num()
    # 获取该问题所属话题
    topics = question.get_topics()
    # 获取该问题被浏览次数
    visit_times = question.get_visit_times()
    # 获取排名第一的回答
    top_answer = question.get_top_answer()
    # 获取排名前十的十个回答
    top_answers = question.get_top_i_answers(10)
    # 获取所有回答
    answers = question.get_all_answers()

    print title  # 输出：现实可以有多美好？
    print detail
    # 输出：
    # 本问题相对于“现实可以多残酷？传送门：现实可以有多残酷？
    # 题主：       昨天看了“现实可以有多残酷“。感觉不太好，所以我
    # 开了这个问题以相对应，希望能够“中和一下“。和那个问题题主不想
    # 把它变成“比惨大会“一样，我也不想把这个变成“鸡汤故事会“，或者
    # 是“晒幸福“比赛。所以大家从“现实，实际”的角度出发，讲述自己的
    # 美好故事，让大家看看社会的冷和暖，能更加辨证地看待世界，是此
    # 题和彼题共同的“心愿“吧。
    print answers_num  # 输出：2441
    print followers_num  # 输出：26910
    for topic in topics:
        print topic,  # 输出：情感克制 现实 社会 个人经历
    print visit_times  # 输出: 该问题当前被浏览的次数
    print top_answer  # 输出：<zhihu.Answer instance at 0x7f8b6582d0e0>(Answer类对象)
    print top_answers  # 输出：<generator object get_top_i_answers at 0x7fed676eb320>(代表前十的Answer的生成器)
    print answers

def searchTest(keyword, search_type):
    search = Search(keyword, search_type)
    if search_type is 'question':
        for question_url in search.getQuestions():
            question_test(question_url)
    elif search_type is 'people':
        peoples = search.getPeoples()
    elif search_type is 'topic':
        topics = search.getTopics()

def main():
    keyword = '屠呦呦'
    searchTest(keyword,'question')

if __name__ == '__main__':
    main()