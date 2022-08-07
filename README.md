# google-calendar-api-examples
 Easy examples of using google calendar api in python. This file is based on Calendar API official [Quickstart Sample](https://developers.google.com/calendar/api/quickstart/python), adding access to multiple calendars.

## Setup credentials.json
You need go to [Google Cloud Console](https://console.cloud.google.com/?hl=zh-TW) do following things:
1. Create a project and switch to it.
1. Enable Calendar API in this project.
1. (Add a test account)
1. Get an credentials by OAuth2.0.
1. Download credentials JSON file.
1. Rename it to 'credentials.json' and copy it to this root folder.

## Usage
```python
python3 get-events.py
```
If this is your first time running the code, it opens a new window prompting you to authorize access to your data.

## Result
```
Getting events form calendar [Work](ID: xxx)...
Getting events form calendar [Play](ID: xxx)...
All events in upcoming 100 days:
2022-09-03 [Work] Meeting with xxxx
2022-09-09 [Work] CES conf
2022-09-10 [Play] Hawaii
2022-09-28 [Work] Q3 Project report
```

## Calendar API Reference
* [CalendarList](https://developers.google.com/calendar/api/v3/reference/calendarList)
* [Calendar](https://developers.google.com/calendar/api/v3/reference/calendars)
* [Event](https://developers.google.com/calendar/api/v3/reference/events)
