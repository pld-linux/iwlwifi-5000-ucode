%bcond_with	exp # experimental, turned on only when such exists
Summary:	Microcode image for Intel Wireless WiFi Link 5000AGN Adapter
Summary(pl.UTF-8):	Obraz mikrokodu dla układów bezprzewodowych Intel Wireless WiFi Link 5000AGN
%define	_module	5000
Name:		iwlwifi-%{_module}-ucode
Version:	8.83.5.1
Release:	2
License:	distributable
Group:		Base/Kernel
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
# Source0-md5:	da82465019b3c7d1ee5156474ab4931d
Source1:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-5.4.A.11.tar.gz
# Source1-md5:	748860c5079dde1a1313e72511b9322a
%if %{with exp}
# http://www.intellinuxwireless.org/?n=experimental
Source2:	http://www.intellinuxwireless.org/iwlwifi/downloads/iwlwifi-5000-exp-%{version}.tgz
# Source2-md5:	xx
%endif
URL:		http://www.intellinuxwireless.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The file provided in this package must be present on your system in
order for the Intel Wireless WiFi Link 5000AGN driver for Linux
(iwlwifi-%{_module}) to operate on your system.

On adapter initialization, and at varying times during the uptime of
the adapter, the microcode is loaded into the RAM on the network
adapter. The microcode provides the low level MAC features including
radio control and high precision timing events (backoff, transmit,
etc.) while also providing varying levels of packet filtering which
can be used to keep the host from having to handle packets that are
not of interest given the current operating mode of the device.

%description -l pl.UTF-8
Plik dostarczany przez ten pakiet jest wymagany w systemie do
działania linuksowego sterownika dla układów bezprzewodowych Intel
Wireless WiFi Link 5000AGN (iwlwifi-%{_module}).

Przy inicjalizacji układu i w różnych chwilach w trakcie jego
działania mikrokod jest wczytywany do pamięci RAM układu. Mikrokod
udostępnia funkcje niskopoziomowe MAC, w tym sterowanie częścią
radiową i zdarzeniami wymagającymi dużej dokładności czasowej
(oczekiwania, transmisja itp.), a także różne poziomy filtrowania
pakietów, zapobiegające docieraniu do komputera pakietów
niepotrzebnych w danym trybie pracy urządzenia.

%prep
%setup -q -c -a1 %{?with_exp:-a2}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install */iwlwifi-%{_module}-*.ucode $RPM_BUILD_ROOT/lib/firmware
install iwlwifi-5000-ucode-8.83*/LICENSE.%{name} $RPM_BUILD_ROOT/lib/firmware/%{name}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc iwlwifi-5000-ucode-8.83*/README*
/lib/firmware/%{name}-LICENSE
/lib/firmware/*.ucode
