# Session Summary Fetch API

Public API to fetch saved session summaries from PostgreSQL (Supabase).

## Endpoint

```
GET /api/v1/records/fetch?semester=Semester 1&book_name=Microsoft 365&session_number=1
```

Returns:
```json
{
  "session_name": "Getting Started with Windows 11",
  "summary": "..."
}
```

## Local test

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# edit .env with your DATABASE_URL
uvicorn app.main:app --reload --port 8000
```

## Deployment to Render (free)

See deployment instructions in the conversation.