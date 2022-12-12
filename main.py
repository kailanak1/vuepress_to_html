import markdown
import os

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
    repl_all(s, sub, repl)


def repl_all(s, sub, repl):
    s = s.replace(":::", "<div>")
    print(s)


def convert(files):
    if len(article_files) != 0:
        for article_path in article_files:
            with open(os.path.expanduser(f"{article_path}")) as article:
                article = article.read()
                html_article = markdown.markdown(article)
                # convert ::: to <div>stuff</div>
                if html_article.find(':::'):
                    nth_repl_all(html_article, ':::', '</div>', 2)
                else:
                    print(html_article)


for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        if name.endswith(".md"):
            file_path = os.path.join(root, name)
            article_files.append(file_path)
    convert(article_files)
