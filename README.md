# Smart Notes Backend

This repository contains the backend API for the Smart Notes application, a project inspired by the AI-powered note-taking features introduced by Samsung and Apple. The frontend can be found at [SmartNotes_front-end](https://github.com/vikrant500/SmartNotes_front-end).

## About the Project

Smart Notes was born out of necessity when Samsung and Apple released AI-powered updates to their native note-taking applications, which weren't supported on the Samsung Tab S6 Lite. Instead of missing out on these innovative features, I decided to build a complete solution from scratch. This project demonstrates that cutting-edge AI note-taking capabilities can be implemented on any device through a web application.

## Local Setup

### Prerequisites
- Python 3.8 or higher
- Git
- A Google Gemini API key

### Installation Steps

1. Clone both repositories in the same parent directory:
   ```bash
   git clone [https://github.com/vikrant500/SmartNotes_api.git]
   git clone [https://github.com/vikrant500/SmartNotes_front-end.git]
   ```

2. Navigate to the API directory:
   ```bash
   cd api
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the api directory:
   ```bash
   touch .env
   ```

6. Add your Gemini API key to the `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Running the Application

1. Start the frontend (in its directory):
   ```bash
   npm run dev
   ```

2. Start the backend server:
   ```bash
   python3 main.py
   ```

The backend server will start running on `http://localhost:8000`.

## Features
- AI-powered note analysis and enhancement
- Integration with Google's Gemini AI
- RESTful API endpoints for note management
- Real-time processing of notes

## Security Note
Never commit your `.env` file or expose your API keys in public repositories.
