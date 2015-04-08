FROM podhub/gevent
MAINTAINER Jon Chen <bsd@voltaire.sh>

EXPOSE 5000

RUN /usr/bin/pacman -Syu --noconfirm libmemcached

RUN /usr/bin/pip install podhub.follower

RUN mkdir -p /var/log/podhub/follower/

RUN echo '#!/bin/sh\nexec /usr/bin/follower 2>&1' > /service/follower/run
RUN chmod +x /service/follower/run
