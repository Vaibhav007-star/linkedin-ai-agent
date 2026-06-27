# 🚀 LinkedIn AI Agent

An AI-powered LinkedIn content automation system built with Python and Google Gemini.

The project automatically collects AI and Data Science news, filters relevant articles, generates professional summaries, creates engaging LinkedIn posts, and prepares them for publishing.

> **Status:** 🚧 In Development

---

# Features

* 📡 Collect articles from multiple RSS feeds
* 🧠 Filter AI, Machine Learning, Data Science, and Python topics
* 💾 Store articles in SQLite
* 🤖 Generate AI-powered article summaries using Google Gemini
* ✍️ Create professional LinkedIn posts
* 🔄 Avoid duplicate articles
* 📊 Score and rank articles
* 📝 Structured logging
* ⚙️ Modular project architecture

---

# Tech Stack

* Python 3.12
* Google Gemini API
* SQLAlchemy
* SQLite
* Feedparser
* Loguru
* Python Dotenv

---

# Project Architecture

```text
RSS Feeds
     │
     ▼
RSS Collector
     │
     ▼
Topic Filter
     │
     ▼
SQLite Database
     │
     ▼
Gemini AI Summarizer
     │
     ▼
LinkedIn Writer
     │
     ▼
Database
```

---

# Current Project Structure

```text
linkedin-ai-agent/
│
├── app/
│   ├── analytics/
│   ├── classifier/
│   ├── collector/
│   ├── database/
│   ├── image_generator/
│   ├── publisher/
│   ├── reviewer/
│   ├── scheduler/
│   ├── summarizer/
│   ├── utils/
│   └── writer/
│
├── config/
├── database/
├── logs/
├── prompts/
├── tests/
│
├── main.py
├── setup_project.py
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/linkedin-ai-agent.git
```

Move into the project:

```bash
cd linkedin-ai-agent
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it (Windows):

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
DATABASE_URL=sqlite:///database/posts.db
LOG_LEVEL=INFO
```

---

# Run the Project

```bash
python main.py
```

---

# Development Roadmap

## ✅ Completed

* Project setup
* Logging
* SQLite database
* RSS collector
* Topic filtering
* Duplicate detection
* Gemini integration
* AI summarizer
* LinkedIn post writer

## 🚧 In Progress

* Reviewer Agent
* Hashtag Generator
* Image Prompt Generator

## 📅 Planned

* LinkedIn Publisher
* Scheduler
* Analytics Dashboard
* Human Approval Workflow
* Docker Support
* CI/CD Pipeline

---

# Future Workflow

```text
RSS Feed
      │
      ▼
Collector
      │
      ▼
Topic Filter
      │
      ▼
Summarizer
      │
      ▼
LinkedIn Writer
      │
      ▼
Reviewer
      │
      ▼
Image Prompt Generator
      │
      ▼
Human Approval
      │
      ▼
LinkedIn Publisher
      │
      ▼
Analytics Dashboard
```

---

# Learning Goals

This project demonstrates:

* AI-powered automation
* Prompt engineering
* Modular Python architecture
* REST API integration
* Database design
* Content generation workflows
* Production-ready software structure

---

# License

This project is licensed under the MIT License.

---

⭐ If you found this project interesting, consider starring the repository.
