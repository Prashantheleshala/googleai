from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("user_input")

    with open("/Users/prashantheleshala/Desktop/genaiapps/task_app1/key/gemini_key.txt", "r") as f:
        key = f.read()
        genai.configure(api_key=key)

    # Init the gemini model
    model = genai.GenerativeModel(
        model_name='gemini-1.5-pro-latest',
        system_instruction="""You are a polite, helpful AI data science Tutor. Given a data science
                              topic, help the user to understand it. If the question is not related to data science,
                              politely say you cannot answer."""
    )

    if user_input:
        # Generate AI response
        ai_response = model.generate_content(user_input)
        return jsonify({"role": "assistant", "content": ai_response.text})
    else:
        return jsonify({"role": "assistant", "content": "Please provide input."})

if __name__ == "__main__":
    app.run(debug=True)
