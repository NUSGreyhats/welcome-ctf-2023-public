FROM pwn.red/jail
COPY --from=ubuntu / /srv

RUN mkdir /srv/app
ADD ./app/fma /srv/app/run
ADD ./app/libc.so.6 /srv/app/libc.so.6
ADD ./app/ld-linux.so.2 /srv/app/ld-linux.so.2

ENV JAIL_TIME 60
