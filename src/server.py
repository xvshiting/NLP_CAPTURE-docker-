# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import json
import main_process as mp
import tools
import logging
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.warning('Do not support get!')
        self.write("Do not support get !")
    def post(self):
        param = self.request.body.decode('utf-8')
        res=dict()
        try:
            res=mp.process(param)
        except Exception as e:
            logging.exception("main process error!")


        self.write(json.dumps(res))
class GetJsonHandler(tornado.web.RequestHandler):
    def get(self,name):
        self.write(json.dumps(mp.getJson(name)))
    def post(self):
        logging.warning('GetJosn do not support post')
        self.write('GetJosn do not support post')
class AddJsonHandler(tornado.web.RequestHandler):
    def get(self):
        logging.warning('Do not support get!')
        self.write("Do not support get !")
    def post(self,name):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        res=mp.AddJson(name,param)
        self.write(res)
class DelJsonHandler(tornado.web.RequestHandler):
    def get(self,name):
        res=mp.DeletJson(name)
        self.write(res)
    def post(self):
        logging.warning('Do not support post!')
        self.write("Do not support post !")

class UpdateJsonHandler(tornado.web.RequestHandler):
    def get(self):
        logging.warning('Do not support get!')
        self.write("Do not support get !")
    def post(self,name):
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        res=mp.UpdateJson(name,param)
        self.write(res)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/GetJson/(.*)",GetJsonHandler),
        (r"/AddJson/(.*)",AddJsonHandler),
        (r"/DelJson/(.*)",DelJsonHandler),
        (r"/UpdataJson/(.*)",UpdateJsonHandler),
    ])
if __name__ == "__main__":
    logging.basicConfig(filename='log/capture.log',datefmt='%Y-%m-%d %I:%M:%S %p',format='%(asctime)s : L(%(levelname)s) : %(message)s',level=logging.WARNING)
    app = make_app()
    app.listen(8899,address="0.0.0.0")
    tornado.ioloop.IOLoop.current().start()
