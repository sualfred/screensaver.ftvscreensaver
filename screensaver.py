#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2013 Tristan Fischer (sphere@dersphere.de)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import xbmcaddon
import xbmcgui
import xbmc

addon = xbmcaddon.Addon()
addon_name = addon.getAddonInfo('name')
addon_path = addon.getAddonInfo('path')


class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            self.exit_callback()

    def onInit(self):
        self.abort_requested = False
        self.started = False
        self.exit_monitor = self.ExitMonitor(self.exit)

        if addon.getSetting('enable_Dim') == 'true':
            xbmcgui.Window(10000).setProperty('fTVscreensaver.dim', '1')

        if addon.getSetting('list1') == 'Random Movies':
            xbmcgui.Window(10000).setProperty('fTVscreensaver.content1', '%s/resources/playlist/movie_idle.xsp' % addon_path)
        else:
            xbmcgui.Window(10000).setProperty('fTVscreensaver.content1', addon.getSetting('list1'))

        if addon.getSetting('list2') == 'Random TV Shows':
            xbmcgui.Window(10000).setProperty('fTVscreensaver.content2', '%s/resources/playlist/tvshow_idle.xsp' % addon_path)
        else:
            xbmcgui.Window(10000).setProperty('fTVscreensaver.content2', addon.getSetting('list2'))

        xbmcgui.Window(10000).setProperty('fTVscreensaver.scrollspeed', addon.getSetting('scrollspeed'))

    def exit(self):
        self.abort_requested = True
        self.exit_monitor = None
        self.log('exit')
        self.close()

    def log(self, msg):
        xbmc.log(u'fTV Screensaver: %s' % msg)

if __name__ == '__main__':
    screensaver = Screensaver(
        'script-ftv-screensaver-main.xml',
        addon_path,
        'default',
    )
    screensaver.doModal()
    del screensaver
    sys.modules.clear()
