from nest import Get, Post, Controller, PATHS
from aiohttp import web

@Controller('/')
class MungController(object):

  def __init__(self):
    pass

  @Get('')
  def my_func_a(req):
    print(req.headers)
    print(req.rel_url.query.get('name', ''))
    return web.Response(text='/ get test')

  @Post('')
  def my_func_c(req):
    print(req.body_exists)
    print(req.match_info.get('name', ''))
    return web.Response(text='/ post test')
