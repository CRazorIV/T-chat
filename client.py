import asyncio
import websockets

async def chat():
    uri = "ws://localhost:8765"
    username = input("Enter your username: ")

    async with websockets.connect(uri) as websocket:
        await websocket.send(username)  # Stuur username naar de server

        async def receive():
            async for message in websocket:
                print(f"\n📩 {message}")  # Berichten van andere gebruikers worden direct getoond

        async def send():
            while True:
                message = await asyncio.to_thread(input, f"{username}: ")
                if message.lower() == "exit":
                    break
                await websocket.send(message)

        asyncio.create_task(receive())  # Ontvangen start als achtergrondtaak
        await send()  # Blijf berichten sturen

asyncio.run(chat())
