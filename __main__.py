from bitdeli import profile_events
from bitdeli.chunkedlist import ChunkedList

for profile, events in profile_events():
    pevents = profile.get('commits')
    if not pevents:
        profile['commits'] = pevents = ChunkedList()
    pevents.push(e.object for e in events)

