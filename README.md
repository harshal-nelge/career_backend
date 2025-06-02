# 🚀 Career Navigator


> An AI-powered career recommendation system that provides personalized career suggestions based on your educational background, interests, skills, and certifications.

## 🌐 Live Demo

🔗 **[Try Laksh AI]([https://laksh-ai.vercel.app/])**



## ✨ Features

- 🤖 **AI-Powered Recommendations** - Uses Google's Generative AI for intelligent career matching
- 👤 **Personalized Analysis** - Considers specialization, interests, skills, and certifications
- 🔥 **RESTful API** - Clean endpoints for seamless frontend integration
- 💾 **Data Persistence** - SQLite database for storing user profiles and recommendations
- ⚡ **Fast & Scalable** - Built with Django and optimized for performance
- 🛡️ **Secure Authentication** - Google OAuth2 integration

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Django 5.0.6 | Backend Framework |
| Django REST Framework | API Development |
| Google Generative AI | Career Recommendations |
| SQLite3 | Database |
| Google OAuth2 | Authentication |

## 📦 Installation

### Prerequisites
- Python 3.8+
- Google Cloud Platform account
- Google Generative AI API access

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/career-navigator.git
   cd career-navigator/career_backend/career_navigator
   ```

2. **Setup virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Google Cloud**
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/)
   - Enable the Generative Language API
   - Create OAuth2 credentials and download as `client_secret.json`
   - Place in the project root directory

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## 🔗 API Reference

### Get Career Recommendations

**Endpoint:** `POST /career/recommend/`

**Request Body:**
```json
{
    "specialization": "Computer Science",
    "interest": "Machine Learning, Data Analysis, AI Research",
    "skills": "Python, TensorFlow, SQL, Statistics, Data Visualization",
    "certification": "AWS Machine Learning, Google Analytics Certified"
}
```

**Response:**
```json
[
    "Senior Data Scientist",
    "Machine Learning Engineer", 
    "AI Research Scientist",
    "Business Intelligence Lead"
]
```

**cURL Example:**
```bash
curl -X POST http://localhost:8000/career/recommend/ \
  -H "Content-Type: application/json" \
  -d '{
    "specialization": "Computer Science",
    "interest": "Web Development, Cloud Computing",
    "skills": "JavaScript, React, AWS, Docker",
    "certification": "AWS Solutions Architect"
  }'
```

