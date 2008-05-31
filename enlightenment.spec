#
%define		ecore_ver	0.9.9.038
%define		edje_ver	0.5.0.038
%define		eet_ver 	0.9.10.038
%define		embryo_ver	0.9.1.038
%define		evas_ver	0.9.9.038

Summary:	Enlightenment Window Manager
Summary(pl.UTF-8):	Zarządca okien X - Enlightenment
Name:		enlightenment
Version:	0.16.999.038
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	d54d8f7094b398fbd547992b8ad80cae
Source1:	%{name}-xsession.desktop
Source2:	enlightenmentDR17-wcnt.txt
Patch0:		enlightenmentDR17-module_temp_mac.patch
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
# ecore-evas ecore-config ecore-dbus ecore-file
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	edje >= %{edje_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	eet-devel >= %{eet_ver}
BuildRequires:	efreet-devel
BuildRequires:	embryo-devel >= %{embryo_ver}
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXext-devel
Requires:	fonts-TTF-bitstream-vera
Requires:	vfmg >= 0.9.95
Requires:	enlightenment-theme-default = %{version}
Requires:	enlightenment-init-default = %{version}
Requires:	evas-engine-buffer >= %{evas_ver}
Requires:	evas-engine-software_x11 >= %{evas_ver}
Requires:	evas-loader-eet >= %{evas_ver}
Requires:	evas-loader-jpeg >= %{evas_ver}
Requires:	evas-loader-png >= %{evas_ver}
Obsoletes:	enlightenmentDR17 >= 0.16.999
Obsoletes:	enlightenmentDR17-libs >= 0.16.999
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%{expand:%%define	_sysconfdir	%{_sysconfdir}/X11}
%undefine	__cxx

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl.UTF-8
Enlightenment jest najpotężniejszym i najpiękniejszym zarządcą okien
jaki kiedykolwiek został stworzony dla Linuksa ;)

%package module-cpufreq-freqset
Summary:	CPU speed management binary
Summary(pl.UTF-8):	Program do zaządzania szybkością CPU
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Obsoletes:	enlightenmentDR17-module-cpufreq-freqset >= 0.16.999

%description module-cpufreq-freqset
freqset makes you able to change CPU frequency using cpufreq module.

It contains SUID binary.

%description module-cpufreq-freqset -l pl.UTF-8
freqset pozwala zmieniać częstotliwość pracy procesora przy użyciu
modułu cpufreq.

Zawiera binarkę SUID.

%package devel
Summary:	Development headers for Enlightenment
Summary(pl.UTF-8):	Pliki nagłówkowe dla Enlightenmenta
Group:		Development/Libraries
# by headers included in e.h
# ecore-x ecore-evas ecore-con ecore-ipc ecore-job ecore-txt ecore-config ecore-file ecore-dbus
Requires:	ecore-devel >= %{ecore_ver}
Requires:	edje-devel >= %{edje_ver}
Requires:	eet-devel >= %{eet_ver}
Requires:	efreet-devel
Obsoletes:	enlightenmentDR17-devel >= 0.16.999

%description devel
Development headers for Enlightenment.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla Enlightenmenta.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--disable-valgrind \
	--with-profile=SLOW_PC
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/init/default.edj
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/themes/default.edj

install -d $RPM_BUILD_ROOT%{_libdir}/enlightenment/modules_extra
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/config-apps
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/wcnt.txt
find $RPM_BUILD_ROOT%{_libdir}/enlightenment -name '*.la' | xargs rm

cd $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts
VERA=$(ls Vera*.ttf)
for FONT in $VERA; do
	rm -f $FONT
	ln -s %{_fontsdir}/TTF/$FONT .
done
cd -

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README TODO
%attr(755,root,root) %{_bindir}/enlightenment
%attr(755,root,root) %{_bindir}/enlightenment_fm
%attr(755,root,root) %{_bindir}/enlightenment_imc
%attr(755,root,root) %{_bindir}/enlightenment_remote
%attr(755,root,root) %{_bindir}/enlightenment_start
# SETUID! allows rebooting, hibernating and shutting system down
%attr(4754,root,sys) %{_bindir}/enlightenment_sys
%attr(755,root,root) %{_bindir}/enlightenment_thumb
%dir %{_libdir}/enlightenment
%dir %{_libdir}/enlightenment/modules
%dir %{_libdir}/enlightenment/modules/*
%dir %{_libdir}/enlightenment/modules/*/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/*/linux-gnu-*/*.so
# should be in %{_datadir} (FHS)
%{_libdir}/enlightenment/modules/*/module.desktop
%{_libdir}/enlightenment/modules/*/e-module-*.edj
%dir %{_libdir}/enlightenment/modules_extra
%dir %{_libdir}/enlightenment/preload
%attr(755,root,root) %{_libdir}/enlightenment/preload/e_precache.so
%dir %{_sysconfdir}/enlightenment
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/enlightenment/sysactions.conf
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop

%files module-cpufreq-freqset
%defattr(644,root,root,755)
# what group should it be ?
%attr(4754,root,sys) %{_libdir}/enlightenment/modules/cpufreq/linux-gnu-*/freqset

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/enlightenment-config
%dir %{_includedir}/enlightenment
%{_includedir}/enlightenment/*.h
