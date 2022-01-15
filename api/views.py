from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response

import json
import datetime
import pytz

class Get_Time(APIView):
    def get(self, request, timezone='UTC'):
        t=get_timezone(timezone)
        result = datetime.datetime.now().astimezone(pytz.timezone(t)).strftime("%Y-%m-%d %H:%M:%S")
        return JsonResponse({timezone.upper():result}, safe=False)

#datetime.datetime.utcnow().astimezone(pytz.timezone("Asia/Kolkata")).isoformat()

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

    if(timezone=='CHADT'):
        timezone='Pacific/Chatham'

    if(timezone=='NZDT'):
        timezone='NZ'

    if(timezone=='ANAT'):
        timezone='Asia/Anadyr'

    if(timezone=='AEDT'):
        timezone='Australia/ACT'

    if(timezone=='ACDT'):
        timezone='Australia/Adelaide'

    if(timezone=='AEST'):
        timezone='Australia/Queensland'

    if(timezone=='JST'):
        timezone='Japan'

    if(timezone=='ACWST'):
        timezone='Australia/Eucla'

    if(timezone=='CST'):
        timezone='Asia/Shanghai'

    if(timezone=='WIB'):
        timezone='Asia/Jakarta'

    if(timezone=='MMT'):
        timezone='Indian/Cocos'

    if(timezone=='BST'):
        timezone='Asia/Dhaka'

    if(timezone=='NPT'):
        timezone='Asia/Katmandu'

    if(timezone=='IST'):
        timezone='Asia/Kolkata'

    if(timezone=='UZT'):
        timezone='Asia/Tashkent'

    if(timezone=='AFT'):
        timezone='Asia/Kabul'

    if(timezone=='GST'):
        timezone='Asia/Dubai'

    if(timezone=='IRST'):
        timezone='Asia/Tehran'

    if(timezone=='MSK'):
        timezone='Europe/Moscow'

    if(timezone=='EET'):
        timezone='Europe/Bucharest'

    if(timezone=='CET'):
        timezone='Europe/Brussels'

    if(timezone=='CVT'):
        timezone='Atlantic/Cape_Verde'

    if(timezone=='WGST'):
        timezone='Atlantic/South_Georgia'

    if(timezone=='ART'):
        timezone='America/Argentina/Buenos_Aires'

    if(timezone=='NST'):
        timezone='America/St_Johns'

    if(timezone=='VET'):
        timezone='America/Caracas'

    if(timezone=='EST'):
        timezone='EST'

    if(timezone=='CT'):
        timezone='US/Central'

    if(timezone=='MST'):
        timezone='US/Mountain'

    if(timezone=='PST'):
        timezone='US/Pacific'

    if(timezone=='AKST'):
        timezone='US/Alaska'

    if(timezone=='MART'):
        timezone='Pacific/Marquesas'

    if(timezone=='HST'):
        timezone='US/Hawaii'

    if(timezone=='NUT'):
        timezone='Pacific/Niue'

    if(timezone=='AOE'):
        timezone='Pacific/Wallis'

    return timezone
