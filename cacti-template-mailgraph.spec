%define		template	mailgraph
Summary:	Mailgraph statistics template for Cacti
Name:		cacti-template-%{template}
Version:	0.1
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	cacti_data_template_postfix_processing_mailgraph.xml
Source1:	cacti_data_template_postfix_processing_virus_mailgraph.xml
Source2:	cacti_graph_template_postfix_processing_mailgraph.xml
URL:		http://forums.cacti.net/about1571.html
BuildRequires:	rpmbuild(macros) >= 1.554
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
Template for Cacti - Mail statistics via mailgraph rrd files.

%prep
%setup -qcT
cp -a %{SOURCE0} .
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
cp -a *.xml $RPM_BUILD_ROOT%{resourcedir}

%post
%cacti_import_template %{resourcedir}/cacti_data_template_postfix_processing_mailgraph.xml
%cacti_import_template %{resourcedir}/cacti_data_template_postfix_processing_virus_mailgraph.xml
%cacti_import_template %{resourcedir}/cacti_graph_template_postfix_processing_mailgraph.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{resourcedir}/*.xml
