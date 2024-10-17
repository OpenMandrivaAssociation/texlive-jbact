Name:		texlive-jbact
Version:	52717
Release:	2
Summary:	BibTeX style for biology journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jbact
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jbact.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The style is a development of apalike.bst in the BibTeX bundle.
The style serves two journals -- if the user executes
"\nocite{TitlesOn}", the style serves for the Journal of
Theoretical Biology; otherwise it serves for the Journal of
Molecular Biology.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/jbact

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
