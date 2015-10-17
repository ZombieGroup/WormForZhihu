create table Users(
	user_ID char(8) primary key,
	followers_num int,
	followees_num int,
	agrees_num int,
	thanks_num int,
	asks_num int,
	answers_num int,
	collections_num int
);

create table Questions(
	question_ID char(8) primary key,
	asker_ID char(8),
	detail text,
	title varchar(20),
	answers_num int,
	followers_num int,
	foreign key (asker_ID) references Users(user_ID)
);

create table Topic(
	topic_name varchar(20) primary key
);

create table Answers(
	answer_ID char(8) primary key,
	question_ID char(8),
	author_ID char(8),
	detail text,
	upvote int,
	visit_times int,
	foreign key (question_ID) references Questions(question_ID),
	foreign key (author_ID) references Users(user_ID)
);

create table Collection(
	name varchar(8) primary key,
	creator char(8),
	foreign key (creator) references Users(user_ID)
);

create table Follow_Question(
	question_ID char(8),
	follower_ID char(8),
	foreign key (question_ID) references Questions(question_ID),
	foreign key (follower_ID) references Users(user_ID),
	primary key (question_ID, follower_ID)
);

create table Follow_User(
	follower_ID char(8),
	followee_ID char(8),
	foreign key (follower_ID) references Users(user_ID),
	foreign key (followee_ID) references Users(user_ID),
	primary key (followee_ID, follower_ID)
);

create table Question_Topics(
	question_ID char,
	topic_name varchar(20),
	foreign key (question_ID) references Questions(question_ID),
	foreign key (topic_name) references Topic(topic_name)
);

create table Collection_Answers(
	collection_name varchar(8),
	answer_ID char(8),
	foreign key (collection_name) references Collection(name),
	foreign key (answer_ID) references Answers(answer_ID),
	primary key (collection_name, answer_ID)
);