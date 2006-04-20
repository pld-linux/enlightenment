Summary:	Enlightenment Window Manager
Summary(pl):	Zarz�dca okien X - Enlightenment
Summary(de):	Enlightenment ist ein Window Manager f�r X
Name:		enlightenment
Version:	0.16.7.2
Release:	2
License:	BSD
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	78747d34f882676eafe26eef22a448be
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
Source4:	%{name}-e_gen_menu
Source5:	%{name}-e_check_menu
Patch0:		%{name}-edirconf.patch
Patch1:		%{name}-ac_am_fixes.patch
Patch2:		%{name}-pl.patch
Patch3:		%{name}-no_eng_config.patch
Patch4:		%{name}-check_menus.patch
Patch5:		%{name}-winter-i18n.patch
URL:		http://enlightenment.org/
BuildRequires:	XFree86
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.13
BuildRequires:	fnlib-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	iconv
BuildRequires:	imlib2-devel
BuildRequires:	libghttp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
Requires:	ImageMagick-coder-png
Requires:	vfmg >= 0.9.95
Requires:	xinitrc-ng
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties
%define		_sysconfdir	/etc/X11/enlightenment

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpot�niejszym i najpi�kniejszym zarz�dc� okien
jaki kiedykolwiek zosta� stworzony dla Linuksa ;)

%description -l de
Enlightenment ist ein Window Manager f�r X. Sein Designziel ist es, so
konfigurierbar wie nur m�glich in den Bereichen Aussehen und Bedienung
zu sein. Das derzeitige Design von Enlightenment steuert darauf hin,
ein "vern�nftiger" Desktop zu werden, das bedeutet, es verwaltet
Anwendungsfenster, zudem wird in der Lage sein, Anwendungen zu starten
und Dateien zu verwalten.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# tar-gziped text files !?!
( cd config
for LANG_FILE in ja ko pl; do
	mkdir $LANG_FILE
	cd $LANG_FILE
	tar -zxvf ../config.$LANG_FILE
	cd ..
done )
%patch3 -p1
%patch4 -p1
mkdir themes/winter
cd themes/winter
tar -zxf ../winter.etheme
cd -
%patch5 -p1

for FILE in actionclasses.cfg keybindings.cfg keybindings.gmc.cfg \
		keybindings.nogmc.cfg menus.cfg; do
	iconv -f EUC-JP -t UTF-8 config/ja/$FILE.ja > \
		config/ja/$FILE.ja_JP.UTF-8
	iconv -f EUC-KR -t UTF-8 config/ko/$FILE.ko > \
		config/ko/$FILE.ko_KR.UTF-8
	iconv -f ISO-8859-2 -t UTF-8 config/pl/$FILE.pl > \
		config/pl/$FILE.pl_PL.UTF-8
done	# it helps, but UTF-8 still isn't working correctly

mv -f po/{no,nb}.po
rm po/*.gmo

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
export LOCALEDIR=%{_datadir}/locale
%configure \
	--enable-sound=yes

# regenerate gmo files
%{__make} -C po update-gmo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir},/etc/sysconfig/wmstyle}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/enlightenment/scripts/e_gen_menu
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/enlightenment/scripts/e_check_menu

rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/enlightenment/X11

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%config %{_sysconfdir}
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/enlightenment
%{_datadir}/enlightenment/[!s]*
%attr(755,root,root) %{_datadir}/enlightenment/scripts
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/*
%{_mandir}/man1/*