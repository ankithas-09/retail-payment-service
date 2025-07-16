from app.models.orm_models import AuditLog
from app.models.database import SessionLocal

def log_action(action: str, details: str):
    db = SessionLocal()
    log = AuditLog(action=action, details=details)
    db.add(log)
    db.commit()
    db.close()
