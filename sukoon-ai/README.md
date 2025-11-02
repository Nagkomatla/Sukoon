# Sukoon AI Backend

**A comprehensive mental health care platform combining AI agents, automation, and empathetic support for patients with schizophrenia and other mental health conditions.**

FastAPI server for the Sukoon Agentic AI (Schizophrenia Care Assistant) - a holistic solution that bridges the gap between psychiatric care and emotional support, offering continuous, affordable, and humanized mental health care powered by AI.

## 🌟 Overview

Sukoon is a revolutionary mental health care platform designed to provide continuous support, medication adherence monitoring, and emotional well-being tracking. Built with accessibility in mind, especially for low-resource settings, Sukoon combines multiple technologies to create a seamless, empathetic care experience.

## ✨ Key Features

### 🤖 AI Agent (Inya.ai + Gnani.ai)
- **Daily Patient Calls**: Automated daily calls to check on patients
- **Medication Verification**: Asks patients if they've taken their prescribed medication
- **Emotional State Assessment**: Checks patient emotional well-being during each interaction
- **Empathetic Responses**: Provides comfort, encouragement, and support to reduce fear and isolation
- **Intelligent Escalation**: Automatically schedules doctor appointments if symptoms worsen
- **Contextual Conversations**: Understands patient responses and adapts accordingly

### 💬 Telegram Bot + n8n Automation
- **Daily Medication Reminders**: Automated reminders sent at scheduled times (9 AM, 1 PM, 8 PM)
- **Interactive Responses**: Patients can reply to reminders with their medication status
- **Automatic Logging**: All responses are automatically logged in Google Sheets
- **Real-time Tracking**: Enables easy tracking of medication adherence over time
- **Negative Keyword Detection**: Identifies concerning responses that may require intervention
- **Seamless Integration**: Works alongside AI agent calls for comprehensive coverage

### 🌐 Sukoon Web App (Base44)
- **Centralized Dashboard**: Single platform accessible to patients, family members, and doctors
- **Real-time Medication Status**: Live view of medication adherence and timing
- **Emotional Logs**: Track emotional state patterns and trends over time
- **Call Summaries**: Detailed summaries of AI agent interactions
- **Multi-user Access**: Secure access for different stakeholders (patients, families, healthcare providers)
- **Data Visualization**: Charts and graphs for better understanding of patient progress

### 🧠 Empathetic Support
- **Beyond Data Collection**: Sukoon focuses on emotional support, not just data gathering
- **Active Listening**: AI agents listen attentively and respond with empathy
- **Comfort & Encouragement**: Provides emotional support to reduce patient isolation
- **Fear Reduction**: Helps alleviate anxiety and fear associated with mental health conditions
- **Personalized Interactions**: Tailored conversations based on individual patient needs

### 📈 Data Persistence & Monitoring
- **Google Sheets Integration**: Responses stored in spreadsheets for immediate access
- **Database Integration**: Designed for integration with Base44 database for scalability
- **Historical Tracking**: Long-term monitoring of medication adherence and emotional trends
- **Export Capabilities**: Data can be exported for clinical analysis and reporting
- **Audit Trails**: Complete logs of all interactions for accountability and review

### 🔐 Security & Scalability
- **Secure Architecture**: Built with security best practices for healthcare data
- **Scalable Design**: Can handle growing numbers of patients and interactions
- **Low-Cost Solution**: Designed to be affordable, especially for low-resource settings
- **Accessible Technology**: Uses widely available platforms (Telegram, Google Sheets)
- **Privacy Compliant**: Respects patient privacy and data protection requirements

## 🏗️ Architecture

### System Components

1. **Backend API (FastAPI)**
   - RESTful API endpoints for web app integration
   - Handles post-call data processing
   - Manages logging and data persistence

2. **AI Agent Layer**
   - Inya.ai integration for voice calls
   - Gnani.ai for natural language processing
   - Emotional state detection and analysis

3. **Automation Layer (n8n)**
   - Scheduled medication reminders
   - Telegram bot integration
   - Google Sheets data logging
   - Workflow automation

4. **Frontend (Base44)**
   - Web application dashboard
   - Real-time data visualization
   - Multi-user interface

5. **Data Storage**
   - Google Sheets (current implementation)
   - Base44 Database (planned integration)

