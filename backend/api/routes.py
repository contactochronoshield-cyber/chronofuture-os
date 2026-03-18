from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.deps import get_db
from core.auth import register_user, login_user
from core.system import system_status
from core.users import get_users
from core.courses import get_courses
from core.profiles import create_profile, get_profile
from core.community import create_post, get_posts

router = APIRouter()

# Sistema
router.get("/system")(system_status)

# Usuarios básicos
router.get("/users")(get_users)

# Cursos
router.get("/courses")(get_courses)

# Auth real con DB
router.post("/register")(
    lambda username, password, db=Depends(get_db): register_user(username, password, db)
)

router.post("/login")(
    lambda username, password, db=Depends(get_db): login_user(username, password, db)
)

# Perfiles
router.post("/profile")(create_profile)
router.get("/profile/{user_id}")(get_profile)

# Comunidad
router.post("/post")(create_post)
router.get("/community")(get_posts)
