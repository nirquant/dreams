# Dreams - Cognitive Wellness Ecosystem

This repository contains the Dreamz website. The homepage introduces the company as a complete cognitive wellness ecosystem, while the product page showcases the Dreamz smart sleep mask with a waitlist system that collects and stores email addresses.

## Features

- Responsive landing page showcasing the Dreams sleep mask product
- Waitlist system for collecting user emails
- Server-side storage of emails in a JSON file
- Admin view of collected emails

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the Flask server:
   ```
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## How It Works

- The application uses Flask to serve both the static files and handle API requests
- When a user submits their email through the waitlist form, it's sent to the Flask backend
- Emails are stored in a `waitlist_data.json` file
- The waitlist preview shows all collected emails (in a real production environment, this would be password protected)

## File Structure

- `index.html` - Company homepage
- `product.html` - Smart sleep mask product page
- `styles.css` - CSS styles for the landing page
- `script.js` - JavaScript for animations and UI effects
- `app.py` - Flask server that handles API requests and serves static files
- `waitlist_data.json` - JSON file that stores the email addresses (created automatically)

## API Endpoints

- `GET /api/waitlist` - Returns the current waitlist data
- `POST /api/waitlist` - Adds a new email to the waitlist

## Production Considerations

For a production environment, consider the following improvements:

- Add password protection for viewing the waitlist data
- Implement a proper database instead of a JSON file
- Set up HTTPS for secure data transmission
- Add email verification
- Implement rate limiting to prevent abuse
- Deploy to a proper web server instead of Flask's development server

---

© 2023 Cosmic Sleep Technologies 