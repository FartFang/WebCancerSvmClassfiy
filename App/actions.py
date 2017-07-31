# coding=utf-8
import json
import os

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from App.predict import turnToSvmData, scale, predict


@api_view(['GET'])
def putdata(request):
    str = request.GET.get('str','')
    # os.system('echo '+str+'> /Users/fei/data.txt')

    print str
    # result = predict()
    d = {"status":200,"result":"this is result"}
    # return Response(d)
    os.system('touch /Users/fangziming/Downloads/Predict/App/data.txt')
    f = open('/Users/fangziming/Downloads/Predict/App/data.txt', 'w')
    f.write(str)
    f.close()

    turnToSvmData()
    count = scale()
    print count
    m = predict(count)
    return Response(m)

# @api_view(['GET'])
# def index(request):
#     content = {}
#     content['result']="hello"
#     return render(request,'post.html',content)

@api_view(['POST'])
def post(request):
    ctx ={}
    print "hello"

    if request.method=='POST':
        print 'post'
    # ctx['content':request.POST['str']]
    # str = request.POST['str']
    received_json_data = json.loads(request.body)
    # str = 'h'
    str = received_json_data['str']

    os.system('touch /Users/fangziming/Predict/App/data.txt')
    f = open('/Users/fangziming/Predict/App/data.txt','w')
    f.write(str)
    f.close()

    turnToSvmData()
    count = scale()
    m = predict(count)
    return Response(m)
    # return render(request, "post.html", ctx)


# 表单
def submit_form(request):
    return render_to_response('submit_form.html')


# 接收请求数据
def submit(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        str = request.GET['q']
        print str
        os.system('touch /Users/fangziming/Predict/App/data.txt')
        f = open('/Users/fangziming/Predict/App/data.txt', 'w')
        f.write(str)
        f.close()

        turnToSvmData()
        count = scale()
        content = {}
        m = predict(count)
        if m==-1:
            return render(request, 'error.html', content)
        content['result1']=m['probabilityOfCancer']
        content['result2']=m['probabilityOfNonCancer']
        content['result3'] = m['type']
        return render(request,'response.html',content)
    else:
        message = '你提交了空表单'
        return HttpResponse(message)