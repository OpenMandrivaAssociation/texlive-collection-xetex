# revision 24140
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-xetex
Version:	20120223
Release:	1
Summary:	XeTeX packages
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-xetex.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-arabxetex
Requires:	texlive-euenc
Requires:	texlive-fixlatvian
Requires:	texlive-fontbook
Requires:	texlive-fontwrap
Requires:	texlive-mathspec
Requires:	texlive-philokalia
Requires:	texlive-polyglossia
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
Requires:	texlive-xetexconfig
Requires:	texlive-xetexfontinfo
Requires:	texlive-xltxtra
Requires:	texlive-xunicode
Requires:	texlive-collection-basic

%description
Packages for XeTeX, the Unicode/OpenType-enabled TeX by
Jonathan Kew, http://scripts.sil.org/xetex.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
