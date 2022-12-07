FROM node:lts-alpine AS build
RUN apk add git

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY *.js ./
COPY src ./src
RUN npm run build



FROM python:3.6-alpine

# install dependencies
RUN apk update && apk upgrade
RUN apk add --no-cache gcc \
                       libc-dev \
                       libffi-dev
WORKDIR /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# copy source-codes
COPY learning_platform/ /app/learning_platform/
COPY --from=build /app/dist /app/dist/
COPY *.py /app/
COPY db.sqlite3 /app
COPY boot.sh /app
RUN chmod +x /app/boot.sh

# start server
EXPOSE 8000
CMD ["./boot.sh"]
