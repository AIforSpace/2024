from ics import Calendar, Event
c = Calendar()
e = Event()

aest_offset = 10
e.name = "timezone test"
e.begin = '2022-09-21 '+str(16)+':00:00'
c.events.add(e)
# e = Event()
# e.name = "My cool event2 "
# e.begin = '2022-09-21 01:00:00'
# c.events.add(e)
# c.events



# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('my.ics', 'w') as my_file:
    my_file.writelines(c.serialize_iter())
# and it's done !