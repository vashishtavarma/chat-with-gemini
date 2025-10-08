# Chat with Gemini

A simple web application that provides text-based Q&A and image analysis capabilities using Google's Gemini AI models. Built with Streamlit for an easy-to-use web interface.

## Features

- **Text-based Q&A**: Ask questions and get intelligent responses using Gemini-2.5-Flash
- **Image Analysis**: Upload images for description and analysis using Gemini-2.5-Pro
- **Web Interface**: Clean and intuitive Streamlit-based interface
- **Secure API Management**: Environment variable-based API key configuration

## Prerequisites

- Python 3.8 or higher
- Google AI API key (obtain from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:vashishtavarma/chat-with-gemini.git
   cd chat-with-gemini
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   - Create a `.env` file in the project root
   - Add your Google AI API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

### Text Q&A Application

1. **Start the text Q&A app**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Ask questions** in the text input field and click "Submit" to get AI responses

### Image Analysis Application

1. **Start the image analysis app**:
   ```bash
   streamlit run vision.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload an image** and/or provide text description for AI analysis

## Project Structure

```
chat-with-gemini/
├── app.py              # Text-based Q&A application
├── vision.py           # Image analysis application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
├── LICENSE            # MIT License
└── README.md          # Project documentation
```

## Dependencies

- **google-generativeai**: Google's Generative AI Python SDK
- **streamlit**: Web app framework for Python
- **python-dotenv**: Environment variable management
- **Pillow**: Image processing library (for vision.py)

## Models Used

- **app.py**: Uses `gemini-2.5-flash` for fast text responses
- **vision.py**: Uses `gemini-2.5-pro` for advanced image analysis

## API Configuration

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file as `GOOGLE_API_KEY`

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your `.env` file contains the correct `GOOGLE_API_KEY`
2. **Model Access**: Verify that Gemini models are available in your region
3. **Import Errors**: Install all dependencies with `pip install -r requirements.txt`
4. **Image Upload Issues**: Supported formats are PNG, JPG, and JPEG

### Warning Messages

You may see Google library warnings in the console. These are normal and don't affect functionality.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