## 📋 Project Structure

```
sukoon-ai/
├── sukoon_api.py                           # Main FastAPI application
├── requirements.txt                        # Python dependencies
├── Procfile                                # Deployment configuration
├── n8n_medication_reminder_workflow.json   # n8n automation workflow
└── README.md                               # Project documentation

Builathon_nxtwave/
├── sukoon_api.py      # Alternative FastAPI implementation
├── requirements.txt   # Python dependencies
├── Procfile           # Deployment configuration for Render/Heroku
└── README.md          # Project documentation
```

## 🚀 Setup

### Prerequisites
- Python 3.8+
- FastAPI
- Telegram Bot Token
- Google Sheets API credentials
- n8n instance (for automation workflows)

### Installation

1. Install dependencies:
```bash
cd sukoon-ai
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

# Google Sheets Configuration
GOOGLE_SHEETS_CREDENTIALS=path_to_credentials.json
GOOGLE_SHEET_ID=your_sheet_id

# AI Agent Configuration
INYA_AI_API_KEY=your_inya_api_key
GNANI_AI_API_KEY=your_gnani_api_key
```

3. Run the application:
```bash
uvicorn sukoon_api:app --reload
```

4. Import n8n workflow:
   - Import `n8n_medication_reminder_workflow.json` into your n8n instance
   - Configure Telegram and Google Sheets credentials in n8n
   - Activate the workflow

## 🌐 Deployment

This project includes a Procfile for deployment on platforms like Render or Heroku.

The server runs on port 10000 when deployed.

### Deployment Steps

1. Configure environment variables in your hosting platform
2. Deploy the FastAPI application
3. Set up n8n instance (can be self-hosted or cloud)
4. Import and activate automation workflows
5. Configure webhook endpoints for integrations

## 📡 API Endpoints

- `GET /` - Home endpoint - Returns service status
- `GET /api/sukoon/greeting` - Dynamic greeting message for patients
- `GET /api/sukoon/ending` - Dynamic ending message for calls
- `POST /api/sukoon/postcall` - Receives and logs post-call data from AI agent

### Example API Usage

```bash
# Get greeting
curl "http://localhost:8000/api/sukoon/greeting?patient_name=John"

# Post call data
curl -X POST "http://localhost:8000/api/sukoon/postcall" \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": "123",
    "call_summary": "...",
    "medication_status": "taken",
    "emotional_state": "calm"
  }'
```

## 🔄 Workflow

### Medication Reminder Flow
1. **Scheduled Trigger**: n8n workflow triggers at 9 AM, 1 PM, and 8 PM daily
2. **Data Retrieval**: Reads patient data from Google Sheets
3. **Reminder Sent**: Sends personalized Telegram message to each patient
4. **Response Handling**: Patient replies are captured via Telegram trigger
5. **Status Update**: Response is logged back to Google Sheets
6. **Conditional Logic**: Negative keywords trigger alerts for healthcare providers

### AI Agent Call Flow
1. **Daily Call Initiation**: AI agent calls patient at scheduled time
2. **Conversation**: Engages in empathetic conversation
3. **Assessment**: Checks medication status and emotional state
4. **Data Collection**: Gathers information about patient well-being
5. **Post-Call Processing**: Sends data to backend API
6. **Escalation**: If needed, automatically schedules doctor appointment

## 🎯 Impact

**Sukoon bridges the gap between psychiatric care and emotional support** — offering a comprehensive solution that combines:

- **Continuous Monitoring**: 24/7 support through multiple channels
- **Affordability**: Low-cost solution accessible to underserved populations
- **Humanized Care**: AI that understands empathy and emotional needs
- **Clinical Integration**: Seamless connection with healthcare providers
- **Family Involvement**: Enables families to stay informed and supportive
- **Data-Driven Insights**: Comprehensive tracking for better treatment outcomes

By providing continuous, affordable, and humanized mental health care, Sukoon addresses critical gaps in mental health services, particularly in resource-constrained environments. The platform reduces isolation, improves medication adherence, and ensures timely interventions when needed.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is part of the Sukoon mental health care platform.

## 📞 Support

For support and inquiries, please reach out through the appropriate channels.

---

**Built with ❤️ for better mental health care**
