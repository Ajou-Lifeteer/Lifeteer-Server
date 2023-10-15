from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


etc = APIRouter()

templates = Jinja2Templates(directory="test")


# 애플리케이션 로딩시 필요 데이터를 조회하기 위한 API
@etc.get('/', response_class=HTMLResponse)
async def init_client(request: Request):
    return templates.TemplateResponse("test.html", {"request": request, "name": "World"})


# 챗봇으로부터 응답을 받기 위한 API
@etc.get('/get-response')
async def get_chatbot_response():
    return {'msg': '~~~~'}


# 사용자의 월간 활동기록을 조회하기 위한 API
@etc.get('/get-monthly-log')
async def get_monthly_log():
    return {'msg': '~~~'}


# 사용자의 아카이브 활동기록을 조회하기 위한 API
@etc.get('/get-archive-log')
async def get_archive_log():
    return {'msg': '~~~'}


# 사용자의 Toekn을 재발급하기 위한 API
@etc.get('/update-token')
async def update_user_token():
    return {'msg': '~~~'}


# 미션을 완료하기 위한 API
@etc.get('complete-mission')
async def complete_mission():
    return {'msg': '~~~'}
