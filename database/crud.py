from sqlalchemy.orm import Session


def read(db: Session, model, domain):
    return db.query(model).filter(domain).first()


def read_all(db: Session, model, domain, skip: int = 0, limit: int = 100):
    return db.query(model).filter(domain).offset(skip).limit(limit).all()

def create(db: Session,model,**data):
    db_user = model(data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
