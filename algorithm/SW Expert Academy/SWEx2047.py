
sentence = str('The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.')
for i in sentence:
    if 97<= ord(i) <=122:
        print(chr(ord(i)-32),end="")
    else:
        print(i,end="")