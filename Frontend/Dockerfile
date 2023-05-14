# Use the official Nginx image as the base
FROM nginx
# Copy your HTML file to the container
COPY Frontend.html /usr/share/nginx/html
# Copy your Nginx configuration file to the container
RUN echo 'server { \
    listen 9000; \
    server_name localhost; \
    location / { \
    root /usr/share/nginx/html; \
    index Frontend.html; \
    } \
    }' > /etc/nginx/conf.d/default.conf
# Expose port 9000
EXPOSE 9000
# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
