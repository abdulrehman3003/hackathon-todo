import pytest
from httpx import AsyncClient
from sqlmodel import Session, select
from app.models.task import Task
from app.models.user import User
from app.auth.jwt import create_access_token
from uuid import UUID

async def create_test_user(session: Session, email: str = "test_user@example.com", password: str = "password123") -> User:
    from app.auth.service import get_password_hash
    user = User(email=email, password_hash=get_password_hash(password))
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def get_auth_headers(user_id: UUID, user_email: str) -> dict:
    token = create_access_token({"sub": str(user_id), "email": user_email})
    return {"Authorization": f"Bearer {token}"}

@pytest.mark.asyncio
async def test_create_task_success(client: AsyncClient, session: Session):
    user = await create_test_user(session)
    headers = await get_auth_headers(user.id, user.email)
    response = await client.post(
        "/tasks/",
        json={"title": "New Task", "description": "Description for new task"},
        headers=headers
    )
    assert response.status_code == 201
    assert response.json()["title"] == "New Task"
    assert response.json()["user_id"] == str(user.id)
    assert response.json()["completed"] == False

@pytest.mark.asyncio
async def test_create_task_missing_title(client: AsyncClient, session: Session):
    user = await create_test_user(session)
    headers = await get_auth_headers(user.id, user.email)
    response = await client.post(
        "/tasks/",
        json={"description": "Description for new task"},
        headers=headers
    )
    assert response.status_code == 422 # Pydantic validation error

@pytest.mark.asyncio
async def test_list_tasks_pagination(client: AsyncClient, session: Session):
    user = await create_test_user(session)
    headers = await get_auth_headers(user.id, user.email)
    
    for i in range(5):
        session.add(Task(title=f"Task {i}", user_id=user.id))
    await session.commit()

    response = await client.get("/tasks/?limit=2&offset=1", headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    meta = response.json()["meta"]
    assert len(data) == 2
    assert meta["total"] == 5
    assert meta["limit"] == 2
    assert meta["offset"] == 1

@pytest.mark.asyncio
async def test_get_task_not_owner(client: AsyncClient, session: Session):
    user1 = await create_test_user(session, email="user1@example.com")
    user2 = await create_test_user(session, email="user2@example.com")
    
    task1 = Task(title="User1's Task", user_id=user1.id)
    session.add(task1)
    await session.commit()
    await session.refresh(task1)

    headers2 = await get_auth_headers(user2.id, user2.email)
    response = await client.get(f"/tasks/{task1.id}", headers=headers2)
    assert response.status_code == 403
    assert response.json() == {"detail": "Access denied", "code": "forbidden"}

@pytest.mark.asyncio
async def test_update_task_success(client: AsyncClient, session: Session):
    user = await create_test_user(session)
    task = Task(title="Task to Update", user_id=user.id)
    session.add(task)
    await session.commit()
    await session.refresh(task)

    headers = await get_auth_headers(user.id, user.email)
    response = await client.put(
        f"/tasks/{task.id}",
        json={"title": "Updated Task", "completed": True},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    assert response.json()["completed"] == True

@pytest.mark.asyncio
async def test_toggle_task(client: AsyncClient, session: Session):
    user = await create_test_user(session)
    task = Task(title="Task to Toggle", user_id=user.id, completed=False)
    session.add(task)
    await session.commit()
    await session.refresh(task)

    headers = await get_auth_headers(user.id, user.email)
    response = await client.patch(f"/tasks/{task.id}/toggle", headers=headers)
    assert response.status_code == 200
    assert response.json()["completed"] == True

    response = await client.patch(f"/tasks/{task.id}/toggle", headers=headers)
    assert response.status_code == 200
    assert response.json()["completed"] == False

@pytest.mark.asyncio
async def test_delete_task_success(client: AsyncClient, session: Session):
    user = await create_test_user(session)
    task = Task(title="Task to Delete", user_id=user.id)
    session.add(task)
    await session.commit()
    await session.refresh(task)

    headers = await get_auth_headers(user.id, user.email)
    response = await client.delete(f"/tasks/{task.id}", headers=headers)
    assert response.status_code == 204

    # Verify task is deleted
    response = await client.get(f"/tasks/{task.id}", headers=headers)
    assert response.status_code == 404
