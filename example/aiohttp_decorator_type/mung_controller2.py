from nest import Get, Post, Controller, PATHS
from aiohttp import web

@Controller('/m')
class MungController2(object):

  def __init__(self):
    pass

  @Get('')
  def my_func_a(self):
    return web.Response(text='/m get test')

  @Post('')
  def my_func_c(self):
    return web.Response(text='/m post test')
