# Use an official Node.js image with Chromium dependencies for Puppeteer
FROM node:16-slim

# Install necessary dependencies for Puppeteer and Chromium
RUN apt-get update && apt-get install -y \
    chromium \
    --no-install-recommends

# Set the working directory in the container
WORKDIR /app

# Install Puppeteer (it will install Chromium automatically)
RUN npm install puppeteer

# Copy your script into the container
COPY screenshot.js /app/screenshot.js

# Run the Puppeteer script to take a screenshot
CMD ["node", "screenshot.js"]
