from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图就是 python函数
视图函数有两个要求：
    1. 视图函数的第一个参数就是接收请求，就是接收请求,这个请求就是，HttpRequest的类对象
    2. 必须返回一个响应
"""

# request
from django.http import HttpRequest
# respond
from django.http import HttpResponse


# 我们期望用户输入 http://127.0.0.11:8000/index/
# 来访问视图函数
def index(request):
    # return HttpResponse('ok')

    # render 的三个参数 render翻译过来就是渲染模版
    # request, 请求
    # template_name,
    # context=None

    # 模拟数据查询
    context = {
        'name': '马上双十二，点击有惊喜'
    }
    return render(request, 'book/index.html', context=context)
