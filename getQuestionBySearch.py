#-*- coding:utf8 -*-
__author__ = 'wangzhaoyi'


import urllib2
import zhihu

import os, sys, time, platform, random
import re, json, cookielib

# requirements
import requests, termcolor, html2text
try:
    from bs4 import BeautifulSoup
except:
    import BeautifulSoup

# module
from auth import islogin
from auth import Logging

class Search:
    keyword = None
    search_type = None
    search_types = ('question', 'people', 'topic')
    search_url = None
    soup = None
    
    def __init__(self, keyword, search_type=None, search_url=None):
        self.keyword = keyword

        if search_type != None and search_type in self.search_types:
            self.search_type=search_type
        if search_url != None:
            self.search_url = search_url
        else:
            self.getSearchURL()

        self.parser()
            
    def parser(self):
        r = requests.get(self.search_url)
        self.soup = BeautifulSoup(r.content)

    def getSearchURL(self):
        urlhead='http://www.zhihu.com/search?type='
        search_url = urlhead + self.search_type + '&q=' + self.keyword
        self.search_url = search_url
        return search_url

    def getQuestions(self):
        if self.search_type != 'question':
            return False
        else:
            question_list = self.soup.find_all("a", class_="question-link")["href"]
            questions = []
            for i in question_list:
                question = i.contents[0].encode("utf-8").replace("\n", "")
                if platform.system() == 'Windows':
                    question = question.decode('utf-8').encode('gbk')
                questions.append(question)
            return questions

    def getPeoples(self):
        if self.search_type != 'people':
            return False
        else:
            people_list = self.soup.find_all("a", class_="name-link")["href"]
            peoples = []
            for i in people_list:
                people = i.contents[0].encode("utf-8").replace("\n", "")
                if platform.system() == 'Windows':
                    people = people.decode('utf-8').encode('gbk')
                peoples.append(people)
            return peoples

    def getTopics(self):
        if self.search_type != 'topic':
            return False
        else:
            topic_list = self.soup.find_all("a", class_="name-link")["href"]
            topics = []
            for i in topic_list:
                topic = i.contents[0].encode("utf-8").replace("\n", "")
                if platform.system() == 'Windows':
                    topic = topic.decode('utf-8').encode('gbk')
                topics.append(topic)
            return topics
