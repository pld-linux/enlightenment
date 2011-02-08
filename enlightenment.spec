
%define		ecore_ver	1.0.0
%define		edje_ver	1.0.0
%define		eet_ver 	1.4.0
%define         embryo_ver      1.0.0
%define		evas_ver	1.0.0

Summary:	Enlightenment Window Manager
Summary(pl.UTF-8):	Zarządca okien X - Enlightenment
Name:		enlightenment
Version:	0.16.999.55225
Release:	0.1
License:	BSD
Group:		X11/Window Managers
Source0:	http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
# Source0-md5:	296e321c66e5819b21179307342e1d29
Source1:	%{name}-xsession.desktop
Source2:	enlightenmentDR17-wcnt.txt
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.6
# edbus, ehal
BuildRequires:	e_dbus-devel
# ecore ecore-file ecore-ipc ecore-con ecore-job ecore-imf
BuildRequires:	ecore-devel >= %{ecore_ver}
# ecore-evas ecore-imf-evas
BuildRequires:	ecore-evas-devel >= %{ecore_ver}
BuildRequires:	ecore-ipc-devel >= %{ecore_ver}
BuildRequires:	edje >= %{edje_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	eet-devel >= %{eet_ver}
# efreet efreet-mime
BuildRequires:	audit-libs-devel
BuildRequires:	efreet-devel
BuildRequires:	embryo-devel >= %{embryo_ver}
BuildRequires:	evas-devel >= %{evas_ver}
BuildRequires:	gettext-autopoint
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	libtool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXext-devel
Requires:	enlightenment-theme-default = %{version}
Requires:	evas-engine-buffer >= %{evas_ver}
Requires:	evas-engine-software_x11 >= %{evas_ver}
Requires:	evas-loader-eet >= %{evas_ver}
Requires:	evas-loader-jpeg >= %{evas_ver}
Requires:	evas-loader-png >= %{evas_ver}
Requires:	fonts-TTF-bitstream-vera
Requires:	vfmg >= 0.9.95
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
# ecore-x ecore-evas ecore-con ecore-ipc ecore-job ecore-txt ecore-config ecore-file
Requires:	ecore-devel >= %{ecore_ver}
Requires:	ecore-evas-devel >= %{ecore_ver}
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

%build
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--disable-valgrind \
	--with-profile=SLOW_PC
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/data/themes/default.edj

install -d $RPM_BUILD_ROOT%{_libdir}/enlightenment/modules_extra
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/config-apps
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/wcnt.txt
find $RPM_BUILD_ROOT%{_libdir}/enlightenment -name '*.la' | xargs rm

#cd $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts
#VERA=$(ls Vera*.ttf)
#for FONT in $VERA; do
#	rm -f $FONT
#	ln -s %{_fontsdir}/TTF/$FONT .
#done
#cd -

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_sysconfdir}/enlightenment
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/enlightenment/sysactions.conf
%attr(755,root,root) %{_bindir}/enlightenment
#%attr(755,root,root) %{_bindir}/enlightenment_init
%attr(755,root,root) %{_bindir}/enlightenment_imc
%attr(755,root,root) %{_bindir}/enlightenment_remote
%attr(755,root,root) %{_bindir}/enlightenment_start
%dir %{_libdir}/enlightenment
%dir %{_libdir}/enlightenment/modules
#
%dir %{_libdir}/enlightenment/modules/battery
%{_libdir}/enlightenment/modules/battery/e-module-battery.edj
%dir %{_libdir}/enlightenment/modules/battery/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/battery/linux-gnu-*/batget
%attr(755,root,root) %{_libdir}/enlightenment/modules/battery/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/battery/module.desktop
#
%dir %{_libdir}/enlightenment/modules/bluez
%{_libdir}/enlightenment/modules/bluez/e-module-bluez.edj
%dir %{_libdir}/enlightenment/modules/bluez/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/bluez/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/bluez/module.desktop
#
%dir %{_libdir}/enlightenment/modules/clock
%{_libdir}/enlightenment/modules/clock/e-module-clock.edj
%dir %{_libdir}/enlightenment/modules/clock/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/clock/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/clock/module.desktop
#
%dir %{_libdir}/enlightenment/modules/comp
%{_libdir}/enlightenment/modules/comp/e-module-comp.edj
%dir %{_libdir}/enlightenment/modules/comp/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/comp/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/comp/module.desktop
%{_libdir}/enlightenment/modules/comp/shadow.edj
#
%dir %{_libdir}/enlightenment/modules/conf
%{_libdir}/enlightenment/modules/conf/e-module-conf.edj
%dir %{_libdir}/enlightenment/modules/conf/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_acpibindings
%dir %{_libdir}/enlightenment/modules/conf_acpibindings/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_acpibindings/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_acpibindings/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_applications
%{_libdir}/enlightenment/modules/conf_applications/e-module-conf_applications.edj
%dir %{_libdir}/enlightenment/modules/conf_applications/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_applications/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_applications/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_borders
%{_libdir}/enlightenment/modules/conf_borders/e-module-conf_borders.edj
%dir %{_libdir}/enlightenment/modules/conf_borders/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_borders/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_borders/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_clientlist
%{_libdir}/enlightenment/modules/conf_clientlist/e-module-conf_clientlist.edj
%dir %{_libdir}/enlightenment/modules/conf_clientlist/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_clientlist/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_clientlist/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_colors
%{_libdir}/enlightenment/modules/conf_colors/e-module-conf_colors.edj
%dir %{_libdir}/enlightenment/modules/conf_colors/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_colors/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_colors/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_desk
%{_libdir}/enlightenment/modules/conf_desk/e-module-conf_desk.edj
%dir %{_libdir}/enlightenment/modules/conf_desk/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_desk/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_desk/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_desklock
%{_libdir}/enlightenment/modules/conf_desklock/e-module-conf_desklock.edj
%dir %{_libdir}/enlightenment/modules/conf_desklock/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_desklock/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_desklock/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_desks
%{_libdir}/enlightenment/modules/conf_desks/e-module-conf_desks.edj
%dir %{_libdir}/enlightenment/modules/conf_desks/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_desks/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_desks/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_dialogs
%{_libdir}/enlightenment/modules/conf_dialogs/e-module-conf_dialogs.edj
%dir %{_libdir}/enlightenment/modules/conf_dialogs/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_dialogs/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_dialogs/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_display
%{_libdir}/enlightenment/modules/conf_display/e-module-conf_display.edj
%dir %{_libdir}/enlightenment/modules/conf_display/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_display/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_display/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_dpms
%{_libdir}/enlightenment/modules/conf_dpms/e-module-conf_dpms.edj
%dir %{_libdir}/enlightenment/modules/conf_dpms/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_dpms/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_dpms/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_edgebindings
%{_libdir}/enlightenment/modules/conf_edgebindings/e-module-conf_edgebindings.edj
%dir %{_libdir}/enlightenment/modules/conf_edgebindings/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_edgebindings/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_edgebindings/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_engine
%{_libdir}/enlightenment/modules/conf_engine/e-module-conf_engine.edj
%dir %{_libdir}/enlightenment/modules/conf_engine/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_engine/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_engine/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_fonts
%dir %{_libdir}/enlightenment/modules/conf_fonts/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_fonts/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_fonts/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_icon_theme
%{_libdir}/enlightenment/modules/conf_icon_theme/e-module-conf_icon_theme.edj
%dir %{_libdir}/enlightenment/modules/conf_icon_theme/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_icon_theme/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_icon_theme/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_imc
%{_libdir}/enlightenment/modules/conf_imc/e-module-conf_imc.edj
%dir %{_libdir}/enlightenment/modules/conf_imc/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_imc/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_imc/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_interaction
%{_libdir}/enlightenment/modules/conf_interaction/e-module-conf_interaction.edj
%dir %{_libdir}/enlightenment/modules/conf_interaction/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_interaction/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_interaction/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_intl
%{_libdir}/enlightenment/modules/conf_intl/e-module-conf_intl.edj
%dir %{_libdir}/enlightenment/modules/conf_intl/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_intl/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_intl/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_keybindings
%dir %{_libdir}/enlightenment/modules/conf_keybindings/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_keybindings/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_keybindings/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_menus
%{_libdir}/enlightenment/modules/conf_menus/e-module-conf_menus.edj
%dir %{_libdir}/enlightenment/modules/conf_menus/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_menus/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_menus/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_mime
%{_libdir}/enlightenment/modules/conf_mime/e-module-conf_mime.edj
%dir %{_libdir}/enlightenment/modules/conf_mime/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_mime/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_mime/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_mouse
%{_libdir}/enlightenment/modules/conf_mouse/e-module-conf_mouse.edj
%dir %{_libdir}/enlightenment/modules/conf_mouse/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_mouse/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_mouse/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_mouse_cursor
%{_libdir}/enlightenment/modules/conf_mouse_cursor/e-module-conf_mouse_cursor.edj
%dir %{_libdir}/enlightenment/modules/conf_mouse_cursor/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_mouse_cursor/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_mouse_cursor/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_mousebindings
%{_libdir}/enlightenment/modules/conf_mousebindings/e-module-conf_mousebindings.edj
%dir %{_libdir}/enlightenment/modules/conf_mousebindings/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_mousebindings/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_mousebindings/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_paths
%{_libdir}/enlightenment/modules/conf_paths/e-module-conf_paths.edj
%dir %{_libdir}/enlightenment/modules/conf_paths/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_paths/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_paths/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_performance
%{_libdir}/enlightenment/modules/conf_performance/e-module-conf_performance.edj
%dir %{_libdir}/enlightenment/modules/conf_performance/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_performance/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_performance/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_profiles
%{_libdir}/enlightenment/modules/conf_profiles/e-module-conf_profiles.edj
%dir %{_libdir}/enlightenment/modules/conf_profiles/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_profiles/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_profiles/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_scale
%{_libdir}/enlightenment/modules/conf_scale/e-module-conf_scale.edj
%dir %{_libdir}/enlightenment/modules/conf_scale/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_scale/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_scale/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_screensaver
%dir %{_libdir}/enlightenment/modules/conf_screensaver/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_screensaver/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_screensaver/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_shelves
%{_libdir}/enlightenment/modules/conf_shelves/e-module-conf_shelves.edj
%dir %{_libdir}/enlightenment/modules/conf_shelves/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_shelves/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_shelves/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_startup
%{_libdir}/enlightenment/modules/conf_startup/e-module-conf_startup.edj
%dir %{_libdir}/enlightenment/modules/conf_startup/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_startup/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_startup/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_theme
%dir %{_libdir}/enlightenment/modules/conf_theme/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_theme/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_theme/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_transitions
%{_libdir}/enlightenment/modules/conf_transitions/e-module-conf_transitions.edj
%dir %{_libdir}/enlightenment/modules/conf_transitions/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_transitions/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_transitions/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_wallpaper
%dir %{_libdir}/enlightenment/modules/conf_wallpaper/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_wallpaper/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_wallpaper/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_wallpaper2
%dir %{_libdir}/enlightenment/modules/conf_wallpaper2/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_wallpaper2/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_wallpaper2/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_display
%{_libdir}/enlightenment/modules/conf_window_display/e-module-conf_window_display.edj
%dir %{_libdir}/enlightenment/modules/conf_window_display/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_window_display/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_window_display/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_focus
%{_libdir}/enlightenment/modules/conf_window_focus/e-module-conf_window_focus.edj
%dir %{_libdir}/enlightenment/modules/conf_window_focus/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_window_focus/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_window_focus/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_manipulation
%{_libdir}/enlightenment/modules/conf_window_manipulation/e-module-conf_winmanip.edj
%dir %{_libdir}/enlightenment/modules/conf_window_manipulation/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_window_manipulation/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_window_manipulation/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_remembers
%{_libdir}/enlightenment/modules/conf_window_remembers/e-module-conf_window_remembers.edj
%dir %{_libdir}/enlightenment/modules/conf_window_remembers/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_window_remembers/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_window_remembers/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_winlist
%{_libdir}/enlightenment/modules/conf_winlist/e-module-conf_winlist.edj
%dir %{_libdir}/enlightenment/modules/conf_winlist/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_winlist/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_winlist/module.desktop
#
%dir %{_libdir}/enlightenment/modules/connman
%{_libdir}/enlightenment/modules/connman/e-module-connman.edj
%dir %{_libdir}/enlightenment/modules/connman/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/connman/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/connman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/cpufreq
%{_libdir}/enlightenment/modules/cpufreq/e-module-cpufreq.edj
%dir %{_libdir}/enlightenment/modules/cpufreq/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/cpufreq/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/cpufreq/module.desktop
#
%dir %{_libdir}/enlightenment/modules/dropshadow
%{_libdir}/enlightenment/modules/dropshadow/e-module-dropshadow.edj
%dir %{_libdir}/enlightenment/modules/dropshadow/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/dropshadow/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/dropshadow/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything-apps
%{_libdir}/enlightenment/modules/everything-apps/e-module.edj
%dir %{_libdir}/enlightenment/modules/everything-apps/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything-apps/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/everything-apps/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything-aspell
%dir %{_libdir}/enlightenment/modules/everything-aspell/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything-aspell/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/everything-aspell/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything-calc
%dir %{_libdir}/enlightenment/modules/everything-calc/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything-calc/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/everything-calc/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything-files
%dir %{_libdir}/enlightenment/modules/everything-files/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything-files/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/everything-files/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything-settings
%dir %{_libdir}/enlightenment/modules/everything-settings/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything-settings/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/everything-settings/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything-windows
%dir %{_libdir}/enlightenment/modules/everything-windows/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything-windows/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/everything-windows/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything
%{_libdir}/enlightenment/modules/everything/e-module-everything.edj
%dir %{_libdir}/enlightenment/modules/everything/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/everything/module.desktop
#
%dir %{_libdir}/enlightenment/modules/fileman
%{_libdir}/enlightenment/modules/fileman/e-module-fileman.edj
%dir %{_libdir}/enlightenment/modules/fileman/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/fileman/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/fileman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/fileman_opinfo
%{_libdir}/enlightenment/modules/fileman_opinfo/e-module-fileman_opinfo.edj
%dir %{_libdir}/enlightenment/modules/fileman_opinfo/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/fileman_opinfo/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/fileman_opinfo/module.desktop
#
%dir %{_libdir}/enlightenment/modules/gadman
%{_libdir}/enlightenment/modules/gadman/e-module-gadman.edj
%dir %{_libdir}/enlightenment/modules/gadman/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/gadman/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/gadman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/ibar
%{_libdir}/enlightenment/modules/ibar/e-module-ibar.edj
%dir %{_libdir}/enlightenment/modules/ibar/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/ibar/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/ibar/module.desktop
#
%dir %{_libdir}/enlightenment/modules/ibox
%{_libdir}/enlightenment/modules/ibox/e-module-ibox.edj
%dir %{_libdir}/enlightenment/modules/ibox/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/ibox/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/ibox/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-bluetooth
%{_libdir}/enlightenment/modules/illume-bluetooth/e-module-illume-bluetooth.edj
%dir %{_libdir}/enlightenment/modules/illume-bluetooth/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-bluetooth/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-bluetooth/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-home-toggle
%{_libdir}/enlightenment/modules/illume-home-toggle/e-module-illume-home-toggle.edj
%dir %{_libdir}/enlightenment/modules/illume-home-toggle/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-home-toggle/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-home-toggle/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-home
%{_libdir}/enlightenment/modules/illume-home/e-module-illume-home.edj
%dir %{_libdir}/enlightenment/modules/illume-home/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-home/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-home/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-indicator
%{_libdir}/enlightenment/modules/illume-indicator/e-module-illume-indicator.edj
%dir %{_libdir}/enlightenment/modules/illume-indicator/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-indicator/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-indicator/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-kbd-toggle
%{_libdir}/enlightenment/modules/illume-kbd-toggle/e-module-illume-kbd-toggle.edj
%dir %{_libdir}/enlightenment/modules/illume-kbd-toggle/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-kbd-toggle/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-kbd-toggle/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-keyboard
%dir %{_libdir}/enlightenment/modules/illume-keyboard/dicts
%{_libdir}/enlightenment/modules/illume-keyboard/dicts/*.dic
%{_libdir}/enlightenment/modules/illume-keyboard/e-module-illume-keyboard.edj
%dir %{_libdir}/enlightenment/modules/illume-keyboard/keyboards
%{_libdir}/enlightenment/modules/illume-keyboard/keyboards/ignore_built_in_keyboards
%{_libdir}/enlightenment/modules/illume-keyboard/keyboards/*.kbd
%{_libdir}/enlightenment/modules/illume-keyboard/keyboards/*.png
%dir %{_libdir}/enlightenment/modules/illume-keyboard/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-keyboard/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-keyboard/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-mode-toggle
%{_libdir}/enlightenment/modules/illume-mode-toggle/e-module-illume-mode-toggle.edj
%dir %{_libdir}/enlightenment/modules/illume-mode-toggle/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-mode-toggle/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-mode-toggle/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-softkey
%{_libdir}/enlightenment/modules/illume-softkey/e-module-illume-softkey.edj
%dir %{_libdir}/enlightenment/modules/illume-softkey/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-softkey/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-softkey/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume
%dir %{_libdir}/enlightenment/modules/illume/dicts
%{_libdir}/enlightenment/modules/illume/dicts/*.dic
%{_libdir}/enlightenment/modules/illume/e-module-illume.edj
%dir %{_libdir}/enlightenment/modules/illume/keyboards
%{_libdir}/enlightenment/modules/illume/keyboards/ignore_built_in_keyboards
%{_libdir}/enlightenment/modules/illume/keyboards/*.kbd
%{_libdir}/enlightenment/modules/illume/keyboards/*.png
%dir %{_libdir}/enlightenment/modules/illume/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume/linux-gnu-*/wifiget
%{_libdir}/enlightenment/modules/illume/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume2
%{_libdir}/enlightenment/modules/illume2/e-module-illume2.edj
%dir %{_libdir}/enlightenment/modules/illume2/keyboards
%{_libdir}/enlightenment/modules/illume2/keyboards/ignore_built_in_keyboards
%dir %{_libdir}/enlightenment/modules/illume2/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume2/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume2/module.desktop
%dir %{_libdir}/enlightenment/modules/illume2/policies
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume2/policies/illume.so
#
%dir %{_libdir}/enlightenment/modules/mixer
%{_libdir}/enlightenment/modules/mixer/e-module-mixer.edj
%dir %{_libdir}/enlightenment/modules/mixer/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/mixer/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/mixer/module.desktop
#
%dir %{_libdir}/enlightenment/modules/msgbus
%{_libdir}/enlightenment/modules/msgbus/e-module-msgbus.edj
%dir %{_libdir}/enlightenment/modules/msgbus/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/msgbus/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/msgbus/module.desktop
#
%dir %{_libdir}/enlightenment/modules/ofono
%{_libdir}/enlightenment/modules/ofono/e-module-ofono.edj
%dir %{_libdir}/enlightenment/modules/ofono/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/ofono/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/ofono/module.desktop
#
%dir %{_libdir}/enlightenment/modules/pager
%{_libdir}/enlightenment/modules/pager/e-module-pager.edj
%dir %{_libdir}/enlightenment/modules/pager/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/pager/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/pager/module.desktop
#
%dir %{_libdir}/enlightenment/modules/start
%{_libdir}/enlightenment/modules/start/e-module-start.edj
%dir %{_libdir}/enlightenment/modules/start/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/start/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/start/module.desktop
#
%dir %{_libdir}/enlightenment/modules/syscon
%{_libdir}/enlightenment/modules/syscon/e-module-syscon.edj
%dir %{_libdir}/enlightenment/modules/syscon/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/syscon/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/syscon/module.desktop
#
%dir %{_libdir}/enlightenment/modules/systray
%{_libdir}/enlightenment/modules/systray/e-module-systray.edj
%dir %{_libdir}/enlightenment/modules/systray/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/systray/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/systray/module.desktop
#
%dir %{_libdir}/enlightenment/modules/temperature
%{_libdir}/enlightenment/modules/temperature/e-module-temperature.edj
%dir %{_libdir}/enlightenment/modules/temperature/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/temperature/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/temperature/linux-gnu-*/tempget
%{_libdir}/enlightenment/modules/temperature/module.desktop
#
%dir %{_libdir}/enlightenment/modules/winlist
%{_libdir}/enlightenment/modules/winlist/e-module-winlist.edj
%dir %{_libdir}/enlightenment/modules/winlist/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/winlist/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/winlist/module.desktop
#
%dir %{_libdir}/enlightenment/modules/wizard
%dir %{_libdir}/enlightenment/modules/wizard/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/wizard/linux-gnu-*/*.so
#
%dir %{_libdir}/enlightenment/preload
%attr(755,root,root) %{_libdir}/enlightenment/preload/e_precache.so
#
%dir %{_libdir}/enlightenment/utils
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_fm
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_fm_op
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_init
# SETUID ! allows rebooting, hibernating and shuting system down
%attr(4755,root,root) %{_libdir}/enlightenment/utils/enlightenment_sys
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_thumb
%{_datadir}/enlightenment
#
%{_datadir}/xsessions/enlightenment.desktop

%files module-cpufreq-freqset
%defattr(644,root,root,755)
# what group should it be ?
%attr(4754,root,sys) %{_libdir}/enlightenment/modules/cpufreq/linux-gnu-*/freqset

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/enlightenment-config
%dir %{_includedir}/enlightenment
%{_includedir}/enlightenment/*.h
%{_pkgconfigdir}/enlightenment.pc
%{_pkgconfigdir}/everything.pc
