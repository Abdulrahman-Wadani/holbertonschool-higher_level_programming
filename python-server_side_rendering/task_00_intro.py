def generate_invitations(template: str, attendees: list):
    counter = 1
    if (not isinstance(template, str) or not isinstance(attendees, list)):
        print('error')
        return

    for attendee in attendees:
        if (not isinstance(attendee, dict)):
            print('error')
            return
    if (len(template) == 0 or len(attendees) == 0):
        print('error')
        return
    for attendee in attendees:
        if (not attendee.get('name')):
            attendee['name'] = 'N/A'
        if (not attendee.get('event_title')):
            attendee['event_title'] = 'N/A'
        if (not attendee.get('event_date')):
            attendee['event_date'] = 'N/A'
        if (not attendee.get('event_location')):
            attendee['event_location'] = 'N/A'

    for attendee in attendees:
        tmp = template[:]
        tmp = tmp.replace('{name}', attendee['name'])
        tmp = tmp.replace('{event_title}', attendee['event_title'])
        tmp = tmp.replace('{event_date}', attendee['event_date'])
        tmp = tmp.replace('{event_location}', attendee['event_location'])
        with open(f'output_{counter}.txt', 'w') as file:
            file.write(tmp)
        counter += 1
