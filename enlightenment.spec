# TODO: verify install time dependencies
#
# Conditonal build:
%bcond_without	systemd		# systemd (user session) support
%bcond_with	wayland		# Wayland clients in composite module
%bcond_with	wayland_egl	# Wayland clients EGL rendering
#
%define		efl_ver		1.8.3
%define		elementary_ver	1.8.2

Summary:	Enlightenment Window Manager
Summary(hu.UTF-8):	Enlightenment ablakkezelő
Summary(pl.UTF-8):	Zarządca okien X - Enlightenment
Name:		enlightenment
Version:	0.18.3
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	http://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.bz2
# Source0-md5:	1ce67de50f48f49e4803023f2426d997
Source1:	%{name}-xsession.desktop
Source2:	e-module-wl_desktop_shell.edj
Source3:	e-module-wl_screenshot.edj
Patch0:		%{name}-missing.patch
URL:		http://enlightenment.org/
BuildRequires:	alsa-lib-devel >= 1.0.8
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1:1.11
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	ecore-con-devel >= %{efl_ver}
BuildRequires:	ecore-devel >= %{efl_ver}
BuildRequires:	ecore-evas-devel >= %{efl_ver}
BuildRequires:	ecore-file-devel >= %{efl_ver}
BuildRequires:	ecore-input-devel >= %{efl_ver}
BuildRequires:	ecore-input-evas-devel >= %{efl_ver}
BuildRequires:	ecore-ipc-devel >= %{efl_ver}
BuildRequires:	ecore-x-devel >= %{efl_ver}
BuildRequires:	edje >= %{efl_ver}
BuildRequires:	edje-devel >= %{efl_ver}
BuildRequires:	eet-devel >= %{efl_ver}
BuildRequires:	eeze-devel >= %{efl_ver}
BuildRequires:	efreet-devel >= %{efl_ver}
BuildRequires:	eina-devel >= %{efl_ver}
BuildRequires:	eio-devel >= %{efl_ver}
BuildRequires:	eldbus-devel >= %{efl_ver}
BuildRequires:	elementary-devel >= %{elementary_ver}
BuildRequires:	elementary-devel < 1.8.99
BuildRequires:	emotion-devel >= %{efl_ver}
BuildRequires:	evas-devel >= %{efl_ver}
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	libtool >= 2:2
BuildRequires:	libxcb-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
%{?with_systemd:BuildRequires:	systemd-units >= 1:192}
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xkeyboard-config
%if %{with wayland}
%{?with_wayland_egl:BuildRequires:	Mesa-libEGL-devel >= 7.10}
BuildRequires:	pixman-devel >= 0.3
# wayland-server
BuildRequires:	wayland-devel >= 1.3.0
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.3.0
%endif
Requires:	alsa-lib >= 1.0.8
Requires:	ecore >= %{efl_ver}
Requires:	ecore-con >= %{efl_ver}
Requires:	ecore-evas >= %{efl_ver}
Requires:	ecore-file >= %{efl_ver}
Requires:	ecore-input >= %{efl_ver}
Requires:	ecore-input-evas >= %{efl_ver}
Requires:	ecore-ipc >= %{efl_ver}
Requires:	ecore-x >= %{efl_ver}
Requires:	edje-libs >= %{efl_ver}
Requires:	eet >= %{efl_ver}
Requires:	eeze >= %{efl_ver}
Requires:	efreet >= %{efl_ver}
Requires:	eina >= %{efl_ver}
Requires:	eio >= %{efl_ver}
Requires:	eldbus >= %{efl_ver}
Requires:	elementary >= %{elementary_ver}
Requires:	emotion >= %{efl_ver}
Requires:	evas >= %{efl_ver}
Requires:	evas-engine-software_x11 >= %{efl_ver}
Requires:	evas-loader-jpeg >= %{efl_ver}
Requires:	evas-loader-png >= %{efl_ver}
%{?with_systemd:Requires:	systemd-units >= 1:192}
%if %{with wayland}
%{?with_wayland_egl:Requires:	Mesa-libEGL >= 7.10}
Requires:	pixman >= 0.3
Requires:	wayland >= 1.3.0
Requires:	xorg-lib-libxkbcommon >= 0.3.0
%endif
Suggests:	vfmg >= 0.9.95
Obsoletes:	enlightenmentDR17
Obsoletes:	enlightenmentDR17-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description  -l hu.UTF-8
Enlightenment egy ablakkezelő, amely arra készült, hogy hatékony,
bővíthető, beállítható legyen, és tényleg jól nézzen ki.

%description -l pl.UTF-8
Enlightenment jest najpotężniejszym i najpiękniejszym zarządcą okien
jaki kiedykolwiek został stworzony dla Linuksa ;)

