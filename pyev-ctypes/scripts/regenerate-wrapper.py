#!/usr/bin/python
'''
apt-get install python-ply
http://code.google.com/p/rpythonic/

http://dist.schmorp.de/libev/libev-4.11.tar.gz
make and make install - you should then have /usr/local/lib/libev.so
'''
import os, sys

sys.path.append('../../rpythonic')
import rpythonic
rpythonic.set_cache('../.' )

rpythonic.wrap( 'libev', 
	header='/usr/local/include/ev.h',
	library_names=['libev'],
	strip_prefixes = ['ev_', 'EV_'],
	ctypes_footer = open('ctypes-footer.py','rb').read(),
)
