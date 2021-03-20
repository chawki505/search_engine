import os
from abc import ABC

import tornado.ioloop
import tornado.web
import re

from pagerank import sort_page_by_score
from utils import deserialize, get_clean_tokens
from paths import path_pagerank, path_dico, path_pagelist_plaintext_resume

print("* deserialize pagerank")
pagerank = deserialize(path_pagerank)

print("* deserialize dico")
dictionnary = deserialize(path_dico)

print("* deserialize page list plaintext")
pagelist = deserialize(path_pagelist_plaintext_resume)

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "../../front-end"),
}


class SearchHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.render("../../front-end/index.html")

    def post(self):
        request = self.get_argument('req')
        clean_req = get_clean_tokens(request)
        res = sort_page_by_score(clean_req, dictionnary, pagerank)
        top10res = []
        for i in res[:15]:
            id = pagelist[i[0]][0]
            title = pagelist[i[0]][1]
            content = pagelist[i[0]][2]

            top10res.append((id, title, content[:300] + "..."))

        self.render("../../front-end/result.html", request=request, result_pagelist=top10res)


class ResultHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.render("../../front-end/result.html")

    def post(self):
        self.redirect("/")


def make_app():
    return tornado.web.Application([
        (r"/", SearchHandler),
        (r"/result", ResultHandler),
    ], **settings)


if __name__ == "__main__":
    port = 8080

    app = make_app()
    app.listen(port)

    print("http://localhost:{0}".format(port))

    tornado.ioloop.IOLoop.current().start()