%package module-cpufreq-freqset
Summary:	CPU speed management binary
Summary(hu.UTF-8):	CPU sebesség menedzselő program
Summary(pl.UTF-8):	Program do zaządzania szybkością CPU
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Obsoletes:	enlightenmentDR17-module-cpufreq-freqset

%description module-cpufreq-freqset
freqset makes you able to change CPU frequency using cpufreq module.

It contains SUID binary.

%description module-cpufreq-freqset -l hu.UTF-8
freqset-tel lehetőséged van a CPU frekvenciáját változtatni a cpufreq
modul használatával.

SUID binárist tartalmaz.

%description module-cpufreq-freqset -l pl.UTF-8
freqset pozwala zmieniać częstotliwość pracy procesora przy użyciu
modułu cpufreq.

Zawiera binarkę SUID.

%package devel
Summary:	Development headers for Enlightenment
Summary(hu.UTF-8):	Fejlesztői fájlok Enlightenment-hez
Summary(pl.UTF-8):	Pliki nagłówkowe dla Enlightenmenta
Group:		Development/Libraries
# doesn't require base
Requires:	ecore-devel >= %{efl_ver}
Requires:	ecore-con-devel >= %{efl_ver}
Requires:	ecore-evas-devel >= %{efl_ver}
Requires:	ecore-file-devel >= %{efl_ver}
Requires:	ecore-input-devel >= %{efl_ver}
Requires:	ecore-input-evas-devel >= %{efl_ver}
Requires:	ecore-ipc-devel >= %{efl_ver}
Requires:	ecore-x-devel >= %{efl_ver}
Requires:	edje-devel >= %{efl_ver}
Requires:	eet-devel >= %{efl_ver}
Requires:	eeze-devel >= %{efl_ver}
Requires:	efreet-devel >= %{efl_ver}
Requires:	eina-devel >= %{efl_ver}
Requires:	eio-devel >= %{efl_ver}
Requires:	eldbus-devel >= %{efl_ver}
Requires:	elementary-devel >= %{elementary_ver}
Requires:	elementary-devel < 1.8.99
Requires:	emotion-devel >= %{efl_ver}
Requires:	evas-devel >= %{efl_ver}
Obsoletes:	enlightenmentDR17-devel

%description devel
Development headers for Enlightenment.

%description devel -l hu.UTF-8
Fejlesztői fájlok Enlightenment-hez.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla Enlightenmenta.

%prep
%setup -q
# missing files
%patch0 -p1
cp -p %{SOURCE2} src/modules/wl_desktop_shell
cp -p %{SOURCE3} src/modules/wl_screenshot

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	%{!?with_systemd:--disable-systemd} \
	%{?with_wayland:--enable-wayland-clients} \
	%{?with_wayland_egl:--enable-wayland-egl} \
	--with-profile=SLOW_PC
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

# recheck: still valid for E18?
install -d $RPM_BUILD_ROOT%{_libdir}/enlightenment/modules_extra
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/config-apps

