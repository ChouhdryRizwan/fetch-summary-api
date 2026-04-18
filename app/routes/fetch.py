import logging
from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.db_models import SummaryRecord

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/records", tags=["Records"])


@router.get(
    "/fetch",
    summary="Get a session summary by semester, book, and session number",
)
def fetch_summary(
    semester: str = Query(..., description="Semester name, e.g. 'Semester 1'"),
    book_name: str = Query(..., description="Book/module name, e.g. 'Microsoft 365'"),
    session_number: int = Query(..., description="Session number"),
    db: Session = Depends(get_db),
):
    record = (
        db.query(SummaryRecord)
        .filter(
            SummaryRecord.semester.ilike(semester),
            SummaryRecord.book_name.ilike(book_name),
            SummaryRecord.session_number == session_number,
        )
        .order_by(SummaryRecord.updated_at.desc())
        .first()
    )

    if not record:
        raise HTTPException(
            status_code=404,
            detail=(
                f"No summary found for semester='{semester}', "
                f"book='{book_name}', session={session_number}."
            ),
        )

    return {
        "session_name": record.session_name,
        "summary": record.summary,
    }