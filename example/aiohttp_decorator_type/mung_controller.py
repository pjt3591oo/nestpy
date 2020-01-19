from nest import Get, Post, Controller, PATHS
from aiohttp import web

@Controller('/')
class MungController(object):

  def __init__(self):
    pass

  @Get('')
  def my_func_a(self):
    return web.Response(text='/ get test')

  @Post('')
  def my_func_c(self):
    return web.Response(text='/ post test')
