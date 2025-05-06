# 📄 AI-Powered Resume Matcher

An intelligent system that analyzes resumes and job descriptions to compute match scores and help recruiters prioritize top candidates. Now includes a lightweight **Logistic Regression model** served through a Flask API for easy integration and deployment.

---

## 🚀 Features

- ✅ **Resume Parsing & Skill Extraction**
- ✅ **Job Description Analysis**
- ✅ **Match Score Calculation** using NLP & ML
- ✅ **Interactive Visual Analytics** (via Jupyter Notebook)
- ✅ **Logistic Regression Model** (deployed via API)
- ✅ **Health Endpoint for API Monitoring**
- ✅ Easy deployment & integration-ready

---

## ⚙️ API Endpoints

| Endpoint         | Method | Description                                   |
|------------------|--------|-----------------------------------------------|
| `/`              | GET    | Welcome page for the API                      |
| `/predict`       | POST   | Accepts job & resume JSON, returns prediction |
| `/health`        | GET    | Health check endpoint                         |

### Sample `/predict` Request Payload

```json
{
  "title": "Customer Service Representative",
  "location": "US, NY, New York",
  "department": "Support",
  "salary_range": "$50,000 - $60,000",
  "company_profile": "Fast-growing tech support firm",
  "description": "Answer customer queries and resolve issues.",
  "requirements": "Good communication skills required.",
  "benefits": "Health, 401K, and paid vacation.",
  "telecommuting": 0,
  "has_company_logo": 1,
  "has_questions": 0,
  "employment_type": "Full-time",
  "required_experience": "Mid-Senior level",
  "required_education": "Bachelor's Degree",
  "industry": "Information Technology",
  "function": "Customer Service"
}
