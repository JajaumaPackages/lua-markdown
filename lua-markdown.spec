%global luaver 5.1
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:		lua-markdown
Version:	0.32
Release:	2%{?dist}
BuildArch:	noarch
Summary:	Markdown module for Lua
License:	MIT
URL:		http://www.frykholm.se/files/markdown.lua
Source0:	http://www.frykholm.se/files/markdown.lua
Source1:	http://www.frykholm.se/files/markdown-tests.lua
BuildRequires:	lua >= %{luaver}
Requires:	lua >= %{luaver}

%description
This is an implementation of the popular text markup language Markdown
in pure Lua.  Markdown can convert documents written in a simple and
easy to read text format to well-formatted HTML.


%prep
%setup -c -T
cp -av %{SOURCE0} .
cp -av %{SOURCE1} .


%build
# nothing to do here


%install
mkdir -p %{buildroot}%{luapkgdir}
mkdir -p %{buildroot}%{_bindir}
cp -av markdown.lua %{buildroot}%{luapkgdir}

# fix script
sed -i %{buildroot}%{luapkgdir}/markdown.lua -e '1{/^#!/d}'

# create a wrapper
echo -en '#!/bin/sh\nlua %{luapkgdir}/markdown.lua "$@"' \
  > %{buildroot}%{_bindir}/markdown.lua
chmod +x %{buildroot}%{_bindir}/markdown.lua


%check
lua markdown.lua -t


%files
%{_bindir}/markdown.lua
%{luapkgdir}/markdown.lua


%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  2 2013 Thomas Moschny <thomas.moschny@gmx.de> - 0.32-1
- New package.
