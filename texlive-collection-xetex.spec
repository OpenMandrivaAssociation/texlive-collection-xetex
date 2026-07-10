%global tl_name collection-xetex
%global tl_revision 78834

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	XeTeX and packages
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-xetex
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-xetex.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(arabxetex)
Requires:	texlive(bidi-atbegshi)
Requires:	texlive(bidicontour)
Requires:	texlive(bidipagegrid)
Requires:	texlive(bidipresentation)
Requires:	texlive(bidishadowtext)
Requires:	texlive(businesscard-qrcode)
Requires:	texlive(collection-basic)
Requires:	texlive(cqubeamer)
Requires:	texlive(ctex)
Requires:	texlive(ctex-faq)
Requires:	texlive(fixlatvian)
Requires:	texlive(font-change-xetex)
Requires:	texlive(fontbook)
Requires:	texlive(fontwrap)
Requires:	texlive(interchar)
Requires:	texlive(na-position)
Requires:	texlive(philokalia)
Requires:	texlive(ptext)
Requires:	texlive(shtthesis)
Requires:	texlive(simple-resume-cv)
Requires:	texlive(simple-thesis-dissertation)
Requires:	texlive(tetragonos)
Requires:	texlive(ucharclasses)
Requires:	texlive(unicode-bidi)
Requires:	texlive(unimath-plain-xetex)
Requires:	texlive(unisugar)
Requires:	texlive(xebaposter)
Requires:	texlive(xechangebar)
Requires:	texlive(xecjk)
Requires:	texlive(xecolor)
Requires:	texlive(xecyr)
Requires:	texlive(xeindex)
Requires:	texlive(xelatex-dev)
Requires:	texlive(xesearch)
Requires:	texlive(xespotcolor)
Requires:	texlive(xetex)
Requires:	texlive(xetex-devanagari)
Requires:	texlive(xetex-itrans)
Requires:	texlive(xetex-pstricks)
Requires:	texlive(xetex-tibetan)
Requires:	texlive(xetexconfig)
Requires:	texlive(xetexfontinfo)
Requires:	texlive(xetexko)
Requires:	texlive(xetexref)
Requires:	texlive(xevlna)
Requires:	texlive(zbmath-review-template)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Packages for XeTeX, the Unicode/OpenType-enabled TeX by Jonathan Kew.
See https://tug.org/xetex.

