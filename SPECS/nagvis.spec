Name: nagvis
Version: 1.8.5
Release: 5.rgm
Summary: Nagios advanced map editor

Group: Applications/System
License: GPL
URL: http://www.nagvis.org/
Source0: %{name}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: php, php-gd, php-mysqlnd, php-mbstring, nagios, mk-livestatus, graphviz, rgm-base
BuildRequires: rpm-macros-rgm

# define path
%define datadir		%{rgm_path}/%{name}-%{version}
%define linkdir		%{rgm_path}/%{name}


%description
NagVis is a visualization addon for the well known network managment system Nagios.
NagVis can be used to visualize Nagios Data, e.g. to display IT processes like a mail
system or a network infrastructure.

%prep
%setup -T -b 0 -n %{name}

%install
cd ..
rm -rf %{buildroot}
install -d -m0755 %{buildroot}%{datadir}
install -d -m0755 %{buildroot}%{datadir}/etc/profiles
install -d -m0755 %{buildroot}%{datadir}/share/var
install -d -m0755 %{buildroot}%{datadir}/var/tmpl/cache
install -d -m0755 %{buildroot}%{datadir}/var/tmpl/compile
install -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
cp -afpvr %{name}/* %{buildroot}%{datadir}
cp -afpvr  %{name}/docs/en_US %{buildroot}%{datadir}/docs/fr_FR
mv %{buildroot}%{datadir}/docs/ %{buildroot}%{datadir}/share/

# RGM specifics
install -d -m0755 %{buildroot}%{rgm_docdir}/%{name}

rm -rf %{buildroot}%{datadir}/etc/auth.db
rm -rf %{buildroot}%{datadir}/etc/maps/*
rm -rf %{buildroot}%{datadir}/share/userfiles/images/maps/*

install -D -m 0644 %{_sourcedir}/%{name}-rgm/nagvis.ini.php  %{buildroot}%{rgm_docdir}/%{name}/nagvis.ini.php
install -D -m 0644 %{_sourcedir}/%{name}-rgm/nagvis.ini.php %{buildroot}%{datadir}/etc/nagvis.ini.php
install -d -m0755 %{buildroot}%{rgm_docdir}/httpd
install -D -m 0644 %{_sourcedir}/%{name}-rgm/httpd-nagvis.example.conf %{buildroot}%{rgm_docdir}/httpd/


%clean
rm -rf %{buildroot}


%pre
# create RGM system group if it doesn't already exists
/usr/sbin/groupadd -r %{rgm_group} >/dev/null 2>&1 || :


%post
ln -nsf %{datadir} %{linkdir}
chown -h %{rgm_user_nagios}:%{rgm_group} %{linkdir}
chmod -R g+w %{datadir}*
if [ -e %{_sysconfdir}/httpd/conf.d/15_%{name}.conf ]; then
    rm -f %{_sysconfdir}/httpd/conf.d/15_%{name}.conf
fi
# execute SQL postinstall script
/usr/share/rgm/manage_sql.sh -d %{rgm_db_nagvis} -u %{rgm_sql_internal_user} -p %{rgm_sql_internal_pwd}


%files
%doc %{rgm_docdir}/%{name}
%doc %{rgm_docdir}/httpd/httpd-nagvis.example.conf
%defattr(0640, %{rgm_user_nagios}, %{rgm_group}, 0775)
%config(noreplace) %{datadir}/etc
%defattr(-, %{rgm_user_nagios}, %{rgm_group}, 0775)
%{datadir}


%changelog
* Tue Apr 25 2023 Vincent Fricou <vfricou@fr.scc.com> - 1.8.5-5.rgm
- fix requirement to php-mysqlnd

* Thu Mar 11 2021 Eric Belhomme <ebelhomme@fr.scc.com> - 1.8.5-4.rgm
- move httpd config file as example file in /usr/share/doc/rgm/httpd/

* Thu Oct 22 2020 Eric Belhomme <ebelhomme@fr.scc.com> - 1.8.5-3.rgm
- fix authorization module to MySQL backend

* Thu Apr 18 2019 Eric Belhomme <ebelhomme@fr.scc.com> - 1.8.5-2.rgm
- replaced default sqlite auth backend with mysql auth backend
- added auth_mysql section on config file
- create empty DB on post section

* Tue Mar 19 2019 Eric Belhomme <ebelhomme@fr.scc.com> - 1.8.5-1.rgm
- use of rpm-macros-rgm
- fix apache config file
- fix ownerships

* Fri Feb 22 2019 Michael Aubertin <maubertin@fr.scc.com> - 1.8.5-0.rgm
- Initial fork

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