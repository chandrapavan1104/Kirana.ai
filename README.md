# Kirana.ai - Smart Inventory Management System

Kirana.ai is an intelligent inventory management system that combines natural language processing with a modern web interface to help store owners manage their inventory efficiently.

## Features

- 🎤 Voice Command Support
- 💬 Natural Language Processing
- 📱 Modern React Dashboard
- 🔄 Real-time Inventory Updates
- 🛒 Shopping Cart Integration

## Tech Stack

### Backend
- FastAPI (Python)
- Whisper (Speech-to-Text)
- Transformers (NLP)
- In-memory Storage (Temporary)

### Frontend
- Next.js
- TypeScript
- Tailwind CSS
- React Context API
- Axios

## Prerequisites

- Python 3.11+
- Node.js 18+
- npm or yarn
- Git

## Installation

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/chandrapavan1104/Kirana.ai.git
cd Kirana.ai
```

2. Create and activate a virtual environment:
```bash
cd kirana-backend
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the backend server:
```bash
uvicorn main:app --reload
```

The backend server will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd kirana-dashboard
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Start the development server:
```bash
npm run dev
# or
yarn dev
```

The frontend will be available at `http://localhost:3000`

## Usage

### Voice Commands

The system supports various voice commands for inventory management:

- "Add 5 kg of rice"
- "Update stock of sugar to 10 kg"
- "Delete milk from inventory"
- "List all items"
- "Show inventory status"

### Text Commands

You can also type commands in the chat interface:

- Add items: "Add [quantity] [unit] of [item]"
- Update items: "Update [item] to [quantity] [unit]"
- Delete items: "Delete [item]"
- List inventory: "Show inventory" or "List items"

### Cart Management

- Items can be added to cart through voice or text commands
- View cart by clicking the cart icon
- Modify quantities in the cart
- Remove items from cart

## API Endpoints

### Backend API

- `POST /text-command`: Process text commands
  - Request body: `{ "command": "string" }`
  - Response: `{ "success": boolean, "response": string, "item": object }`

- `POST /transcribe`: Process voice commands
  - Request: Form data with audio file
  - Response: `{ "transcription": string }`

## Project Structure

```
Kirana.ai/
├── kirana-backend/
│   ├── main.py              # FastAPI application
│   ├── agent.py             # Command execution agent
│   ├── inventory.py         # Inventory management
│   ├── inventory_toolkit.py # Inventory operations
│   ├── command_parser_agent.py # NLP command parsing
│   └── requirements.txt     # Python dependencies
│
└── kirana-dashboard/
    ├── src/
    │   ├── components/      # React components
    │   │   ├── Chatbot.tsx  # Chat interface
    │   │   ├── CartModal.tsx # Cart management
    │   │   └── CartIcon.tsx # Cart icon
    │   ├── context/         # React context
    │   │   └── cartContext.tsx # Cart state management
    │   ├── pages/           # Next.js pages
    │   └── styles/          # CSS styles
    ├── package.json         # Node.js dependencies
    └── tsconfig.json        # TypeScript configuration
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI Whisper for speech recognition
- Hugging Face Transformers for NLP
- FastAPI for the backend framework
- Next.js for the frontend framework

## Contact

Chandra Pavan - [@chandrapavan1104](https://github.com/chandrapavan1104)

Project Link: [https://github.com/chandrapavan1104/Kirana.ai](https://github.com/chandrapavan1104/Kirana.ai)
