Name: nagvis
Version: 1.8.5
Release: 0.eon
Summary: Nagios advanced map editor

Group: Applications/System
License: GPL
URL: http://www.nagvis.org/
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-eon.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: php, php-gd, php-mysql, php-mbstring, nagios, mk-livestatus, graphviz

# define path
%define eondir		/srv/eyesofnetwork
%define eonconfdir	/srv/eyesofnetworkconf/%{name}
%define datadir		%{eondir}/%{name}-%{version}
%define linkdir		%{eondir}/%{name}

# define user / group
%define NAGIOSUSR	nagios
%define APPLIANCEGRP	eyesofnetwork

%description
NagVis is a visualization addon for the well known network managment system Nagios.
NagVis can be used to visualize Nagios Data, e.g. to display IT processes like a mail 
system or a network infrastructure.

%prep
%setup -T -b 0 -n %{name}-%{version}
%setup -T -b 1 -n %{name}-eon

%install
cd ..
rm -rf %{buildroot}
install -d -m0755 %{buildroot}%{datadir}
install -d -m0755 %{buildroot}%{datadir}/etc/profiles
install -d -m0755 %{buildroot}%{datadir}/share/var
install -d -m0755 %{buildroot}%{datadir}/var/tmpl/cache
install -d -m0755 %{buildroot}%{datadir}/var/tmpl/compile
install -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
cp -afpvr %{name}-%{version}/* %{buildroot}%{datadir}
cp -afpvr  %{name}-%{version}/docs/en_US %{buildroot}%{datadir}/docs/fr_FR
mv %{buildroot}%{datadir}/docs/ %{buildroot}%{datadir}/share/

# eon specifics
install -d -m0755 %{buildroot}%{eonconfdir}
cp -afpvr %{name}-eon/* %{buildroot}%{eonconfdir}
cp -afpvr %{name}-eon/nagvis.ini.php %{buildroot}%{datadir}/etc/
rm -rf %{buildroot}%{datadir}/etc/auth.db
cp -afpvr %{name}-eon/auth.db %{buildroot}%{datadir}/etc/
rm -rf %{buildroot}%{datadir}/etc/maps/*
rm -rf %{buildroot}%{datadir}/share/userfiles/images/maps/*
install -D -m 0644 %{name}-eon/%{name}.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/%{name}.conf

%clean
rm -rf %{buildroot}

%post
ln -nsf %{datadir} %{linkdir}
chown -h %{NAGIOSUSR}:%{APPLIANCEGRP} %{linkdir}
chmod -R g+w %{datadir}*

%files
%defattr(-, root, root, 0755)
%{_sysconfdir}/httpd/conf.d/nagvis.conf
%{eonconfdir}
%defattr(-, %{NAGIOSUSR}, %{APPLIANCEGRP}, 0775)
%{datadir}

%changelog
* Mon Aug 17 2015 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.8.5-0.eon
- upgrade to version 1.8.5

* Mon May 18 2015 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.8.3-0.eon
- upgrade to version 1.8.3

* Mon Mar 30 2015 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.8.2-0.eon
- upgrade to version 1.8.2

* Tue May 20 2014 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.7.10-1.eon
- graphviz dependency fix

* Thu Mar 06 2014 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.7.10-0.eon
- packaged for EyesOfNetwork appliance 4.1

* Wed Jun 19 2013 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.7.9-0.eon
- packaged for EyesOfNetwork appliance 4.0

* Tue May 15 2012 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.6.6-0.eon
- upgrade to version 1.6.6

* Fri Apr 27 2012 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.6.5-0.eon
- upgrade to version 1.6.5

* Tue Feb 28 2012 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.6.4-0.eon
- upgrade to version 1.6.4

* Fri Feb 17 2012 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.6.3-0.eon
- upgrade to version 1.6.3

* Tue Jan 03 2012 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.6.2-0.eon
- upgrade to version 1.6.2

* Wed Dec 21 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.6.1-0.eon
- upgrade to version 1.6.1

* Mon Dec 12 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.6.0-0.eon
- upgrade to version 1.6.0

* Mon Aug 01 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.10-0.eon
- upgrade to version 1.5.10

* Tue May 24 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.9-0.eon
- upgrade to version 1.5.9

* Thu Feb 03 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.8-0.eon
- upgrade to version 1.5.8

* Wed Jan 19 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.7-0.eon
- upgrade to version 1.5.7

* Thu Jan 06 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.6-1.eon
- search module fix

* Mon Dec 13 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.6-0.eon
- upgrade to version 1.5.6

* Mon Nov 01 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.5-0.eon
- upgrade to version 1.5.5

* Sun Oct 24 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.4-0.eon
- upgrade to version 1.5.4

* Mon Oct 04 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.3-0.eon
- upgrade to version 1.5.3

* Fri Oct 01 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.2-0.eon
- upgrade to version 1.5.2

* Mon Sep 06 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.5.1-0.eon
- packaged for EyesOfNetwork appliance 2.2
- upgrade to version 1.5.1

* Wed Jul 28 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.7-1.eon
- packaged for EyesOfNetwork appliance 2.2

* Fri Apr 09 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.7-0.eon
- packaged for EyesOfNetwork appliance 2.1
- upgrade to version 1.4.7

* Mon Feb 08 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.6-0.eon
- upgrade to version 1.4.6
- apache setenv deleted

* Fri Nov 27 2009 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.5-0.eon
- upgrade to version 1.4.5

* Tue Oct 20 2009 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.4-0.eon
- upgrade to version 1.4.4

* Thu Sep 17 2009 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.3-0.eon
- upgrade to version 1.4.3

* Mon Aug 17 2009 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.2-0.eon
- upgrade to version 1.4.2

* Fri Jul 10 2009 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.1-0.eon
- upgrade to version 1.4.1

* Mon May 25 2009 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.4.0-0.eon
- packaged for EyesOfNetwork appliance 2.0

* Mon Feb 23 2009 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.3.2-1.eon
- states order modified in NagVisStatefulObject.php 

* Tue Nov 18 2008 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.3.2-0.eon
- packaged for EyesOfNetwork appliance

* Fri Oct 17 2008 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.3.1-0.eon
- packaged for EyesOfNetwork appliance
