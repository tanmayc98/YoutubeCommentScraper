from selenium import webdriver

import time
import nltk

def get_comments(url):

    driver = webdriver.Chrome("chromedriver-2")
    driver.get(url)
    time.sleep(5)
    i = 500
    prev = 0
    step_size = 500
    more_comments = True
    while more_comments:
        driver.execute_script('window.scrollTo(1, '+str(i)+');')

        # now wait let load the comments
        print(i)
        time.sleep(10)
        value = driver.execute_script('return window.pageYOffset;')
        if value == prev:
            more_comments = False
        else:
            prev = value

        print("Current scroll position is : " + str(value))

        i = i + step_size

    comment_div = driver.find_element_by_xpath('//*[@id="contents"]')
    comments = comment_div.find_elements_by_xpath('//*[@id="content-text"]')
    comment_list = []
    for comment in comments:
        print(comment.text)
        comment_list.append(comment.text)

    print("Total Number of comments scraped: "+str(len(comment_list)))

    unique_words = {}
    for comment1 in comment_list:
        tokens = nltk.word_tokenize(comment1)
        for word in tokens:
            word_lower = word.lower()
            if word_lower not in unique_words.keys():
                unique_words[word_lower] = 1
            else:
                unique_words[word_lower] += 1

    for w in sorted(unique_words, key=unique_words.get, reverse=True):
        print(w, unique_words[w])

    return comment_list



