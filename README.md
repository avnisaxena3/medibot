# MedAssist - AI Medical Assistant Chatbot

A Flask-based web application that provides medical assistance through an AI chatbot. Users describe their symptoms and receive structured medical information including probable causes, recommended OTC drugs, precautions, and when to visit a doctor.

## Features

- **Web UI** - Interactive chat interface with light/dark mode toggle
- **Structured Responses** - Medical advice formatted as JSON with condition, causes, drugs, precautions, and disclaimers
- **LangChain Integration** - Uses LangChain agents for intelligent query processing
- **Multiple LLM Providers** - Supports OpenAI and Anthropic models
- **Search Tool** - Integrates DuckDuckGo search for additional information
- **CORS Enabled** - Frontend and backend communication over HTTP

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Git

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/MedAssist.git
   cd MedAssist
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file with your API keys:**
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   # or
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   LLM_PROVIDER=openai  # or "anthropic"
   PORT=5500
   ```

## Usage

**Start the server:**
```bash
python api.py
```

The server will start on `http://127.0.0.1:5500/`

**Access the application:**
- Open your browser and navigate to `http://127.0.0.1:5500/`
- Type a symptom or medical question in the chat input
- Click "Send" to get medical advice

## Project Structure

```
MedAssist/
├── api.py              # Flask server with /chat endpoint
├── main.py             # CLI version with agent logic
├── tools.py            # DuckDuckGo search tool integration
├── index.html          # Frontend UI
├── script.js           # Frontend chat logic
├── style.css           # Frontend styling
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not in repo)
└── README.md           # This file
```

## API Endpoints

- **GET** `/` - Serves the frontend HTML
- **GET** `/<filename>` - Serves static files (CSS, JS, etc.)
- **POST** `/chat` - Medical query endpoint
  - Request: `{"query": "user symptom or question"}`
  - Response: `{"condition": "...", "probable_causes": [...], ...}`

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for GPT models | Required if using OpenAI |
| `ANTHROPIC_API_KEY` | Anthropic API key for Claude models | Required if using Anthropic |
| `LLM_PROVIDER` | Which LLM provider to use | `openai` |
| `OPENAI_MODEL` | OpenAI model name | `gpt-3.5-turbo` |
| `ANTHROPIC_MODEL` | Anthropic model name | `claude-3-5-sonnet` |
| `PORT` | Server port | `5500` |

## Technologies Used

- **Backend:** Flask, LangChain, OpenAI/Anthropic API
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
- **Tools:** DuckDuckGo Search, Pydantic for structured responses

## Disclaimer

⚠️ **This application is for informational purposes only.** It is not a substitute for professional medical advice. Always consult with a qualified healthcare provider for medical concerns.

## License

MIT License - See LICENSE file for details

## Author

Your Name / Your Organization

## Support

For issues, questions, or contributions, please open an issue on GitHub.
