FROM nginx

RUN mkdir /stocks_products/

RUN rm /etc/nginx/conf.d/default.conf

COPY ./project.conf /etc/nginx/conf.d/

WORKDIR /stocks_products/
