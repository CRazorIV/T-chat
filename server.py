import websockets
import asyncio

connected_clients = set()

async def handle_client(websocket, path=None):  # 'path' is nu optioneel
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Message received: {message}")
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Client has terminated the connection!")
    finally:
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # Houd de server draaiend

asyncio.run(main())  # Start de event loop correct
