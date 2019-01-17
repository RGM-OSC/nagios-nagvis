#!/bin/sh

# define path
eondir="/srv/eyesofnetwork"
eonconfdir="/srv/eyesofnetworkconf/nagvis"
datadir="${eondir}/nagvis"

# user / group
APPLIANCEGRP="eyesofnetwork"
chown -R nagios:${APPLIANCEGRP} ${datadir}*
chmod -R g+w ${datadir}*

# graphviz
if [ -f "/usr/bin/dot" ]; then
	/usr/bin/dot -c
fi
