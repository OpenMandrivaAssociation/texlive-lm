%global tl_name lm
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.005
Release:	%{tl_revision}.1
Summary:	Latin modern fonts in outline formats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/lm
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Latin Modern family of fonts consists of 72 text fonts and 20
mathematics fonts, and is based on the Computer Modern fonts released
into public domain by AMS (copyright (c) 1997 AMS). The lm font set
contains a lot of additional characters, mainly accented ones, but not
exclusively. There is one set of fonts, available both in Adobe Type 1
format (*.pfb) and in OpenType format (*.otf). There are five sets of
TeX Font Metric files, corresponding to: Cork encoding (cork-*.tfm); QX
encoding (qx-*.tfm); TeX'n'ANSI aka LY1 encoding (texnansi-*.tfm); T5
(Vietnamese) encoding (t5-*.tfm); and Text Companion for EC fonts aka
TS1 (ts1-*.tfm).