find $RPM_BUILD_ROOT%{_libdir}/enlightenment -name '*.la' | xargs %{__rm}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
/etc/xdg/menus/enlightenment.menu
%dir %{_sysconfdir}/enlightenment
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/enlightenment/sysactions.conf
%attr(755,root,root) %{_bindir}/enlightenment
%attr(755,root,root) %{_bindir}/enlightenment_filemanager
%attr(755,root,root) %{_bindir}/enlightenment_imc
%attr(755,root,root) %{_bindir}/enlightenment_open
%attr(755,root,root) %{_bindir}/enlightenment_remote
%attr(755,root,root) %{_bindir}/enlightenment_start
%if %{with systemd}
%{_prefix}/lib/systemd/user/e18.service
%endif
%dir %{_libdir}/enlightenment
%dir %{_libdir}/enlightenment/modules
%dir %{_libdir}/enlightenment/modules_extra
#
%dir %{_libdir}/enlightenment/modules/access
%dir %{_libdir}/enlightenment/modules/access/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/access/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/access/module.desktop
#
%dir %{_libdir}/enlightenment/modules/appmenu
%{_libdir}/enlightenment/modules/appmenu/e-module-appmenu.edj
%dir %{_libdir}/enlightenment/modules/appmenu/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/appmenu/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/appmenu/module.desktop
#
%dir %{_libdir}/enlightenment/modules/backlight
%{_libdir}/enlightenment/modules/backlight/e-module-backlight.edj
%dir %{_libdir}/enlightenment/modules/backlight/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/backlight/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/backlight/module.desktop
#
%dir %{_libdir}/enlightenment/modules/battery
%{_libdir}/enlightenment/modules/battery/e-module-battery.edj
%dir %{_libdir}/enlightenment/modules/battery/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/battery/linux-gnu-*/batget
%attr(755,root,root) %{_libdir}/enlightenment/modules/battery/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/battery/module.desktop
#
%dir %{_libdir}/enlightenment/modules/bluez4
%{_libdir}/enlightenment/modules/bluez4/e-module-bluez4.edj
%dir %{_libdir}/enlightenment/modules/bluez4/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/bluez4/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/bluez4/module.desktop
#
%dir %{_libdir}/enlightenment/modules/clock
%{_libdir}/enlightenment/modules/clock/e-module-clock.edj
%dir %{_libdir}/enlightenment/modules/clock/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/clock/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/clock/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf
%{_libdir}/enlightenment/modules/conf/e-module-conf.edj
%dir %{_libdir}/enlightenment/modules/conf/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_applications
%{_libdir}/enlightenment/modules/conf_applications/e-module-conf_applications.edj
%dir %{_libdir}/enlightenment/modules/conf_applications/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_applications/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_applications/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_bindings
%dir %{_libdir}/enlightenment/modules/conf_bindings/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_bindings/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_bindings/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_comp
%dir %{_libdir}/enlightenment/modules/conf_comp/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_comp/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_comp/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_dialogs
%{_libdir}/enlightenment/modules/conf_dialogs/e-module-conf_dialogs.edj
%dir %{_libdir}/enlightenment/modules/conf_dialogs/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_dialogs/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_dialogs/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_display
%dir %{_libdir}/enlightenment/modules/conf_display/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_display/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_display/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_interaction
%{_libdir}/enlightenment/modules/conf_interaction/e-module-conf_interaction.edj
%dir %{_libdir}/enlightenment/modules/conf_interaction/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_interaction/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_interaction/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_intl
%dir %{_libdir}/enlightenment/modules/conf_intl/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_intl/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_intl/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_menus
%{_libdir}/enlightenment/modules/conf_menus/e-module-conf_menus.edj
%dir %{_libdir}/enlightenment/modules/conf_menus/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_menus/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_menus/module.desktop
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
%dir %{_libdir}/enlightenment/modules/conf_randr
%{_libdir}/enlightenment/modules/conf_randr/e-module-conf_randr.edj
%dir %{_libdir}/enlightenment/modules/conf_randr/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_randr/linux-*/module.so
%{_libdir}/enlightenment/modules/conf_randr/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_shelves
%{_libdir}/enlightenment/modules/conf_shelves/e-module-conf_shelves.edj
%dir %{_libdir}/enlightenment/modules/conf_shelves/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_shelves/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_shelves/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_theme
%dir %{_libdir}/enlightenment/modules/conf_theme/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_theme/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_theme/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_wallpaper2
%dir %{_libdir}/enlightenment/modules/conf_wallpaper2/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_wallpaper2/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/conf_wallpaper2/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_manipulation
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
%dir %{_libdir}/enlightenment/modules/connman
%{_libdir}/enlightenment/modules/connman/e-module-connman.edj
%dir %{_libdir}/enlightenment/modules/connman/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/connman/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/connman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/contact
%{_libdir}/enlightenment/modules/contact/e-module-contact.edj
%dir %{_libdir}/enlightenment/modules/contact/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/contact/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/contact/module.desktop
#
%dir %{_libdir}/enlightenment/modules/cpufreq
%{_libdir}/enlightenment/modules/cpufreq/e-module-cpufreq.edj
%dir %{_libdir}/enlightenment/modules/cpufreq/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/cpufreq/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/cpufreq/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything
%{_libdir}/enlightenment/modules/everything/e-module-everything-start.edj
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
%dir %{_libdir}/enlightenment/modules/illume-home
%{_libdir}/enlightenment/modules/illume-home/e-module-illume-home.edj
%dir %{_libdir}/enlightenment/modules/illume-home/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-home/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-home/module.desktop
#
%dir %{_libdir}/enlightenment/modules/illume-home-toggle
%{_libdir}/enlightenment/modules/illume-home-toggle/e-module-illume-home-toggle.edj
%dir %{_libdir}/enlightenment/modules/illume-home-toggle/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume-home-toggle/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume-home-toggle/module.desktop
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
%dir %{_libdir}/enlightenment/modules/illume2
%{_libdir}/enlightenment/modules/illume2/e-module-illume2.edj
%dir %{_libdir}/enlightenment/modules/illume2/keyboards
%{_libdir}/enlightenment/modules/illume2/keyboards/ignore_built_in_keyboards
%dir %{_libdir}/enlightenment/modules/illume2/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume2/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/illume2/module.desktop
%dir %{_libdir}/enlightenment/modules/illume2/policies
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume2/policies/illume.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/illume2/policies/tablet.so
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
%dir %{_libdir}/enlightenment/modules/music-control
%{_libdir}/enlightenment/modules/music-control/e-module-music-control.edj
%dir %{_libdir}/enlightenment/modules/music-control/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/music-control/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/music-control/module.desktop
#
%dir %{_libdir}/enlightenment/modules/notification
%{_libdir}/enlightenment/modules/notification/e-module-notification.edj
%dir %{_libdir}/enlightenment/modules/notification/linux-*
%attr(755,root,root)  %{_libdir}/enlightenment/modules/notification/linux-*/module.so
%{_libdir}/enlightenment/modules/notification/module.desktop
#
%dir %{_libdir}/enlightenment/modules/pager
%{_libdir}/enlightenment/modules/pager/e-module-pager.edj
%dir %{_libdir}/enlightenment/modules/pager/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/pager/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/pager/module.desktop
#
%dir %{_libdir}/enlightenment/modules/quickaccess
%{_libdir}/enlightenment/modules/quickaccess/e-module-quickaccess.edj
%dir %{_libdir}/enlightenment/modules/quickaccess/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/quickaccess/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/quickaccess/module.desktop
#
%dir %{_libdir}/enlightenment/modules/shot
%{_libdir}/enlightenment/modules/shot/e-module-shot.edj
%dir %{_libdir}/enlightenment/modules/shot/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/shot/linux-*/module.so
%{_libdir}/enlightenment/modules/shot/module.desktop
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
%dir %{_libdir}/enlightenment/modules/tasks
%{_libdir}/enlightenment/modules/tasks/e-module-tasks.edj
%dir %{_libdir}/enlightenment/modules/tasks/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/tasks/linux-*/module.so
%{_libdir}/enlightenment/modules/tasks/module.desktop
#
%dir %{_libdir}/enlightenment/modules/teamwork
%{_libdir}/enlightenment/modules/teamwork/e-module-teamwork.edj
%dir %{_libdir}/enlightenment/modules/teamwork/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/teamwork/linux-*/module.so
%{_libdir}/enlightenment/modules/teamwork/module.desktop
#
%dir %{_libdir}/enlightenment/modules/temperature
%{_libdir}/enlightenment/modules/temperature/e-module-temperature.edj
%dir %{_libdir}/enlightenment/modules/temperature/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/temperature/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/temperature/linux-gnu-*/tempget
%{_libdir}/enlightenment/modules/temperature/module.desktop
#
%dir %{_libdir}/enlightenment/modules/tiling
%{_libdir}/enlightenment/modules/tiling/e-module-tiling.edj
%dir %{_libdir}/enlightenment/modules/tiling/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/tiling/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/tiling/module.desktop
#
%dir %{_libdir}/enlightenment/modules/winlist
%{_libdir}/enlightenment/modules/winlist/e-module-winlist.edj
%dir %{_libdir}/enlightenment/modules/winlist/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/winlist/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/winlist/module.desktop
#
%dir %{_libdir}/enlightenment/modules/wizard
%dir %{_libdir}/enlightenment/modules/wizard/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/wizard/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/wizard/linux-gnu-*/page_*.so
%{_libdir}/enlightenment/modules/wizard/def-ibar.txt
%{_libdir}/enlightenment/modules/wizard/desktop
#
%if %{with wayland}
%dir %{_libdir}/enlightenment/modules/wl_desktop_shell
%dir %{_libdir}/enlightenment/modules/wl_desktop_shell/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/module.desktop
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/*.edj
%dir %{_libdir}/enlightenment/modules/wl_screenshot
%dir %{_libdir}/enlightenment/modules/wl_screenshot/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_screenshot/linux-gnu-*/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_screenshot/module.desktop
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_screenshot/*.edj
%endif
#
%dir %{_libdir}/enlightenment/modules/xkbswitch
%{_libdir}/enlightenment/modules/xkbswitch/e-module-xkbswitch.edj
%dir %{_libdir}/enlightenment/modules/xkbswitch/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/xkbswitch/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/xkbswitch/module.desktop
#
%dir %{_libdir}/enlightenment/utils
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_alert
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_backlight
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_fm
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_fm_op
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_static_grabber
# SETUID root: allows rebooting, hibernating and shuting system down
%attr(4755,root,root) %{_libdir}/enlightenment/utils/enlightenment_sys
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_thumb
%{_datadir}/enlightenment
%{_desktopdir}/enlightenment_filemanager.desktop
%{_datadir}/xsessions/enlightenment.desktop

%files module-cpufreq-freqset
%defattr(644,root,root,755)
# what group should it be ?
%attr(4754,root,sys) %{_libdir}/enlightenment/modules/cpufreq/linux-gnu-*/freqset

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/enlightenment
%{_includedir}/enlightenment/e.h
%{_includedir}/enlightenment/e_*.h
%{_includedir}/enlightenment/evry_*.h
%{_pkgconfigdir}/enlightenment.pc
%{_pkgconfigdir}/everything.pc
