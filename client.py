import asyncio
import websockets


async def chat():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Start twee async taken: één voor verzenden, één voor ontvangen
        asyncio.create_task(receive_messages(websocket))

        while True:
            message = input("You: ")
            await websocket.send(message)


async def receive_messages(websocket):
    async for message in websocket:
        print(f"\nOther: {message}\nYou: ", end="")


asyncio.run(chat())
