from fastapi import   HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. schemas import User, ValidateUser
from .. import models, hashing
from .. database import  get_db

router = APIRouter(
    prefix="/user",
    tags = ['user']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User, db: Session = Depends(get_db)):
    if len(user.password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be 72 bytes or fewer"
        )

    try:
        hashed_password = hashing.hash(user.password)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Password hashing failed: {str(e)}"
        )

    user_data = user.model_dump()
    user_data["password"] = hashed_password
    new_user = models.User(**user_data)

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with that email or username already exists"
        )
@router.get("/",status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/login", status_code=status.HTTP_200_OK)
def login(user_credentials: ValidateUser, db: Session = Depends(get_db)):
    
    # Hunt down the user by their email
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    # If the email doesn't exist, kick them out
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )

    # If the email exists, verify the plaintext password against the saved database hash
    if not hashing.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )

    # 4. If they survive both checks, they are in
    return {"message": "Login successful", "user_id": user.id}
    