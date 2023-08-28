FROM pwn.red/jail
COPY --from=ubuntu / /srv

ADD ./app/flag.txt /srv/app/flag.txt
ADD ./app/chall /srv/app/run

RUN chmod 444 /srv/app/flag.txt
RUN chmod +x /srv/app/run

ENV JAIL_TIME 60
