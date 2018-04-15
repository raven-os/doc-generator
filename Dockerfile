FROM debian

RUN apt-get update && apt-get install -y \
	python3 \
	python3-pip \
	graphviz \
	libgraphviz-dev \
	pandoc \
	pkg-config \
	texlive-full

ADD . /app
WORKDIR /app

RUN pip3 install -r requirements.txt
