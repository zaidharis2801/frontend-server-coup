from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import httpx

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Response Viewer</title>
    </head>
    <body>
        <h1>API Response Viewer</h1>
        <button onclick="fetchAPI()">Fetch API Response</button>
        <pre id="response"></pre>
        <script>
            async function fetchAPI() {
                const response = await fetch('/get_result');
                const data = await response.json();
                document.getElementById('response').innerText = JSON.stringify(data, null, 2);
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/get_result")
async def get_result():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            'http://127.0.0.1:8000/get_result',
            json={
                "action": "Foreign Aid",
                "character": "Duke",
                "target": "Player1",
                "cards": ["Duke", "Assassin"],
                "probability": 1.0,
                "intermediate_steps": []
            }
        )
        return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
