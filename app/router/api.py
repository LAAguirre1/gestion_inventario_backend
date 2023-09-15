from fastapi import APIRouter

import app.router.endpoints.users as users
import app.router.endpoints.login as login
import app.router.endpoints.toner as toner
import app.router.endpoints.impresora as impresora
import app.router.endpoints.entrega as entrega

api_router = APIRouter()
api_router.include_router(login.router, tags=["Login"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(toner.router, prefix="/toner", tags=["Toners"])
api_router.include_router(impresora.router, prefix="/impresora", tags=["Impresoras"])
api_router.include_router(entrega.router, prefix="/entrega", tags=["Entregas"])