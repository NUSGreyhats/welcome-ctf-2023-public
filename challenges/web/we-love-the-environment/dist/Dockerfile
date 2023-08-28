FROM php:8.2-alpine

COPY flag /flag
COPY readflag.c /tmp/readflag.c

RUN apk add --no-cache gcc musl-dev && \
    gcc -o /readflag /tmp/readflag.c && \
    rm /tmp/readflag.c && \
    chmod 4755 /readflag && \
    chmod 400 /flag

COPY src /var/www/html
RUN chown -R root:root /var/www/html && \
    chmod -R 555 /var/www/html

USER www-data
CMD ["php", "-S", "0.0.0.0:8000", "-t", "/var/www/html"]