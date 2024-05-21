import requests
from flask import Flask, render_template, url_for, request
from flask import request as req

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/Summarize", methods=["GET", "POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        data = req.form["data"]
        maxL = int(req.form["maxL"])
        minL = maxL // 4

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })[0]

        return render_template("index.html", result=output["summary_text"])
    else:
        return render_template("index.html")


#chatgpt wala 
# import os
# import requests
# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask import request as req


# app = Flask(__name__)
# app.secret_key = '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'  # Replace with your actual secret key


# app = Flask(__name__)
# @app.route("/",methods=["GET","POST"])
# def Index():
#     return render_template("index.html")

# @app.route("/Summarize",methods=["GET","POST"])
# def Summarize():
#     if req.method== "POST":
#         API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
#         headers = {"Authorization": f"Bearer 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"}

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if req.method == "POST":
#         data = req.form.get("data")
#         max_length = req.form.get("maxL")
        
#         if not data or not max_length:
#             flash("Please provide both text data and maximum length.", "error")
#             return redirect(url_for("index"))

#         try:
#             max_length = int(max_length)
#         except ValueError:
#             flash("Maximum length must be an integer.", "error")
#             return redirect(url_for("index"))
        
#         min_length = max_length // 4

#         payload = {
#             "inputs": data,
#             "parameters": {"min_length": min_length, "max_length": max_length}
#         }

#         try:
#             response = requests.post(API_URL, headers=HEADERS, json=payload)
#             response.raise_for_status()
#             summary = response.json()[0]["summary_text"]
#             return render_template("index.html", result=summary)
#         except requests.exceptions.RequestException as e:
#             flash(f"An error occurred: {e}", "error")
#             return redirect(url_for("index"))

#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)
