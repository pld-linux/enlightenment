Summary:	Enlightenment Window Manager
Summary(pl):	Zarz±dca okien X - Enlightenment
Name:		enlightenment
Version:	0.16.999.031
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	2e468e84199b97d67605207a55041c6d
Source1:	%{name}-xsession.desktop
Source2:	enlightenmentDR17-app.tar.gz
# Source2-md5:	9f08a7d1850bc81eb301d849561f609f
Source3:	enlightenmentDR17-wcnt.txt
Patch0:		enlightenmentDR17-module_temp_mac.patch
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	edje-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	fonts-TTF-bitstream-vera
Requires:	vfmg >= 0.9.95
Requires:	enlightenment-theme-default = %{version}
Requires:	enlightenment-init-default
Obsoletes:	enlightenmentDR17 >= 0.16.999
Obsoletes:	enlightenmentDR17-libs >= 0.16.999
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpotê¿niejszym i najpiêkniejszym zarz±dc± okien
jaki kiedykolwiek zosta³ stworzony dla Linuksa ;)

%package module-cpufreq-freqset
Summary:	CPU speed management binary
Summary(pl):	Program do zaz±dzania szybko¶ci± CPU
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Obsoletes:	enlightenmentDR17-module-cpufreq-freqset >= 0.16.999

%description module-cpufreq-freqset
freqset makes you able to change CPU frequency using cpufreq module.

It contains SUID binary.

%description module-cpufreq-freqset -l pl
freqset pozwala zmieniaæ czêstotliwo¶æ pracy procesora przy u¿yciu
modu³u cpufreq.

Zawiera binarkê SUID.

%package devel
Summary:	Development headers for Enlightenment
Summary(pl):	Pliki nag³ówkowe dla Enlightenmenta
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	edje-devel
Obsoletes:	enlightenmentDR17-devel >= 0.16.999

%description devel
Development headers for Enlightenment.

%description devel -l pl
Pliki nag³ówkowe dla Enlightenmenta.

%prep
%setup -q
%patch0 -p1
install %{SOURCE2} data/other/applications.tar.gz

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--disable-valgrind	\
	--with-profile=SLOW_PC
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/init/init.edj
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/data/themes/default.edj

install -d $RPM_BUILD_ROOT%{_libdir}/enlightenment/modules_extra
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/config-apps
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}/wcnt.txt
find $RPM_BUILD_ROOT%{_libdir}/enlightenment -name "*.a" -or -name "*.la" \
	| xargs rm

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
%doc AUTHORS COPYING* README
%attr(755,root,root) %{_bindir}/enlightenment
%attr(755,root,root) %{_bindir}/enlightenment_eapp
%attr(755,root,root) %{_bindir}/enlightenment_eapp_cache_gen
%attr(755,root,root) %{_bindir}/enlightenment_imc
%attr(755,root,root) %{_bindir}/enlightenment_remote
%attr(755,root,root) %{_bindir}/enlightenment_start
%attr(755,root,root) %{_bindir}/enlightenment_thumb
%dir %{_libdir}/enlightenment
%dir %{_libdir}/enlightenment/*
%dir %{_libdir}/enlightenment/modules/*
%dir %{_libdir}/enlightenment/modules/*/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/*/linux-gnu-*/*.so
# violates FHS
%{_libdir}/enlightenment/modules/*/module.eap
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
