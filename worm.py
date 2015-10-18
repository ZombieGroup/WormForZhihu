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
        cursor.execute("insert into Questions values(%s, %s, %s, %d, %d)" % id,'00000000' , detail, title, answer_num, followers_num)
        for topic in topics:
            topic_id = topic.get_topic_id
            cursor.execute("insert into Question_Topics values(%s, %s)" % )
        cursor.close()
        self.connect.commit()

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
        cursor.execute("insert into answers values(%s, %s, %s, %s, %d, %d)" % id, question_id, author_id, detail, upvote,visit_times)
        cursor.close()
        self.connect.commit()

    def put_user_in_db(self, user):
        cursor = self.connect.cursor()
        user_id = user.get_user_id()
        follower_num = user.get_followers_num()
        followee_num = user.get_followees_num()
        agree_num = user.get_agree_num()
        thanks_num = user.get_thanks_num()
        ask_num = user.get_asks_num()
        answer_num = user.get_answers_num()
        collection_num = user.get_collections_num()
        cursor.execute("insert into users values(%s, %d, %d, %d, %d, %d, %d)" % user_id, follower_num, followee_num, agree_num, thanks_num, ask_num, answer_num,collection_num)

        # for the Tables besides User
        asks = user.get_asks()
        followers = user.get_followers()
        collections = user.get_collections()
        for question in asks:
            quesiton_id = question.get_question_id()
            cursor.execute("update questions set asker_ID=%s where question_id=%d"% user_id, quesiton_id)
        for user in followers:
            follower_id = user.get_user_id()
            cursor.execute("insert into follow_user values(%s, %s)" % follower_id, user_id)
        for collection in collections:
            collection_name = collection.get_name()
            cursor.execute("insert into collection value(%s, %s)" % collection_name, user_id)
        cursor.close()
        self.connect.commit()

    def put_collection_in_db(self, collection):
        cursor = self.connect.cursor()
        name = collection.get_name()
        answers = collection.get_all_answers()
        for answer in answers:
            answer_id = answer.get_answer_id()
            cursor.execute("insert into Collection_Answers values(%s, %s)" % name, answer_id)
        cursor.close()
        self.connect.commit()


