import openai
import json
from flask import Flask, request, render_template
#API key
openai.api_key = ""

app = Flask(__name__,template_folder='templates', static_folder='static')
@app.route("/send-message", methods=["POST"])
def index():
  return render_template('index.html')
def send_message():
  # Get message from request
  data = request.get_json()
  message = data["message"]
  response = openai.Completion.create(
    model="davinci-002",
    prompt=message,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  response_text = response["choices"][0]["text"]

  # Return response to client
  return {"response": response_text}
print('working')

if __name__ == "__main__":
    app.run()