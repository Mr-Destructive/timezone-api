# Timezone API

## An FOSS API for fetching and converting timezones across the world.

## Techstack

- Django
- Django-Rest-Framework
- DRF-YASG
- pytz
- Heroku

## Endpoints

- `/api/{timezone-code}/` -> get the current time in the given time zone(eg. IST, EST, BST).

- `/api/convert/{t1}/{t2}/` -> convert the time in timezone t1 into other timezone t2.

## List of Timezone Code:

<pre>
Timezone Code |  UTC Offset
______________________________
              |               |
- `LINT`      |  +14     UTC  | 
- `CHADT`     |  +13:45  UTC  | 
- `NZDT`      |  +13     UTC  | 
- `ANAT`      |  +12     UTC  | 
- `AEDT`      |  +11     UTC  | 
- `ACDT`      |  +10:30  UTC  |  
- `AEST`      |  +10     UTC  | 
- `ACST`      |  +9:30   UTC  |      
- `JST`       |  +9      UTC  |  
- `ACWST`     |  +:45    UTC  |  
- `CST`       |  +8      UTC  |  
- `WIB`       |  +7      UTC  |  
- `MMT`       |  +6:30   UTC  |  
- `BST`       |  +6      UTC  |  
- `NPT`       |  +5:45   UTC  |    
- `IST`       |  +5:30   UTC  |    
- `UZT`       |  +5      UTC  |  
- `AFT`       |  +4:30   UTC  |    
- `GST`       |  +4      UTC  |  
- `IRST`      |  +3:30   UTC  |  
- `MSK`       |  +3      UTC  |  
- `EET`       |  +2      UTC  |         
- `CET`       |  +1      UTC  |   
- `CVT`       |  -1      UTC  |   
- `WGST`      |  -2      UTC  |   
- `ART`       |  -3      UTC  |   
- `NST`       |  -3:30   UTC  |     
- `VET`       |  -4      UTC  |   
- `EST`       |  -5      UTC  |   
- `CT`        |  -6      UTC  |     
- `MST`       |  -7      UTC  |     
- `PST`       |  -8      UTC  |     
- `AKST`      |  -9      UTC  |     
- `MART`      |  -9:30   UTC  |       
- `HST`       |  -10     UTC  |       
- `NUT`       |  -11     UTC  |       
- `AOE`       |  -12     UTC  |       
- `UTC`       |  +0      UTC  | 
______________________________|
</pre>
