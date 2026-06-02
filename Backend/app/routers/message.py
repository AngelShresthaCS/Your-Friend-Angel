
 
from fastapi import HTTPException, status, Depends, APIRouter
from .. hashing import pwd_context
from sqlalchemy.orm import Session
from .. schemas import ValidateMessage
from datetime import datetime
from .. import models
from .. database import get_db

router = APIRouter(
    prefix="/message",
    tags = ['messages']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_message(message: ValidateMessage, db: Session = Depends(get_db)):
    
    # 1. Receiver check
    receiver = db.query(models.User).filter(models.User.username == message.receiver).first()
    if receiver is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Can't find the receiver")
    
    # 2. Sender check
    sender = db.query(models.User).filter(models.User.username == message.user).first()
    if not sender:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )

    # 3. Verify the plaintext password against the saved database hash
    if not pwd_context.verify(message.password, sender.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )
    
    # 4. Construct the database object explicitly using the Pydantic object natively
    addmessage = models.Message(
        content=message.content,     # Read directly from Pydantic
        sender=sender.id,         # Mapped to the correct DB column
        receiver=receiver.id,     # Mapped to the correct DB column
        createdat=datetime.utcnow() # Assuming your DB column is named created_at
    )
    
    db.add(addmessage)
    db.commit()
    db.refresh(addmessage)
    
    return addmessage