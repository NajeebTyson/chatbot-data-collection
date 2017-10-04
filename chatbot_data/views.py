# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# Create your views here.

# DB COnfig
db = "chatbot_data"
db_url = "mongodb://127.0.0.1:27017/"
storage_adapter="chatterbot.storage.MongoDatabaseAdapter"

# #bot config
bot = ChatBot(
    'PakBot',
    storage_adapter=storage_adapter,
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    filters=[
        'chatterbot.filters.RepetitiveResponseFilter'
    ],
    database_uri=db_url,
    database=db
)

convo1= [
    "what is the length of river Indus?",
    "2,896 km",
    "which is the worlds second highest peak?",
    "K2",
    "What is total Labour force?",
    "46.84 million",
    "How many communication Post Offices?",
    "12170",
    "How many railway stations in Pakistan?",
    "781",
    "Total length of roads in Pakistan?",
    "259,758 km",
    "How many professional colleges?",
    "382",
    "How many universities?",
    "51",
    "How many high schools?",
    "16100",
    "How many doctors in Pakistan?",
    "113206",
    "Popular games of Pakistan?",
    "Cricket, Hockey, Kabarri",
    "what is national sport of Pakistan?",
    "Hockey",
    "What is national bird?",
    "Chakor",
    "What is national animal of Pakitan?",
    "Markhor",
    "What is nationa tree of Pakistan?",
    "Deodar",
    "National flower?",
    "Jasmine",
    "When did Pakistan won the cricket world cup?",
    "1992",
    "Who is the composer of national anthem of Pakistan?",
    "Abdul Asar Hafeez Jalandhri",
    "Literacy rate of Pakistan?",
    "53%",
    "Official language of Pakistan?",
    "English",
    "National Lanuage of Pakistan?",
    "Urdu",
    "What is the currency of Pakistan?",
    "Rupee",
    "What is the capital of Pakistan?",
    "Islamabad",
    "Who is the current president of Pakistan?",
    "Mamnoon Hussain",
    "National poet of Pakistan?",
    "Allama Iqbal"
]

#train
bot.set_trainer(ListTrainer)
bot.train(convo1)


def index(request):
    if request.method == 'GET':
        template = loader.get_template('chatbot_data/index.html')
        return HttpResponse(template.render(None, request))


@csrf_exempt
def question(request):
    if request.method == 'GET':
        return Http404
    elif request.method == 'POST':
        myQuestion = request.POST["question"]
        my_response = str(bot.get_response(myQuestion))
        new_question = {}
        new_question["question"] = myQuestion
        new_question["answer"] = my_response
        data = None
        with open('./chatbot_data/question_data.json') as out_file:
            data = json.load(out_file)
        data.append(new_question)
        with open('./chatbot_data/question_data.json', "w") as out_file:
            json.dump(data, out_file)
        return JsonResponse({"response": my_response})
