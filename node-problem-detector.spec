#debuginfo not supported with Go
%global debug_package %{nil}
# modifying the Go binaries breaks the DWARF debugging
%global __os_install_post %{_rpmconfigdir}/brp-compress

%global gopath      %{_datadir}/gocode
%global import_path github.com/openshift/node-problem-detector

%global golang_version 1.8.3

%if "%{dist}" == ".el7aos"
%global package_name atomic-openshift
%global product_name Atomic OpenShift
%else
%global package_name origin
%global product_name Origin
%endif

Name:           atomic-openshift-node-problem-detector
Version:        3.7.0
Release:        0%{?dist}
Summary:        Node monitoring for OpenShift
License:        ASL 2.0
URL:            https://%{import_path}

# tar file created like this:
#   mkdir -p aos-node-problem-detector-3.7.0/go/src/k8s.io/node-problem-detector && \
#   curl -L https://github.com/kubernetes/node-problem-detector/archive/c0bd1df.tar.gz \
#     | tar zxf - -C aos-node-problem-detector-3.7.0/go/src/k8s.io/node-problem-detector --strip-components 1 && \
#   tar zcf aos-node-problem-detector-3.7.0.tar.gz --owner=root:0 --group=root:0 aos-node-problem-detector-3.7.0

Source0:        aos-node-problem-detector-3.7.0.tar.gz
BuildRequires:  systemd-devel
BuildRequires:  golang >= %{golang_version}

%description
OpenShift is a distribution of Kubernetes optimized for enterprise application
development and deployment. Node Problem Detector is a program that runs on
each node in an OpenShift cluster and watches for problems that could affect
applications running on the node. Any detected problems are reported via
the cluster API.

%prep
%setup -n aos-node-problem-detector-%{version}

%build
export GOPATH=`pwd`/go
cd go/src/k8s.io/node-problem-detector
make bin/node-problem-detector VERSION=%{version}-%{release}

%install
install -d %{buildroot}%{_bindir}
install -p -m 755 go/src/k8s.io/node-problem-detector/bin/node-problem-detector %{buildroot}%{_bindir}/node-problem-detector

%files
%doc go/src/k8s.io/node-problem-detector/README.md
%doc go/src/k8s.io/node-problem-detector/config/*.json
%license go/src/k8s.io/node-problem-detector/LICENSE
%{_bindir}/node-problem-detector

%changelog
* Tue Sep 12 2017 Joel Smith <joelsmith@redhat.com> 3.7.0-0.0.0
- Initial package version
