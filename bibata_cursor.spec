Name:           bibata-cursor-theme
Version:        0.0.1
Release:        1%{?dist}
Summary:        Bibata Cursor Theme for X11 and Hyprland

License:        GPLv3 
URL:            https://github.com/rtgiskard/bibata_cursor
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  librsvg2-tools
BuildRequires:  xcursorgen
BuildRequires:  git
BuildRequires:  python

Requires:       librsvg2-tools
Requires:       xcursorgen
Requires:       python3

%description
Bibata Cursor Theme is a modern, sleek cursor theme. This package builds the cursor theme for X11 and Hyprland environments.

%prep
%setup -q 

%build
python3 cursor_utils.py --hypr --x11 --out-dir ./out

%install
mkdir -p %{buildroot}/usr/share/icons
cp -r ./out/Bibata-* %{buildroot}/usr/share/icons/

%files
%doc readme.adoc
/usr/share/icons/Bibata-*

%changelog
* Wed Dec 11 2024 Carlos Junior <cjuniorfox@gmail.com> - 0.0.1-1
- RPM Build for the project

