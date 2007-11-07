Summary:	Monsterz - arcade puzzle game
Summary(pl.UTF-8):	Monsterz - układanka zręcznościowa
Name:		monsterz
Version:	0.7.0
Release:	1
License:	WTFPL v2
Group:		Applications/Games
Source0:	http://sam.zoy.org/monsterz/%{name}-%{version}.tar.gz
# Source0-md5:	323d04d4a2a2905df91eab4ff17e537d
URL:		http://sam.zoy.org/monsterz/
Requires:	python
Requires:	python-pygame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monsterz is a little arcade puzzle game, similar to the famous
Bejeweled or Zookeeper.

The goal of the game is to create rows of similar monsters, either
horizontally or vertically. The only allowed move is the swap of two
adjacent monsters, on the condition that it creates a row of three or
more. When alignments are cleared, pieces fall from the top of the
screen to fill the board again. Chain reactions earn you even more
points.

%description -l pl.UTF-8
Monsterz to niewielka układanka zręcznościowa, podobna do słynnych
gier Bejeweled czy Zookeeper.

Celem gry jest utworzenie rzędów podobnych potworów, poziomo lub
pionowo. Jedynym dozwolonym ruchem jest zamiana dwóch sąsiednich
potworów, pod warunkiem, ze tworzy to rząd trzech lub więcej
takich samych. Po wyczyszczeniu z góry ekranu spadają kolejne
elementy, aby wypełnić z powrotem planszę. Reakcje łańcuchowe
pozwalają zdobyć nawet więcej punktów.

%prep
%setup -q

%build
%{__cc} %{rpmldflags} %{rpmcflags} -Wall -o monsterz monsterz.c \
	-DDATADIR="\"%{_datadir}/monsterz\"" \
	-DSCOREFILE="\"/var/games/monsterz\""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/monsterz/{graphics,sound},/var/games}

install monsterz $RPM_BUILD_ROOT%{_bindir}
install monsterz.py $RPM_BUILD_ROOT%{_datadir}/monsterz
install graphics/*.png $RPM_BUILD_ROOT%{_datadir}/monsterz/graphics
install sound/*.wav sound/music.s3m $RPM_BUILD_ROOT%{_datadir}/monsterz/sound
:> $RPM_BUILD_ROOT/var/games/monsterz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%attr(2755,root,games) %{_bindir}/monsterz
%dir %{_datadir}/monsterz
%attr(755,root,root) %{_datadir}/monsterz/monsterz.py
%{_datadir}/monsterz/graphics
%{_datadir}/monsterz/sound
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/monsterz
