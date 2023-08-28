FROM node:14

WORKDIR /usr/src/app

RUN npm install express mongodb

COPY app.js .
COPY login.html .

EXPOSE 3000

CMD ["node", "app.js"]
