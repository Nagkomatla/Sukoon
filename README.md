# Sukoon - AI-Powered Mental Health Care Platform

<div align="center">

**Bridging the gap between psychiatric care and emotional support**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/Nagkomatla/Sukoon)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)

</div>

---

## 🌟 About Sukoon

**Sukoon** is a revolutionary mental health care platform designed to provide continuous, affordable, and humanized mental health care powered by AI. The platform specifically addresses the needs of patients with schizophrenia and other mental health conditions, offering 24/7 support through multiple integrated technologies.

### The Problem We Solve

Mental health care faces critical challenges:
- Limited access to continuous support between appointments
- Medication adherence monitoring gaps
- Emotional isolation and fear among patients
- High costs limiting accessibility
- Lack of real-time data for healthcare providers

### Our Solution

Sukoon combines **AI agents**, **automation**, and **empathetic technology** to create a holistic care ecosystem that:
- Provides daily check-ins and emotional support
- Monitors medication adherence in real-time
- Detects early warning signs of symptom escalation
- Connects patients, families, and healthcare providers
- Operates at low cost for maximum accessibility

---

## ✨ Key Features

### 🤖 AI Agent (Inya.ai + Gnani.ai)
- **Daily Patient Calls**: Automated empathetic conversations to check on patients
- **Medication Verification**: Ensures patients have taken prescribed medications
- **Emotional State Assessment**: Monitors mental and emotional well-being
- **Intelligent Escalation**: Automatically schedules doctor appointments when needed
- **Contextual Understanding**: Adapts conversations based on patient responses

### 💬 Telegram Bot + n8n Automation
- **Scheduled Reminders**: Daily medication reminders at 9 AM, 1 PM, and 8 PM
- **Interactive Responses**: Patients can respond directly via Telegram
- **Automatic Logging**: All interactions logged to Google Sheets
- **Negative Keyword Detection**: Identifies concerning responses for intervention
- **Real-time Tracking**: Live monitoring of medication adherence

### 🌐 Sukoon Web App (Base44)
- **Unified Dashboard**: Centralized platform for all stakeholders
- **Real-time Monitoring**: Live medication status and emotional logs
- **Call Summaries**: Detailed AI agent interaction records
- **Multi-user Access**: Patients, families, and doctors in one platform
- **Data Visualization**: Charts and trends for better insights

### 🧠 Empathetic Support
- **Humanized AI**: Focuses on emotional support, not just data collection
- **Active Listening**: AI agents that truly understand and respond with empathy
- **Comfort & Encouragement**: Reduces patient isolation and fear
- **Personalized Care**: Tailored interactions based on individual needs

### 📈 Data & Monitoring
- **Persistent Storage**: Google Sheets integration with database scalability
- **Historical Tracking**: Long-term monitoring of adherence and trends
- **Clinical Integration**: Data ready for healthcare provider analysis
- **Privacy Compliant**: Secure handling of sensitive health information

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Sukoon Platform                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │   AI Agent   │  │ Telegram Bot │  │  Web App     │ │
│  │ (Inya.ai +   │  │   + n8n      │  │  (Base44)    │ │
│  │  Gnani.ai)   │  │ Automation   │  │              │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘ │
│         │                  │                  │         │
│         └──────────────────┼──────────────────┘         │
│                            │                            │
│                    ┌───────▼────────┐                   │
│                    │  Backend API   │                   │
│                    │   (FastAPI)    │                   │
│                    └───────┬────────┘                   │
│                            │                            │
│                    ┌───────▼────────┐                   │
│                    │  Data Storage  │                   │
│                    │ Google Sheets  │                   │
│                    │  + Base44 DB   │                   │
│                    └────────────────┘                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Repository Structure

```
Sukoon/
├── README.md                              # This file - Main documentation
├── .gitignore                             # Git ignore rules
│
└── sukoon-ai/                             # Backend API directory
    ├── README.md                          # Detailed backend documentation
    ├── sukoon_api.py                      # FastAPI application
    ├── requirements.txt                   # Python dependencies
    ├── Procfile                           # Deployment configuration
    ├── n8n_medication_reminder_workflow.json  # n8n automation workflow
    │
    └── Builathon_nxtwave/                 # Alternative deployment setup
        ├── sukoon_api.py
        ├── requirements.txt
        ├── Procfile
        └── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Telegram Bot Token
- Google Sheets API credentials
- n8n instance (for automation workflows)
- Inya.ai and Gnani.ai API keys

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nagkomatla/Sukoon.git
   cd Sukoon/sukoon-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   # Create a .env file with:
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   GOOGLE_SHEETS_CREDENTIALS=path_to_credentials.json
   GOOGLE_SHEET_ID=your_sheet_id
   INYA_AI_API_KEY=your_inya_api_key
   GNANI_AI_API_KEY=your_gnani_api_key
   ```

