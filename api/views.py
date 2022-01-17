from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

import json
import datetime
import pytz

class Get_Time(APIView):
    def get(self, request, timezone='UTC'):
        t=get_timezone(timezone)
        result = datetime.datetime.now().astimezone(pytz.timezone(t)).strftime("%Y-%m-%d %H:%M:%S")
        return JsonResponse({t:result}, safe=False)

class Convert_Time(APIView):

    def get(self, request, t1, t2):
        x=get_timezone(t1)
        y=get_timezone(t2)
        time1= datetime.datetime.now().astimezone(pytz.timezone(x))
        time2=time1.astimezone(pytz.timezone(y))
        return JsonResponse({t1:time1.strftime("%Y-%m-%d %H:%M:%S"),t2:time2.strftime("%Y-%m-%d %H:%M:%S")}, safe=False)

def get_timezone(timezone):

    timezone=timezone.upper()

    if(timezone=='LINT'):
        timezone='Pacific/Kiritimati'

    elif(timezone=='CHADT'):
        timezone='Pacific/Chatham'

    elif(timezone=='NZDT'):
        timezone='NZ'

    elif(timezone=='ANAT'):
        timezone='Asia/Anadyr'

    elif(timezone=='AEDT'):
        timezone='Australia/ACT'

    elif(timezone=='ACDT'):
        timezone='Australia/Adelaide'

    elif(timezone=='AEST'):
        timezone='Australia/Queensland'

    elif(timezone=='JST'):
        timezone='Japan'

    elif(timezone=='ACWST'):
        timezone='Australia/Eucla'

    elif(timezone=='CST'):
        timezone='Asia/Shanghai'

    elif(timezone=='WIB'):
        timezone='Asia/Jakarta'

    elif(timezone=='MMT'):
        timezone='Indian/Cocos'

    elif(timezone=='BST'):
        timezone='Asia/Dhaka'

    elif(timezone=='NPT'):
        timezone='Asia/Katmandu'

    elif(timezone=='IST'):
        timezone='Asia/Kolkata'

    elif(timezone=='UZT'):
        timezone='Asia/Tashkent'

    elif(timezone=='AFT'):
        timezone='Asia/Kabul'

    elif(timezone=='GST'):
        timezone='Asia/Dubai'

    elif(timezone=='IRST'):
        timezone='Asia/Tehran'

    elif(timezone=='MSK'):
        timezone='Europe/Moscow'

    elif(timezone=='EET'):
        timezone='Europe/Bucharest'

    elif(timezone=='CET'):
        timezone='Europe/Brussels'

    elif(timezone=='CVT'):
        timezone='Atlantic/Cape_Verde'

    elif(timezone=='WGST'):
        timezone='Atlantic/South_Georgia'

    elif(timezone=='ART'):
        timezone='America/Argentina/Buenos_Aires'

    elif(timezone=='NST'):
        timezone='America/St_Johns'

    elif(timezone=='VET'):
        timezone='America/Caracas'

    elif(timezone=='EST'):
        timezone='EST'

    elif(timezone=='CT'):
        timezone='US/Central'

    elif(timezone=='MST'):
        timezone='US/Mountain'

    elif(timezone=='PST'):
        timezone='US/Pacific'

    elif(timezone=='AKST'):
        timezone='US/Alaska'

    elif(timezone=='MART'):
        timezone='Pacific/Marquesas'

    elif(timezone=='HST'):
        timezone='US/Hawaii'

    elif(timezone=='NUT'):
        timezone='Pacific/Niue'

    elif(timezone=='AOE'):
        timezone='Etc/GMT+12'
    else:
        timezone='UTC'

    return timezone

