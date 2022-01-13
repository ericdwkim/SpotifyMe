FROM nginx:1.21-alpine

# Set working directory
WORKDIR /f

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/nginx.conf /etc/nginx/conf.d