4. **Run the backend server**
   ```bash
   uvicorn sukoon_api:app --reload
   ```

5. **Set up n8n workflow**
   - Import `n8n_medication_reminder_workflow.json` into your n8n instance
   - Configure credentials for Telegram and Google Sheets
   - Activate the workflow

For detailed setup instructions, see [sukoon-ai/README.md](sukoon-ai/README.md).

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Service health check |
| `GET` | `/api/sukoon/greeting?patient_name={name}` | Generate personalized greeting |
| `GET` | `/api/sukoon/ending?patient_name={name}` | Generate personalized ending message |
| `POST` | `/api/sukoon/postcall` | Receive and log post-call data from AI agent |

See the [API documentation](sukoon-ai/README.md#-api-endpoints) for detailed examples.

---

## 🔄 How It Works

### Medication Reminder Flow
1. **Scheduled Trigger**: n8n workflow activates at 9 AM, 1 PM, and 8 PM daily
2. **Data Retrieval**: Reads patient information from Google Sheets
3. **Reminder Sent**: Sends personalized Telegram message to each patient
4. **Response Capture**: Patient replies are received via Telegram
5. **Status Update**: Responses are automatically logged to Google Sheets
6. **Alert System**: Negative keywords trigger alerts for healthcare providers

### AI Agent Call Flow
1. **Call Initiation**: AI agent calls patient at scheduled time
2. **Empathetic Conversation**: Engages in supportive dialogue
3. **Assessment**: Checks medication status and emotional state
4. **Data Collection**: Gathers comprehensive patient information
5. **Post-Call Processing**: Sends data to backend API for logging
6. **Escalation**: Automatically schedules doctor appointment if needed

---

## 🎯 Impact

### For Patients
- ✅ **24/7 Support**: Continuous care and emotional support
- ✅ **Medication Adherence**: Improved compliance through reminders
- ✅ **Reduced Isolation**: Empathetic AI companionship
- ✅ **Early Intervention**: Timely detection of concerning symptoms

### For Families
- ✅ **Peace of Mind**: Real-time visibility into patient well-being
- ✅ **Easy Monitoring**: Simple dashboard to track progress
- ✅ **Involvement**: Stay connected and supportive

### For Healthcare Providers
- ✅ **Better Insights**: Comprehensive data for informed decisions
- ✅ **Efficiency**: Automated monitoring reduces manual work
- ✅ **Early Warning**: Proactive alerts for intervention
- ✅ **Scalability**: Care for more patients effectively

### For Healthcare Systems
- ✅ **Affordability**: Low-cost solution for resource-constrained settings
- ✅ **Accessibility**: Reaches underserved populations
- ✅ **Scalability**: Grows with patient needs
- ✅ **Compliance**: Secure and privacy-compliant

---

## 🔐 Security & Privacy

- **Secure Architecture**: Built with healthcare data security best practices
- **Privacy Compliant**: Respects patient privacy and data protection requirements
- **Access Control**: Secure multi-user access with role-based permissions
- **Data Encryption**: Secure transmission and storage of sensitive information

---

## 🌍 Use Cases

- **Psychiatric Care**: Primary use case for schizophrenia and related conditions
- **Medication Management**: Any condition requiring medication adherence
- **Mental Health Monitoring**: Depression, anxiety, bipolar disorder support
- **Elderly Care**: Medication reminders and wellness checks
- **Chronic Disease Management**: Ongoing health monitoring and support

---

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is part of the Sukoon mental health care platform. See the repository for license information.

---

## 📞 Support & Contact

- **GitHub Issues**: [Report bugs or request features](https://github.com/Nagkomatla/Sukoon/issues)
- **Repository**: [View on GitHub](https://github.com/Nagkomatla/Sukoon)

---

## 🙏 Acknowledgments

- **Inya.ai** and **Gnani.ai** for AI agent capabilities
- **n8n** for workflow automation
- **Base44** for web application platform
- **Telegram** for messaging infrastructure

---

<div align="center">

**Built with ❤️ for better mental health care**

**Making mental health support accessible, affordable, and empathetic**

[⭐ Star this repo](https://github.com/Nagkomatla/Sukoon) | [🐛 Report Bug](https://github.com/Nagkomatla/Sukoon/issues) | [💡 Request Feature](https://github.com/Nagkomatla/Sukoon/issues)

</div>

