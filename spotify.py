#!/usr/bin/env python
import dbus

# Koristi korisnički session bus
bus = dbus.SessionBus()

# Sa tog bus-a spoji se na connection 'org.mpris.MediaPlayer2.spotify'
# i dohvati objekt '/org/mpris/MediaPlayer2' sa te veze
player = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')

# Pozovi PlayPause metodu nad tim objektom
player.PlayPause()


# Dohvati 'PlaybackStatus' property od našeg objekta.
# Property je definiran u 'org.mpris.MediaPlayer2.Player' interface-u.
print (player.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus'))

