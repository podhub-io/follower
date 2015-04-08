FROM podhub/gevent
MAINTAINER Jon Chen <bsd@voltaire.sh>

EXPOSE 5000

RUN /usr/bin/pacman -Syu --noconfirm libmemcached base-devel

RUN /usr/bin/pip2 install podhub.follower

RUN mkdir -p /var/log/podhub/follower/

RUN mkdir -p /service/follower
RUN echo '#!/bin/sh\nexec /usr/bin/follower 2>&1' > /service/follower/run
RUN chmod +x /service/follower/run
