#!/usr/bin/env python
import dbus

# Koristi sistemski bus
bus = dbus.SystemBus()

# Sa tog bus-a spoji se na connection 'org.freedesktop.systemd1'
# i dohvati objekt '/org/freedesktop/systemd1' sa te veze
systemd = bus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')

# "Izvuci" iz objekta samo članove koji pripadaju interface-u 'org.freedesktop.Notifications'
# Ovo je potrebno jer DBus ponekad ne zna koju točno metodu želiš pozvati
interface = dbus.Interface(systemd, 'org.freedesktop.systemd1.Manager')

# Restartaj Nginx server
interface.RestartUnit('nginx.service', 'replace')

