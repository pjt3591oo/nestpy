from nest import Get, Post, Controller, PATHS
from aiohttp import web

@Controller('/')
class MungController(object):

  def __init__(self):
    self.a = 1000

  @Get('')
  def my_func_a(self, req):
    # print(req.headers)
    # print(req.rel_url.query.get('name', ''))
    print('self', self, self.a)
    print('req', req.rel_url.query.get('name1', ''))
    print('req', req.rel_url.query.get('name2', ''))
    print()
    return web.Response(text='/ get test')

  @Post('')
  def my_func_c(self, req):
    print(req.body_exists)
    print(req.match_info.get('name', ''))
    return web.Response(text='/ post test')
