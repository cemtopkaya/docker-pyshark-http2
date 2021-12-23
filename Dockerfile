FROM centos



RUN  yum -y update && \
     yum -y install epel-release &&\
     yum -y install wireshark 

RUN  yum -y install python36 
RUN  curl -O https://bootstrap.pypa.io/get-pip.py
RUN /usr/bin/python3.6 get-pip.py 
RUN rm get-pip.py
RUN pip install pyshark
RUN pip install tqdm requests

CMD ["python3"]