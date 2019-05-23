### Stage 1: build ###

FROM node:11.4.0-alpine as builder

# Set working directory.
RUN mkdir /app
WORKDIR /app

# Copy app dependencies.
# photo-album-front/package-lock.json should be after package.json but package-lock.json is not generated:(
# problem may be in my npm version. but it creating on npm install in docker image
COPY photo-album-front/package.json /app/photo-album-front/

# Install app dependencies.
RUN npm install --prefix photo-album-front

# Copy app files.
COPY . /app

# Build app
RUN npm run build --prefix photo-album-front -- --output-path=./dist/out


### Stage 2: delivery ###

FROM nginx:1.15.7-alpine

# Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy output directory from builder to nginx image.
COPY --from=builder /app/photo-album-front/dist/out /usr/share/nginx/html

# Copy nginx configuration file.
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf