import os
import pdpyras

ROUTING_KEY = os.environ["PAGERDUTY_ROUTING_KEY"]

def make_call():
    events_session = pdpyras.EventsAPISession(ROUTING_KEY)
    events_session.url = 'https://events.eu.pagerduty.com'

    # RAISE INCIDENT
    dedup_key = events_session.trigger("<PAGER DUTY INCIDENT FIELD DESCRIPTION>", 'meta')

    # RESOLVE INCIDENT  
    # events_session.resolve(dedup_key)

if __name__ == '__main__':
    make_call()
