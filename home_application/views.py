# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context, render_json
from home_application.models import Count

def home(request):
    """
    首页
    """
    #=====================================
    #获取数据库存储信息
    req_sql = Count.objects.all()
    act = {
        "req_sql": req_sql
    }
    #=====================================
    return render_mako_context(request, '/home_application/home.html', act)

def computer(request):
    '''
    首页的请求计算
    '''

    input1 = request.GET.get("input1")
    input2 = request.GET.get("input2")
    request = int(input2) * int(input1)
    Count.objects.create(
        input1=input1,
        input2=input2,
        result=request
    )
    return render_json(request)




def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
