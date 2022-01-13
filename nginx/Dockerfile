FROM nginx:1.21-alpine

# Set working directory
WORKDIR /flask

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d