FROM node

WORKDIR /app/front
COPY package.json /app/front

RUN npm install

EXPOSE 3000
CMD ["npm", "run", "start"]
