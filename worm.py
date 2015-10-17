__author__ = 'wangzhaoyi'

import MySQLdb
from zhihu import Question
from zhihu import User
from zhihu import Collection
from zhihu import Search


class ConnectItem:
    def __init__(self,user=None, host=None, password=None, dbname=None):
        self.user = user
        self.host = host
        self.password = password
        self.dbname = dbname
    def getItem(self):
        return self.user, self.host, self.password, self.dbname
class PutInDB:
    connectItem = ConnectItem()
    connect = None
    def __init__(self, connectItem=None, user=None, host=None, password=None, dbname=None):
        if connectItem != None:
            self.connectItem = connectItem
        else:
            self.connectItem = ConnectItem(user, host, password, dbname)
        self.connect=MySQLdb.connect(connectItem.getItem(),port=3306)

    def put_question_in_db(self, question):
        cursor = self.connect.cursor()
        id = question.get_question_id()
        title = question.get_title()
        detail = question.get_detail()
        answer_num = question.get_answers_num()
        followers_num = question.get_followers_num()
        topics = question.get_topics()
        #answers = question.get_all_answers()
        cursor.execute("insert into Questions values(%s, %s, %s, %d, %d)" % id,'0000000000' , detail, title, answer_num, followers_num)
        for topic in topics:
            cursor.execute("instert into topic values(%s)" % topic)

    def put_answer_in_db(self, answer):
        cursor = self.connect.cursor()
        id = answer.get_answer_id()
        question = answer.get_question()
        question_id = question.get_question_id()
        author = answer.get_author()
        author_id = author.get_user_id()
        detail = answer.get_content()
        upvote = answer.get_upvote()
        visit_times = answer.get_visit_times()
        cursor.execute("inser in answers values(%s, %s, %s, %s, %d, %d)" % id, question_id, author_id, detail, upvote,visit_times)


    #to be continue~~~
    #def put_user_in_db(self, user):
