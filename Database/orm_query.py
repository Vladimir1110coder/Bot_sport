from Database.models import Player
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

async def orm_add_player(session: AsyncSession, data: dict):
    obj = Player(
        name = data["name"],
        word = data["word"]

    )

    session.add(obj)

    await session.commit()


async def orm_get_players(session: AsyncSession):
    query = select(Player)
    result = await session.execute(query)
    return result.scalars().all()
