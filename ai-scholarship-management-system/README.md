# AI Scholarship Management System

A full-stack scholarship discovery and management platform with React, Express, MongoDB, and FastAPI ML recommendations.

## Modules
- Scholarship Discovery & Search
- AI Recommendation Engine
- Document Management
- Admin & Reporting

## Architecture
React/Vite -> Express API -> MongoDB
                      ↘ FastAPI recommendation service

## Run locally
1. Copy `.env.example` to `.env` and configure MongoDB.
2. `cd backend && npm install && npm run dev`
3. `cd frontend && npm install && npm run dev`
4. `cd ml-service && pip install -r requirements.txt && uvicorn app:app --reload --port 8000`

The project is intentionally isolated under `ai-scholarship-management-system/` so existing coursework files in this repository remain untouched.
