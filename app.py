from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")


@app.route("/bot", methods=["POST"])
def response():
    query=dict(request.form)['query']
    res=english_bot.get_response(query)
    return jsonify({"response": res})


if __name__ == "__main__":
    app.run(host="0.0.0.0",)
