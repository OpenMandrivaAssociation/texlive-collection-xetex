Name:		texlive-collection-xetex
Epoch:		1
Version:	71515
Release:	1
Summary:	XeTeX and packages
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-xetex.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-arabxetex
Requires:	texlive-euenc
Requires:	texlive-fixlatvian
Requires:	texlive-fontbook
Requires:	texlive-fontwrap
Requires:	texlive-mathspec
Requires:	texlive-philokalia
Requires:	texlive-polyglossia
Requires:	texlive-ptext
Requires:	texlive-realscripts
Requires:	texlive-ucharclasses
Requires:	texlive-unisugar
Requires:	texlive-xecjk
Requires:	texlive-xecolor
Requires:	texlive-xecyr
Requires:	texlive-xeindex
Requires:	texlive-xepersian
Requires:	texlive-xesearch
Requires:	texlive-xetex
Requires:	texlive-xetex-def
Requires:	texlive-xetex-itrans
Requires:	texlive-xetex-pstricks
Requires:	texlive-xetex-tibetan
Requires:	texlive-xetexconfig
Requires:	texlive-xetexfontinfo
Requires:	texlive-xetexko
Requires:	texlive-xevlna
Requires:	texlive-xltxtra
Requires:	texlive-xunicode

%description
Packages for XeTeX, the Unicode/OpenType-enabled TeX by
Jonathan Kew, http://tug.org/xetex.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
