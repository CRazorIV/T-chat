import websockets
import asyncio
import datetime

connected_clients = {}

async def handle_client(websocket):
    username = await websocket.recv()  # Vraag username
    connected_clients[websocket] = username
    print(f"{username} connected.")

    try:
        async for message in websocket:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            formatted_message = f"{username}/{timestamp}: {message}"
            print(formatted_message)

            # Stuur bericht naar alle clients
            for client in connected_clients.keys():
                if client != websocket:
                    await client.send(formatted_message)

    except websockets.exceptions.ConnectionClosed:
        print(f"{connected_clients[websocket]} disconnected.")
    finally:
        del connected_clients[websocket]  # Verwijder client bij disconnect

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # Houd server draaiend

asyncio.run(main())
