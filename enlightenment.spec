# TODO: verify install time dependencies
#
# Conditonal build:
%bcond_without	systemd		# systemd (user session) support
%bcond_without	wayland		# Wayland clients in composite module
#
%define		efl_ver		1.27.0

Summary:	Enlightenment Window Manager
Summary(hu.UTF-8):	Enlightenment ablakkezelő
Summary(pl.UTF-8):	Zarządca okien X - Enlightenment
Name:		enlightenment
Version:	0.26.0
Release:	0.1
License:	BSD
Group:		X11/Window Managers
Source0:	https://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.xz
# Source0-md5:	17cbf0f2dfe419019cc90f4392d9980d
URL:		https://www.enlightenment.org/
BuildRequires:	alsa-lib-devel >= 1.0.8
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	efl-devel >= %{efl_ver}
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	libxcb-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
%{?with_systemd:BuildRequires:	systemd-units >= 1:192}
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xkeyboard-config
%if %{with wayland}
BuildRequires:	pixman-devel >= 0.3
# wayland-server
BuildRequires:	wayland-devel >= 1.3.0
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.3.0
BuildRequires:	xorg-xserver-Xwayland
%endif
Requires:	alsa-lib >= 1.0.8
Requires:	efl >= %{efl_ver}
%{?with_systemd:Requires:	systemd-units >= 1:192}
%if %{with wayland}
Requires:	pixman >= 0.3
Requires:	wayland >= 1.3.0
Requires:	xorg-lib-libxkbcommon >= 0.3.0
%endif
Suggests:	vfmg >= 0.9.95
Obsoletes:	enlightenment-module-cpufreq-freqset < 0.26.0
Obsoletes:	enlightenmentDR17
Obsoletes:	enlightenmentDR17-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%define		arch_tag	linux-gnu-*-%{version}

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description  -l hu.UTF-8
Enlightenment egy ablakkezelő, amely arra készült, hogy hatékony,
bővíthető, beállítható legyen, és tényleg jól nézzen ki.

%description -l pl.UTF-8
Enlightenment jest najpotężniejszym i najpiękniejszym zarządcą okien
jaki kiedykolwiek został stworzony dla Linuksa ;)

%package devel
Summary:	Development headers for Enlightenment
Summary(hu.UTF-8):	Fejlesztői fájlok Enlightenment-hez
Summary(pl.UTF-8):	Pliki nagłówkowe dla Enlightenmenta
Group:		Development/Libraries
# doesn't require base
Requires:	efl-devel >= %{efl_ver}
Obsoletes:	enlightenmentDR17-devel

%description devel
Development headers for Enlightenment.

%description devel -l hu.UTF-8
Fejlesztői fájlok Enlightenment-hez.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla Enlightenmenta.

%prep
%setup -q

