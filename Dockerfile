FROM php:8.2-apache

# Install mysqli extension required by the application
RUN docker-php-ext-install mysqli

WORKDIR /var/www/html

# Copy application files into the container
COPY . /var/www/html/

# Give Apache ownership of app files and expose HTTP port
RUN chown -R www-data:www-data /var/www/html
EXPOSE 80

CMD ["apache2-foreground"]
