# Timezone API

## An FOSS API for fetching and converting timezones across the world.

## Techstack

- Django
- Django-Rest-Framework
- DRF-YASG
- pytz
- Heroku

## Endpoints

- `/get/{timezone-code}/` -> get the current time in the given time zone(eg. IST, EST, BST).

- `/convert/{t1}/{t2}/` -> convert the time in timezone t1 into other timezone t2.

