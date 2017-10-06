#!/usr/bin/env python
#coding: utf-8

import time

"""
大家好，我是kevin。

我们的基础课更难的知识点已经全部讲完。接下来，是两道应用题。这两道应用题，多多少少都有些难度。第一道是文本题，第二道则是小游戏题。前者考知识点，后者考逻辑。前者偏坑爹（难），后者偏有趣（更难^_^），这两道应用题，会给大家足够的时间去思考，总结与回顾。

第一道题，是一道文本题。文件夹里有一个twitter数据挖掘的片段，每一行则是一个tweets（微博），里面有该微博的相关字段信息。

对应字段如下（每一个逗号分隔的，“”内的，则是字段的详细信息。空白则代表没有。）：

bid    消息ID 
uid     用户ID 
username 用户名  
ugrade 用户等级字段 
content(text) 微博内容
img(message包含图片链接) 
created_at 微博发布时间 
source(来源)
rt_num

, 转发数 
cm_num, 评论数 
rt_uid, 转发UID
rt_username, 转发用户名
rt_v_class, 转发者等级 
rt_content, 转发内容 
rt_img, 转发内容所涉及图片 
src_rt_num, 源微博回复数 
src_cm_num, 源微博评论数 
gender,(用户性别) 
rt_mid（转发mid） 
geo 地区
lat() 经度
lon 纬度
place 地点
hashtags 
ats  @谁 
rt_hashtags, 回复标签
rt_ats, 回复@谁
v_url, 源微博URL 
rt_v_url 转发URL 


twitter文本附件的排序格式如下

fields=bid,uid,username,v_class,content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url


而童鞋们，则需要利用自己已经掌握的知识，对其进行一个基本的文本分析。


注意：请用utf-8格式打开此文件。

要求如下：

1.该文本里，有多少个用户。（要求：输出为一个整数。）

2.该文本里，每一个用户的名字。 （要求：输出为一个list。）

3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）

4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）

5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）

6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）

7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） 

8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）

9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)

10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）

11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。

12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）

13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）

14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）

15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）
"""

now = time.time()

field_list = ["bid","uid","username","v_class","content","img","time","source","rt_num","cm_num","rt_uid","rt_username","rt_v_class","rt_content","rt_img","src_rt_num","src_cm_num","gender","rt_mid","location","rt_mid","mid","lat","lon","lbs_type","lbs_title","poiid","links","hashtags","ats","rt_links","rt_hashtags","rt_ats","v_url","rt_v_url"]


with open('twitter-data.txt', 'r') as f:
    b_data = f.readlines()

# 1.该文本里，有多少个用户。（要求：输出为一个整数。）

user_list = []

for i in b_data:
    c_data = i[1:-1].split('","')[field_list.index('username')]
    user_list.append(c_data)

user_total = len(set((user_list)))

assert type(user_total) == int

#print user_total

# 2.该文本里，每一个用户的名字。 （要求：输出为一个list。）

#print user_list


# 3.该文本里，有多少个2012年11月发布的tweets。 （要求：输出为一个整数。提示：请阅读python的time模块）

tweets_time_list = [ i[1:-1].split('","')[field_list.index('time')] for i in b_data ]

tweets_in_2012_11 = [ i for i in tweets_time_list if i.startswith('2012-11') == True]

#print len(tweets_in_2012_11)


# 4.该文本里，有哪几天的数据？ （要求：输出为一个list，例：['2012-03-04','2012-03-05']）

time_data = list(set([ i.split()[0] for i in tweets_time_list ]))


# 5.该文本里，在哪个小时发布的数据最多？ （要求：输出一个整数。）


tweets_hours_list = [ i.split(" ")[1][:2] for i in tweets_time_list ]

hours_count = {}
for x in tweets_hours_list:
    hours_count[x] = hours_count.setdefault(x,0) + 1

#print tweets_hours_list
#print hours_count

#print sorted(hours_count.items(),key= lambda x:x[1],reverse=True)

# 6.该文本里，输出在每一天发表tweets最多的用户。（要求：输出一个字典。例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）


tweet_by_user = { x:dict() for x in time_data }

for i in b_data:
    dateline = i.split('","')[field_list.index('time')].split( )[0]
    username = i.split('","')[field_list.index('username')]

    if tweet_by_user[dateline].has_key(username):
        tweet_by_user[dateline][username] += 1
    else:
        tweet_by_user[dateline][username] = 1

#print tweet_by_user

for k,v in tweet_by_user.items():
    us = v.items()
    us.sort(key=lambda x:x[1],reverse=True)
    tweet_by_user[k] = {us[0][0]:us[0][1]}