%build
%meson build \
	%{!?with_systemd:-Dsystemd=false} \
	%{?with_wayland:-Dwl=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.md
/etc/xdg/menus/e-applications.menu
%dir %{_sysconfdir}/enlightenment
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/enlightenment/sysactions.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/enlightenment/system.conf
%attr(755,root,root) %{_bindir}/emixer
%attr(755,root,root) %{_bindir}/enlightenment
%attr(755,root,root) %{_bindir}/enlightenment_askpass
%attr(755,root,root) %{_bindir}/enlightenment_filemanager
%attr(755,root,root) %{_bindir}/enlightenment_fprint
%attr(755,root,root) %{_bindir}/enlightenment_imc
%attr(755,root,root) %{_bindir}/enlightenment_open
%attr(755,root,root) %{_bindir}/enlightenment_paledit
%attr(755,root,root) %{_bindir}/enlightenment_remote
%attr(755,root,root) %{_bindir}/enlightenment_start
%if %{with systemd}
%{_prefix}/lib/systemd/user/enlightenment.service
%endif
%dir %{_libdir}/enlightenment
%dir %{_libdir}/enlightenment/modules
#
%dir %{_libdir}/enlightenment/modules/appmenu
%{_libdir}/enlightenment/modules/appmenu/e-module-appmenu.edj
%dir %{_libdir}/enlightenment/modules/appmenu/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/appmenu/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/appmenu/module.desktop
#
%dir %{_libdir}/enlightenment/modules/backlight
%{_libdir}/enlightenment/modules/backlight/e-module-backlight.edj
%dir %{_libdir}/enlightenment/modules/backlight/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/backlight/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/backlight/module.desktop
#
%dir %{_libdir}/enlightenment/modules/battery
%{_libdir}/enlightenment/modules/battery/e-module-battery.edj
%dir %{_libdir}/enlightenment/modules/battery/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/battery/%{arch_tag}/batget
%attr(755,root,root) %{_libdir}/enlightenment/modules/battery/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/battery/module.desktop
#
%dir %{_libdir}/enlightenment/modules/bluez5
%{_libdir}/enlightenment/modules/bluez5/e-module-bluez5.edj
%dir %{_libdir}/enlightenment/modules/bluez5/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/bluez5/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/bluez5/module.desktop
#
%dir %{_libdir}/enlightenment/modules/clock
%{_libdir}/enlightenment/modules/clock/e-module-clock.edj
%dir %{_libdir}/enlightenment/modules/clock/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/clock/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/clock/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf
%{_libdir}/enlightenment/modules/conf/e-module-conf.edj
%dir %{_libdir}/enlightenment/modules/conf/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_applications
%{_libdir}/enlightenment/modules/conf_applications/e-module-conf_applications.edj
%dir %{_libdir}/enlightenment/modules/conf_applications/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_applications/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_applications/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_bindings
%{_libdir}/enlightenment/modules/conf_bindings/e-module-conf_bindings.edj
%dir %{_libdir}/enlightenment/modules/conf_bindings/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_bindings/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_bindings/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_dialogs
%{_libdir}/enlightenment/modules/conf_dialogs/e-module-conf_dialogs.edj
%dir %{_libdir}/enlightenment/modules/conf_dialogs/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_dialogs/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_dialogs/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_display
%{_libdir}/enlightenment/modules/conf_display/e-module-conf_display.edj
%dir %{_libdir}/enlightenment/modules/conf_display/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_display/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_display/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_interaction
%{_libdir}/enlightenment/modules/conf_interaction/e-module-conf_interaction.edj
%dir %{_libdir}/enlightenment/modules/conf_interaction/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_interaction/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_interaction/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_intl
%{_libdir}/enlightenment/modules/conf_intl/e-module-conf_intl.edj
%dir %{_libdir}/enlightenment/modules/conf_intl/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_intl/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_intl/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_menus
%{_libdir}/enlightenment/modules/conf_menus/e-module-conf_menus.edj
%dir %{_libdir}/enlightenment/modules/conf_menus/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_menus/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_menus/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_paths
%{_libdir}/enlightenment/modules/conf_paths/e-module-conf_paths.edj
%dir %{_libdir}/enlightenment/modules/conf_paths/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_paths/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_paths/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_performance
%{_libdir}/enlightenment/modules/conf_performance/e-module-conf_performance.edj
%dir %{_libdir}/enlightenment/modules/conf_performance/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_performance/%{arch_tag}/module.so
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
%dir %{_libdir}/enlightenment/modules/conf_shelves/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_shelves/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_shelves/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_theme
%{_libdir}/enlightenment/modules/conf_theme/e-module-conf_theme.edj
%dir %{_libdir}/enlightenment/modules/conf_theme/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_theme/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_theme/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_manipulation
%{_libdir}/enlightenment/modules/conf_window_manipulation/e-module-conf_window_manipulation.edj
%dir %{_libdir}/enlightenment/modules/conf_window_manipulation/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_window_manipulation/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_window_manipulation/module.desktop
#
%dir %{_libdir}/enlightenment/modules/conf_window_remembers
%{_libdir}/enlightenment/modules/conf_window_remembers/e-module-conf_window_remembers.edj
%dir %{_libdir}/enlightenment/modules/conf_window_remembers/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/conf_window_remembers/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/conf_window_remembers/module.desktop
#
%dir %{_libdir}/enlightenment/modules/connman
%{_libdir}/enlightenment/modules/connman/e-module-connman.edj
%dir %{_libdir}/enlightenment/modules/connman/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/connman/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/connman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/cpufreq
%{_libdir}/enlightenment/modules/cpufreq/e-module-cpufreq.edj
%dir %{_libdir}/enlightenment/modules/cpufreq/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/cpufreq/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/cpufreq/module.desktop
#
%dir %{_libdir}/enlightenment/modules/everything
%{_libdir}/enlightenment/modules/everything/e-module-everything-start.edj
%{_libdir}/enlightenment/modules/everything/e-module-everything.edj
%dir %{_libdir}/enlightenment/modules/everything/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/everything/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/everything/module.desktop
#
%dir %{_libdir}/enlightenment/modules/fileman
%{_libdir}/enlightenment/modules/fileman/e-module-fileman.edj
%dir %{_libdir}/enlightenment/modules/fileman/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/fileman/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/fileman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/fileman_opinfo
%{_libdir}/enlightenment/modules/fileman_opinfo/e-module-fileman_opinfo.edj
%dir %{_libdir}/enlightenment/modules/fileman_opinfo/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/fileman_opinfo/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/fileman_opinfo/module.desktop
#
%dir %{_libdir}/enlightenment/modules/gadman
%{_libdir}/enlightenment/modules/gadman/e-module-gadman.edj
%dir %{_libdir}/enlightenment/modules/gadman/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/gadman/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/gadman/module.desktop
#
%dir %{_libdir}/enlightenment/modules/geolocation
%{_libdir}/enlightenment/modules/geolocation/e-module-geolocation.edj
%dir %{_libdir}/enlightenment/modules/geolocation/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/geolocation/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/geolocation/module.desktop
#
%dir %{_libdir}/enlightenment/modules/ibar
%{_libdir}/enlightenment/modules/ibar/e-module-ibar.edj
%dir %{_libdir}/enlightenment/modules/ibar/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/ibar/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/ibar/module.desktop
#
%dir %{_libdir}/enlightenment/modules/ibox
%{_libdir}/enlightenment/modules/ibox/e-module-ibox.edj
%dir %{_libdir}/enlightenment/modules/ibox/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/ibox/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/ibox/module.desktop
#
%dir %{_libdir}/enlightenment/modules/lokker
%dir %{_libdir}/enlightenment/modules/lokker/%{arch_tag}
%{_libdir}/enlightenment/modules/lokker/%{arch_tag}/module.so
#
%dir %{_libdir}/enlightenment/modules/mixer
%{_libdir}/enlightenment/modules/mixer/e-module-mixer.edj
%{_libdir}/enlightenment/modules/mixer/sink-icons.txt
%dir %{_libdir}/enlightenment/modules/mixer/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/mixer/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/mixer/module.desktop
#
%dir %{_libdir}/enlightenment/modules/msgbus
%{_libdir}/enlightenment/modules/msgbus/e-module-msgbus.edj
%dir %{_libdir}/enlightenment/modules/msgbus/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/msgbus/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/msgbus/module.desktop
#
%dir %{_libdir}/enlightenment/modules/music-control
%{_libdir}/enlightenment/modules/music-control/e-module-music-control.edj
%dir %{_libdir}/enlightenment/modules/music-control/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/music-control/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/music-control/module.desktop
#
%dir %{_libdir}/enlightenment/modules/notification
%{_libdir}/enlightenment/modules/notification/e-module-notification.edj
%dir %{_libdir}/enlightenment/modules/notification/linux-*
%attr(755,root,root)  %{_libdir}/enlightenment/modules/notification/linux-*/module.so
%{_libdir}/enlightenment/modules/notification/module.desktop
#
%dir %{_libdir}/enlightenment/modules/packagekit
%{_libdir}/enlightenment/modules/packagekit/e-module-packagekit.edj
%dir %{_libdir}/enlightenment/modules/packagekit/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/packagekit/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/packagekit/module.desktop
#
%dir %{_libdir}/enlightenment/modules/pager
%{_libdir}/enlightenment/modules/pager/e-module-pager.edj
%dir %{_libdir}/enlightenment/modules/pager/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/pager/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/pager/module.desktop
#
%dir %{_libdir}/enlightenment/modules/polkit
%{_libdir}/enlightenment/modules/polkit/e-module-polkit.edj
%dir %{_libdir}/enlightenment/modules/polkit/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/polkit/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/polkit/module.desktop
#
%dir %{_libdir}/enlightenment/modules/procstats
%{_libdir}/enlightenment/modules/procstats/e-module-procstats.edj
%dir %{_libdir}/enlightenment/modules/procstats/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/procstats/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/procstats/module.desktop
#
%dir %{_libdir}/enlightenment/modules/quickaccess
%{_libdir}/enlightenment/modules/quickaccess/e-module-quickaccess.edj
%dir %{_libdir}/enlightenment/modules/quickaccess/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/quickaccess/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/quickaccess/module.desktop
#
%dir %{_libdir}/enlightenment/modules/shot
%{_libdir}/enlightenment/modules/shot/e-module-shot.edj
%dir %{_libdir}/enlightenment/modules/shot/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/shot/%{arch_tag}/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/shot/%{arch_tag}/upload
%{_libdir}/enlightenment/modules/shot/module.desktop
%{_libdir}/enlightenment/modules/shot/*.ttf
%{_libdir}/enlightenment/modules/shot/shotedit.edj
%{_libdir}/enlightenment/modules/shot/shots.desktop
#
%dir %{_libdir}/enlightenment/modules/start
%{_libdir}/enlightenment/modules/start/e-module-start.edj
%dir %{_libdir}/enlightenment/modules/start/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/start/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/start/module.desktop
#
%dir %{_libdir}/enlightenment/modules/syscon
%{_libdir}/enlightenment/modules/syscon/e-module-syscon.edj
%dir %{_libdir}/enlightenment/modules/syscon/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/syscon/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/syscon/module.desktop
#
%dir %{_libdir}/enlightenment/modules/systray
%{_libdir}/enlightenment/modules/systray/e-module-systray.edj
%dir %{_libdir}/enlightenment/modules/systray/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/systray/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/systray/module.desktop
#
%dir %{_libdir}/enlightenment/modules/tasks
%{_libdir}/enlightenment/modules/tasks/e-module-tasks.edj
%dir %{_libdir}/enlightenment/modules/tasks/linux-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/tasks/linux-*/module.so
%{_libdir}/enlightenment/modules/tasks/module.desktop
#
%dir %{_libdir}/enlightenment/modules/temperature
%{_libdir}/enlightenment/modules/temperature/e-module-temperature.edj
%dir %{_libdir}/enlightenment/modules/temperature/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/temperature/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/temperature/module.desktop
#
%dir %{_libdir}/enlightenment/modules/tiling
%{_libdir}/enlightenment/modules/tiling/e-module-tiling.edj
%dir %{_libdir}/enlightenment/modules/tiling/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/tiling/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/tiling/module.desktop
#
%dir %{_libdir}/enlightenment/modules/vkbd
%{_libdir}/enlightenment/modules/vkbd/dicts
%{_libdir}/enlightenment/modules/vkbd/e-module-vkbd.edj
%{_libdir}/enlightenment/modules/vkbd/keyboards
%dir %{_libdir}/enlightenment/modules/vkbd/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/vkbd/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/vkbd/module.desktop
%{_libdir}/enlightenment/modules/vkbd/theme.edj
#
%dir %{_libdir}/enlightenment/modules/winlist
%{_libdir}/enlightenment/modules/winlist/e-module-winlist.edj
%dir %{_libdir}/enlightenment/modules/winlist/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/winlist/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/winlist/module.desktop
#
%dir %{_libdir}/enlightenment/modules/wizard
%dir %{_libdir}/enlightenment/modules/wizard/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wizard/%{arch_tag}/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/wizard/%{arch_tag}/page_*.so
%{_libdir}/enlightenment/modules/wizard/def-ibar.txt
%{_libdir}/enlightenment/modules/wizard/desktop
#
%if %{with wayland}
%dir %{_libdir}/enlightenment/modules/wl_buffer
%dir %{_libdir}/enlightenment/modules/wl_buffer/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_buffer/%{arch_tag}/module.so
%dir %{_libdir}/enlightenment/modules/wl_desktop_shell
%dir %{_libdir}/enlightenment/modules/wl_desktop_shell/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/%{arch_tag}/module.so
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/module.desktop
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_desktop_shell/*.edj
%dir %{_libdir}/enlightenment/modules/wl_drm
%dir %{_libdir}/enlightenment/modules/wl_drm/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_drm/%{arch_tag}/module.so
%dir %{_libdir}/enlightenment/modules/wl_text_input
%dir %{_libdir}/enlightenment/modules/wl_text_input/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_text_input/%{arch_tag}/module.so
%dir %{_libdir}/enlightenment/modules/wl_weekeyboard
%{_libdir}/enlightenment/modules/wl_weekeyboard/*.edj
%dir %{_libdir}/enlightenment/modules/wl_weekeyboard/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_weekeyboard/%{arch_tag}/module.so
%dir %{_libdir}/enlightenment/modules/wl_wl
%dir %{_libdir}/enlightenment/modules/wl_wl/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_wl/%{arch_tag}/module.so
%dir %{_libdir}/enlightenment/modules/wl_x11
%dir %{_libdir}/enlightenment/modules/wl_x11/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/wl_x11/%{arch_tag}/module.so
%dir %{_libdir}/enlightenment/modules/xwayland
%dir %{_libdir}/enlightenment/modules/xwayland/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/xwayland/%{arch_tag}/module.so
%{_datadir}/wayland-sessions/enlightenment.desktop
%endif
#
%dir %{_libdir}/enlightenment/modules/xkbswitch
%{_libdir}/enlightenment/modules/xkbswitch/e-module-xkbswitch.edj
%dir %{_libdir}/enlightenment/modules/xkbswitch/%{arch_tag}
%attr(755,root,root) %{_libdir}/enlightenment/modules/xkbswitch/%{arch_tag}/module.so
%{_libdir}/enlightenment/modules/xkbswitch/module.desktop
#
%dir %{_libdir}/enlightenment/utils
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_alert
%attr(4755,root,root) %{_libdir}/enlightenment/utils/enlightenment_ckpasswd
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_elm_cfgtool
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_fm
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_fm_op
# SETUID root: allows rebooting, hibernating and shuting system down
%attr(4755,root,root) %{_libdir}/enlightenment/utils/enlightenment_sys
%attr(4755,root,root) %{_libdir}/enlightenment/utils/enlightenment_system
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_thumb
%attr(755,root,root) %{_libdir}/enlightenment/utils/enlightenment_wallpaper_gen

%{_datadir}/enlightenment
%{_datadir}/xsessions/enlightenment.desktop
%{_desktopdir}/emixer.desktop
%{_desktopdir}/enlightenment_askpass.desktop
%{_desktopdir}/enlightenment_filemanager.desktop
%{_desktopdir}/enlightenment_fprint.desktop
%{_desktopdir}/enlightenment_paledit.desktop
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_iconsdir}/hicolor/*x*/places/*.png
%{_iconsdir}/hicolor/scalable/apps/enlightenment*.svg
%{_iconsdir}/hicolor/scalable/places/enlightenment*.svg
%{_pixmapsdir}/enlightenment-askpass.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/enlightenment
%{_pkgconfigdir}/enlightenment.pc
%{_pkgconfigdir}/everything.pc
