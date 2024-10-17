%global theme	Numix-Circle

Name:		numix-icon-theme-circle
Version:	14.10
Release:	2
Summary:	%{theme} icon theme
Group:		Graphical desktop/Other

License:	GPL-3
URL:		https://www.numixproject.org

Source0:	%{name}-master.tar.gz

BuildArch:	noarch

%description
%{theme} is an icon theme from the Numix project - http://numixproject.org.


%prep
%setup -q -n %{name}-master


%build
# Nothing to build


%install
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/%{theme}
%{__install} -d -m755 %{buildroot}%{_datadir}/icons/%{theme}-Light
cp -axv %{theme}/* %{buildroot}%{_datadir}/icons/%{theme}
cp -axv %{theme}-Light/* %{buildroot}%{_datadir}/icons/%{theme}-Light


%files
%{_datadir}/icons/%{theme}
%{_datadir}/icons/%{theme}-Light
