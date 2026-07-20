# 🚀 AI Marketing Automation Agent

[![Deployed on Streamlit](https://img.shields.io/badge/Deployed%20on-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai-marketing-automation-agent-ocjcj7nxnsj8ssxvkfhjm7.streamlit.app/)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq API](https://img.shields.io/badge/API-Groq-FF6B6B?style=for-the-badge&logo=groq&logoColor=white)](https://console.groq.com)
[![License](https://img.shields.io/badge/License-Proprietary-FF0000?style=for-the-badge)](LICENSE)

> **An intelligent marketing assistant powered by Groq AI** that generates high-quality marketing content, campaign ideas, hashtags, emails, and custom promotional material for businesses of all sizes.
>
<img width="1536" height="1024" alt="ChatGPT Image Jul 20, 2026, 04_42_48 PM" src="https://github.com/user-attachments/assets/19fea893-7c80-44e5-8390-b68c052b5b92" />  

>
> 


---

## 📌 Overview

**AI Marketing Automation Agent** is a Streamlit-based web application designed to help businesses, marketers, and content creators automate their marketing workflows. Leveraging the power of **Groq's Llama 3.3 70B** model, it generates tailored marketing content based on user-defined business details, target audience, tone, and branding.

Whether you need social media posts, email campaigns, hashtag strategies, or creative campaign ideas — this tool delivers professional-grade content in seconds.

---

## 🚀 Live Demo

The application is live and accessible at:

🔗 **[https://ai-marketing-automation-agent-ocjcj7nxnsj8ssxvkfhjm7.streamlit.app/](https://ai-marketing-automation-agent-ocjcj7nxnsj8ssxvkfhjm7.streamlit.app/)**

[![Open App](https://img.shields.io/badge/🚀_Open_App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://ai-marketing-automation-agent-ocjcj7nxnsj8ssxvkfhjm7.streamlit.app/)

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📝 **Content Generator** | Generate complete marketing content including social media posts, emails, blog intros, and CTAs |
| 💡 **Campaign Ideas** | Get 5 creative campaign ideas tailored to your business and audience |
| #️⃣ **Hashtags** | Generate 30+ relevant hashtags categorized by industry, brand, and trends |
| ✉️ **Email Campaigns** | Create professional email sequences with subject lines and follow-ups |
| 🎨 **Custom Prompts** | Write your own prompt for fully customized content generation |
| 🌙 **Dark/Light Mode** | Switch between themes for comfortable viewing |
| 📄 **DOCX Export** | Download generated content as Microsoft Word documents |
| 🔐 **Secure API Handling** | API keys managed securely via Streamlit Secrets |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Frontend framework for rapid UI development |
| **Groq API (Llama 3.3 70B)** | High-performance LLM for content generation |
| **Python-DOCX** | Word document generation |
| **Python-Dotenv** | Environment variable management |
| **Streamlit Cloud** | Hosting and deployment |

---

## 📋 How It Works

1. **Fill Business Details** – Enter business name, industry, target audience, country, brand name, and tone of voice
2. **Select Content Type** – Choose from Content, Ideas, Hashtags, Email, or Custom
3. **Generate** – Click generate and let AI create professional marketing material
4. **Download** – Export content as DOCX for further editing

---

## 📦 Installation (Local Development)

```bash
# Clone the repository
git clone https://github.com/usman-official-ai/AI-Marketing-Automation-Agent.git
cd AI-Marketing-Automation-Agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# Run the app
streamlit run app.py

.

📂 Project Structure

AI-Marketing-Automation-Agent/  
├── app.py                  # Main application file  
├── requirements.txt        # Python dependencies  
├── .gitignore             # Git ignore rules  
├── README.md              # Project documentation  
├── modules/               # Modular components  
│   ├── content_generator.py  
│   ├── marketing_ideas.py  
│   ├── hashtag_generator.py  
│   └── email_generator.py  
├── utils/                 # Utility functions  
│   ├── docx_generator.py  
│   
└── assets/                # Static assets  
    └── style.css  

🧪 Testing  
Local Testing
streamlit run app.py
Cloud Testing
Access the live deployment at the URL above and test all features.

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add some AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is proprietary and confidential. Unauthorized copying, distribution, or use is strictly prohibited.

👨‍💻 Author
usman-official-ai – GitHub

