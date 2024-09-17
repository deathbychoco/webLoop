const puppeteer = require('puppeteer');
const fs = require('fs').promises;

(async () => {
    try {
        console.log("Starting Puppeteer script...");

        // Read the HTML file from the mounted data folder
        const htmlContent = await fs.readFile('/app/data/generated_website.html', 'utf8');
        console.log("HTML content loaded successfully.");

        // Read the CSS file and inject it into the HTML
        const cssContent = await fs.readFile('/app/data/style.css', 'utf8');
        console.log("CSS content loaded successfully.");

        // Inject the CSS into the HTML by adding a <style> tag in the <head>
        const htmlWithCSS = htmlContent.replace(
            '</head>',
            `<style>${cssContent}</style></head>`
        );
        
        // Launch a headless browser
        const browser = await puppeteer.launch({
            args: ['--no-sandbox', '--disable-setuid-sandbox'],
            headless: true  // Headless mode (no GUI)
        });
        console.log("Browser launched.");

        // Create a new page
        const page = await browser.newPage();
        console.log("New page created.");

        // Set the viewport (resolution)
        await page.setViewport({ width: 1920, height: 1080 });
        console.log("Viewport set to 1920x1080.");

        // Set the page content to the HTML with the injected CSS
        console.log("Setting page content...");
        await page.setContent(htmlWithCSS);

        // Wait for the body element to load
        await page.waitForSelector('body', { timeout: 5000 });
        console.log("Body element found.");

        // Take a screenshot with the specified resolution
        await page.screenshot({
            path: '/app/data/website_screenshot.png',  // Save the screenshot in the mounted folder
            fullPage: true  // Capture the full page
        });
        console.log("Screenshot taken successfully at 1920x1080 resolution!");

        // Close the browser
        await browser.close();
        console.log("Browser closed.");
    } catch (err) {
        console.error("Error occurred:", err);
    }
})();
