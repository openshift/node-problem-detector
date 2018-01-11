FROM rhel7:7-released

LABEL com.redhat.component="atomic-openshift-node-problem-detector-docker"
LABEL name="openshift/node-problem-detector"
LABEL version="3.7"

RUN yum -y update && \
    yum -y install atomic-openshift-node-problem-detector && \
    yum clean all

CMD /usr/bin/node-problem-detector