#print tweet_by_user

# 7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） 

"""
1. line.startswith('2012-11-03')
2. time[:] --> 时间
3. setdefault --> time,0 + 1
4. dict.values() --> list拼接
"""

d_20121103 = [ line for line in b_data if line.split('","')[field_list.index('time')].startswith('2012-11-03') ]

hours_tweets = { str(i):0 for i in xrange(24) }

for line in d_20121103:
    hours_tweets[str(int(line.split('","')[field_list.index('time')][11:13]))] += 1

hours_tweets_list = [ i for i in hours_tweets.items() ]

#print sorted(hours_tweets_list,key=lambda x:int(x[0]))

# 8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）

soucre_dict = dict.fromkeys(set([ i.split('","')[field_list.index('source')] for i in b_data ]),0)

for i in b_data:
    soucre_dict[i.split('","')[field_list.index('source')]] += 1

source_list = [ x for x in soucre_dict.items()]
source_list.sort(key=lambda x:x[1], reverse = True)

#print source_list

# 9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)

rt_url_list = [ i for i in b_data if i.split('","')[field_list.index('rt_v_url')].startswith("https://twitter.com/umiushi_no_uta") ]

#print len(rt_url_list)


# 10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）

uid_count = 0
for line in b_data:
    if line.split('","')[field_list.index('uid')] == str(573638104):
        uid_count += 1
# print uid_count 


#11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。


"""
1. 生成uid:count的字典;
2. 将uid进行遍历，不存在的返回null
3. 将uid及对应的count进行列表排序
4. 返回list[0][0]

"""

def max_tweets_uid(*uids):
    uid_count_dict = {}
    max_tweets_list = []

    for i in b_data:
        x = i.split('","')[field_list.index('uid')]
        uid_count_dict[x] = uid_count_dict.setdefault(x ,0) + 1

    if len(uids) < 1:
        return 'error'

    else:
        for uid in uids:

            if uid_count_dict.get(str(uid)) == None:
                #print uid,type(uid),uid_count_dict.get(uid)
                return 'null'

            else:
                max_tweets_list.append((uid,uid_count_dict.get(str(uid))))

        max_tweets_list.sort(key=lambda x:x[1], reverse=True)
        return max_tweets_list[0][0] 


# 12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）

uid_content = [ (i.split('","')[field_list.index('username')],len(i.split('","')[field_list.index('content')])) for i in b_data ]

uid_content.sort(key=lambda x:x[1],reverse=True)

# print uid_content[0][0]



#13. 该文本里，谁转发的URL最多 （要求：输出用户的uid，字符串格式。）


uid_rt_list = [ (i.split('","')[field_list.index('uid')],int(i.split('","')[field_list.index('rt_num')])) for i in b_data if i.split('","')[field_list.index('rt_num')] != "" ]

uid_rt_list.sort(key=lambda x:int(x[1]),reverse=True)

#print uid_rt_list[0][0]

#14. 该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）

uid_rt_11 = [ i for i in b_data if i.split('","')[field_list.index('time')][11:13] == "11" ]

uid_rt_11_dict = { i.split('","')[field_list.index('uid')]:0 for i in uid_rt_11 }

for i in uid_rt_11:
    uid_rt_11_dict[i.split('","')[field_list.index('uid')]] += 1

uid_rt_11_list = sorted([ (k,v) for k,v in uid_rt_11_dict.items() ],key=lambda x:x[1] , reverse=True)

print uid_rt_11_list[0][0]

# print uid_rt_11_dict



#15. 该文本里，哪个用户的源微博URL次数最多。 （要求：输出用户的uid，字符串格式。）

# 获取到源微博的id
rt_count_list = [ i.split('","')[field_list.index('uid')] for i in b_data if i.split('","')[field_list.index('v_url')] != '' ]

print set(rt_count_list)

v_url_list = [ (i,rt_count_list.count(i)) for i in set(rt_count_list) ]
v_url_list.sort(key=lambda x:x[1], reverse=True)

print v_url_list[0]

rt_count_dict = { i.split('","')[field_list.index('uid')]:0 for i in b_data }


for i in b_data:
    uid = i.split('","')[field_list.index('uid')]
    if i.split('","')[field_list.index('v_url')] != "":
        rt_count_dict[uid] += 1

rt_count_sort_list = [ (k,v) for k,v in rt_count_dict.items() ]
rt_count_sort_list.sort(key=lambda x:x[1],reverse=True)

print rt_count_sort_list[0][0]








print "运算时间： %s" % (time.time() - now)
 
