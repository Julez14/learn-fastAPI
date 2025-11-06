# learn-fastAPI
Learning how to use FastAPI.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`
- Alternative API docs (ReDoc): `http://127.0.0.1:8000/redoc`

## Example Endpoints

- `GET /` - Welcome message
- `GET /hello/{name}` - Personalized greeting
