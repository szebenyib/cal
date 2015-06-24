__author__ = 'szebenyib'

import gback
session = gback.GCalSession(oauthfn='gback.oauth',
                            clientfn='logger_google_key.json')
for c in session.names: print c