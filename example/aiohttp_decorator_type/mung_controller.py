from nest import Get, Post, Controller, PATHS
from aiohttp import web

@Controller('/')
class MungController(object):

  def __init__(self):
    pass

  @Get('')
  def my_func_a(self, req):
    # print(req.headers)
    # print(req.rel_url.query.get('name', ''))
    print('req', req.rel_url.query.get('name1', ''))
    print('req', req.rel_url.query.get('name2', ''))
    print(self.test)
    print(self.test1())
    return web.Response(text='/ get test')

  @Post('')
  def my_func_c(self, req):
    print(req.body_exists)
    print(req.match_info.get('name', ''))
    return web.Response(text='/ post test')
