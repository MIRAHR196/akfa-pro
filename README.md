🏗️ Akfa Build — Interactive Backend Engine

An enterprise-ready, modular backend architecture designed for digital material management, estimation, and dynamic interaction systems. Engineered with a human-centric interactive CLI shell interface transitioning into scalable RESTful API services.

🌟 Key Features

Interactive Shell Interface: Human-centric, colorful CLI with custom ANSI formatting and interactive navigational routing.

Clean Architecture: Strict separation of concerns (API Routers, Pydantic Schemas, ORM Data Models, Business Logic Services).

FastAPI Core Engine: Async-first REST endpoints for high throughput and low latency operations.

PostgreSQL Integration: Robust relational database modeling with SQLAlchemy and database migration tracking via Alembic.

Enterprise Modules:

📐 Templates: Reusable design & building blueprints.

📦 Materials: Raw inventory, pricing, and resource tracking.

🏗️ Projects: Construction lifecycle, stage updates, and estimations.

💬 Comments & Feedback: User interaction, ratings, and audit logs.

🖼️ Media: File attachments, portfolio showcases, and blueprints.

🗄️ Archive: Soft deletion system and historic state management.

📐 Project Architecture

akfa-pro/
├── app/
│   ├── api/          # Route handlers & endpoints
│   ├── core/         # Security, database, & config setup
│   ├── models/       # SQLAlchemy database entities
│   ├── schemas/      # Pydantic request/response models
│   └── services/     # Core domain business logic
├── akfa.py           # Interactive CLI Engine entry point
├── main.py           # FastAPI ASGI application entry point
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation


🚀 Getting Started

Prerequisites

Python 3.12 or higher

Git

Installation

Clone the repository:

git clone https://github.com/MIRAHR196/akfa-pro.git
cd akfa-pro


Create and activate a virtual environment:

# Windows (Git Bash / PowerShell)
python -m venv venv
source venv/Scripts/activate  # Git Bash
# .\venv\Scripts\Activate.ps1 # PowerShell


Install dependencies:

pip install -r requirements.txt


Run the Interactive CLI:

python akfa.py


📋 Development Roadmap

[x] Initial Interactive CLI prototype & routing

[x] Version Control Setup & Clean Git workflow

[ ] FastAPI Application Setup & Endpoint Routing

[ ] Pydantic V2 Schemas & Data Validation Layer

[ ] SQLAlchemy ORM & PostgreSQL Database Integration

[ ] JWT Authentication & Role-Based Access Control (RBAC)

[ ] Docker Containerization & CI/CD Pipeline

👨‍💻 Author

Mirahror Mirzaakbarov

GitHub: @MIRAHR196

Specialty: Python / FastAPI Backend Engineering

Developed with a focus on scalable architecture and interactive user experiences
