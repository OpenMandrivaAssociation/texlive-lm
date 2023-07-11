Name:		texlive-lm
Version:	65956
Release:	1
Summary:	Latin modern fonts in outline formats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/lm
License:	GFSL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Latin Modern family of fonts consists of 72 text fonts and
20 mathematics fonts, and is based on the Computer Modern fonts
released into public domain by AMS (copyright (c) 1997 AMS).
The lm font set contains a lot of additional characters, mainly
accented ones, but not exclusively. There is one set of fonts,
available both in Adobe Type 1 format (*.pfb) and in OpenType
format (*.otf). There are five sets of TeX Font Metric files,
corresponding to: Cork encoding (cork-*.tfm); QX encoding (qx-
*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); T5
(Vietnamese) encoding (t5-*.tfm); and Text Companion for EC
fonts aka TS1 (ts1-*.tfm).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/lm
%{_texmfdistdir}/fonts/enc/dvips/lm
%{_texmfdistdir}/fonts/map/dvipdfm/lm
%{_texmfdistdir}/fonts/map/dvips/lm
%{_texmfdistdir}/fonts/opentype/public/lm
%{_texmfdistdir}/fonts/tfm/public/lm
%{_texmfdistdir}/fonts/type1/public/lm
%{_texmfdistdir}/tex/latex/lm
%doc %{_texmfdistdir}/doc/fonts/lm

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
