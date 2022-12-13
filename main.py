import markdown
import os
import re

yourpath = "/path/to/directory"
article_files = []


def nth_repl_all(s, sub, repl, nth):
    find = s.find(sub)
    # loop util we find no match
    i = 1
    while find != -1:
        # if i  is equal to nth we found nth matches so replace
        if i == nth:
            s = s[:find] + repl + s[find + len(sub):]
            i = 0
    # find + len(sub) + 1 means we start after the last match
        find = s.find(sub, find + len(sub) + 1)
        i += 1
    repl_all(s)


def write_file(s):
    html_title = s.partition('\n')[0]
    h_title = re.sub('<[^<]+?>', '', html_title)
    title = re.sub(r'[^\w_. -]', '_', h_title)
    with open(f'{title}.txt', 'w+') as f:
        f.write(s)


def repl_all(s):
    s = s.replace(":::", "<div>")
    write_file(s)


def convert(files):
    if len(article_files) != 0:
        for article_path in article_files:
            with open(os.path.expanduser(f"{article_path}")) as article:
                opened_article = article.read()
                html_article = markdown.markdown(opened_article)
                # convert ::: to <div>stuff</div>
                article.close()
                if html_article.find(':::'):
                    nth_repl_all(html_article, ':::', '</div>', 2)
                else:
                    # write_file(html_article)
                    print("skip")


for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        if name.endswith(".md"):
            file_path = os.path.join(root, name)
            article_files.append(file_path)
    convert(article_files)
