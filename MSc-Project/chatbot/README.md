Access OpenAI API key as an environment variable
```
import os

api_key = os.environ.get('API_KEY')
```

Check environment variable in MacOS
`echo $OPENAI_API_KEY`

Run the Flask app:
`FLASK_APP=chatbot_backend.py flask run`