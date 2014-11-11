#!/usr/bin/env python
import dbus

# Koristi korisnički session bus
bus = dbus.SessionBus()

# Sa tog bus-a spoji se na connection 'org.freedesktop.Notifications'
# i dohvati objekt '/org/freedesktop/Notifications' sa te veze
notifier = bus.get_object('org.freedesktop.Notifications', '/org/freedesktop/Notifications')

# "Izvuci" iz objekta samo članove koji pripadaju interface-u 'org.freedesktop.Notifications'
# Ovo je potrebno jer dbus ponekad ne zna koju točno metodu želiš pozvati
interface = dbus.Interface(notifier, 'org.freedesktop.Notifications')

# Notifikacija bi se trebala pojaviti u uglu ekrana
interface.Notify('test_name', 0, '', 'test_title', 'test_body', '', '', 5000)

