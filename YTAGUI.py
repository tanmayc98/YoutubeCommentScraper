from YouTubeAnalysis import get_comments
import easygui


def front_end():
    msg = "Enter Video URL"
    title = "Video-Comment Analyzer"
    fieldName = "Enter Video URL"
    fieldValue = ""  # we start with blanks for the values

    fieldValue = easygui.enterbox(msg=fieldName, default="", title=title, strip=True)

    while fieldValue == "":
        easygui.msgbox(msg='Please enter valid URL', title=' Error ', ok_button='OK')
        fieldValue = easygui.enterbox(msg=fieldName, default="", title=title, strip=True)

    print("Reply was:", fieldValue)

    comment_list = get_comments(fieldValue)
    comments_output = ""
    i = 1
    for comment in comment_list:
        char_list = [comment[j] for j in range(len(comment)) if ord(comment[j]) in range(0, 65536)]
        print(char_list)
        comments_output = comments_output + str(i)+". "+ ("".join(char_list)) + '\n'
        i = i+1
    print(comments_output)

    easygui.textbox(msg='Comments', title='Result', text=comments_output)


print("".join(['a', 'b', 'c']))

front_end()
