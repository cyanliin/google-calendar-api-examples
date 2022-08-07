import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
DAYS = 100
MAX_EVENTS = 99

def main():
    creds = getCreds();
    try:
        service = build('calendar', 'v3', credentials=creds)
        calendars = getCalenders(service)
        events = getEvents(service, calendars)

        if not events:
            print('No upcoming events found.')
            return

        displayEvents(events)

    except HttpError as error:
        print('An error occurred: %s' % error)


def getCreds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def getCalenders(service):
    calenders = []
    calendar_list = service.calendarList().list(pageToken=None).execute()
    for calendar_list_entry in calendar_list['items']:
        calenders.append(calendar_list_entry)
    return calenders


def getEvents(service, calendar_list):
    now = datetime.datetime.utcnow()
    max_time = now + datetime.timedelta(days=DAYS) 
    all_events = []
    for calender in calendar_list:
        print('Getting events form calendar [{}](ID: {})...'.format(calender['summary'], calender['id']))
        calender_events = service.events().list(
            calendarId=calender['id'],
            timeMin=now.isoformat() + 'Z',
            timeMax=max_time.isoformat() + 'Z',
            maxResults=MAX_EVENTS,
            singleEvents=True,
            orderBy='startTime').execute()
        for event in calender_events['items']:
            event['calendar_name'] = calender['summary']
            all_events.append(event)
    return all_events


def displayEvents(events):
    # sort by start time
    events.sort(key=lambda x: x['start'].get('dateTime', x['start'].get('date')), reverse=False)

    # print
    print('All events in upcoming {} days:'.format(DAYS))
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print('{} [{}] {}'.format(start, event['calendar_name'], event['summary']))


if __name__ == '__main__':
    main()
# [END calendar_quickstart]