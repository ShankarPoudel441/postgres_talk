import psycopg2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import datetime

con = psycopg2.connect(
    host="localhost",
    database="webdata",
    user="postgres",
    password="postgres",
    port=5432)
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS raidforums")
cur.execute("create table raidforums(id int primary key not null, post_name varchar not null, post_by varchar not null, post_date varchar not null, scrap_date timestamp not null)")

url = 'https://raidforums.com/Forum-Databases'
driver = webdriver.Chrome()
driver.get(url)

posts_table = driver.find_elements_by_xpath(
    '//*[@id="forum-display"]/table[3]/tbody/tr')
full_length = len(posts_table)

counter = 0
for i in range(11, full_length-1):
    counter += 1
    post_element = driver.find_element_by_xpath(
        '//*[@id="forum-display"]/table[3]/tbody/tr['+str(i)+']/td[2]')

    post_name = post_element.find_element_by_xpath(
        './/div/div/span/a/span').text

    post_by = post_element.find_element_by_xpath('.//div/span[1]/a/span').text

    try:
        post_date = post_element.find_element_by_xpath(
            './/div/span[2]/span').get_attribute('title')
        possibility = post_element.find_element_by_class_name(
            'forum-display__thread-date').text
        if (re.search("ago$", str(possibility)) == None):
            post_date = post_date + possibility[-12:]
    except:
        post_date = post_element.find_element_by_class_name(
            'forum-display__thread-date').text

    scrap_date = datetime.datetime.now()

    cur.execute("insert into raidforums(id, post_name, post_by, post_date, scrap_date) values(%s, %s, %s, %s,%s)",
                (counter, post_name, post_by, post_date, scrap_date))


con.commit()
cur.close()
con.close()
