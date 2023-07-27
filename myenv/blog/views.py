from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests

bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

list_of_response = [
    "Hi!",
    "Hello! How can I assist you today?",
    "How are you?",
    "I'm good, thank you!",
    "What is your name?",
    "My name is ChatBot.",
    "Nice to meet you.",
    "Likewise!",
    "What's the capital of France?",
    "The capital of France is Paris.",
    "How does a computer work?",
    "Computers process data using electrical circuits and binary code.",
    "What's the weather like today?",
    "What's your favorite color?",
    "I don't have preferences as I'm just an AI, but I like all colors!",
    "How do I get to the nearest coffee shop?",
    "I'm sorry, I don't have access to your location. You can use a maps app to find the nearest coffee shop.",
    "Can you sing a song?",
    "I'm sorry, but I don't have a singing capability. But I can answer your questions!",
    "What's the population of Nepal?",
    "As of my last update, the population of Nepal is approximately 30 million.",
    "Tell me a fun fact.",
    "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "Who is the current Prime Minister of Nepal?",
    "The current Prime Minister of Nepal is [Name of the Prime Minister].",
    "How do I say 'thank you' in Nepali?",
    "In Nepali, 'thank you' is said as 'धन्यवाद' (pronounced as 'dhanyabaad').",
    "What are the popular tourist destinations in Nepal?",
    "Nepal is famous for its beautiful landscapes and trekking destinations. Some popular tourist spots include Mount Everest, Pokhara, Kathmandu Valley, Chitwan National Park, and Lumbini.",
    "Can you tell me a Nepali proverb?",
    "Certainly! Here's a Nepali proverb: 'जहाँ चाह, त्यहाँ राह' (pronounced as 'jahaan chaah, tyahaan raah'), which means 'Where there's a will, there's a way.'",
    "What's the time now in Nepal?",
    "I'm sorry, I don't have access to real-time data. Please check the local time in Nepal using a world clock or time zone converter.",
    "What's the currency of Nepal?",
    "The currency of Nepal is the Nepalese Rupee (NPR).",
    "How do I get a tourist visa for Nepal?",
    "You can apply for a tourist visa to Nepal through the Nepalese Embassy or Consulate in your country or apply for a visa on arrival at the Tribhuvan International Airport in Kathmandu.",
    "Tell me a famous Nepali dish.",
    "One famous Nepali dish is 'Dal Bhat,' which consists of lentil soup (dal) and steamed rice (bhat) served with various side dishes.",
    "What's the average temperature in Nepal during winter?",
    "The average temperature in Nepal during winter varies depending on the region. In Kathmandu, the average temperature ranges from 7°C to 20°C.",
    "What are the major languages spoken in Nepal?",
    "Nepali is the official language of Nepal. Additionally, there are various regional languages and dialects spoken by different ethnic groups.",
    "Can you recommend a good trekking route in Nepal?",
    "The Everest Base Camp trek and the Annapurna Circuit trek are two popular and breathtaking trekking routes in Nepal.",
    "What's the national flower of Nepal?",
    "The national flower of Nepal is 'Rhododendron arboreum,' commonly known as the 'Lali Gurans' in Nepali.",
    "Tell me a famous mythological story from Nepal.",
    "The story of 'Goddess Taleju' is a famous mythological story from Nepal. She is considered a protective deity of the Kathmandu Valley.",
    "What's the highest mountain peak in Nepal?",
    "The highest mountain peak in Nepal is Mount Everest, also known as 'Sagarmatha' in Nepali and 'Chomolungma' in Tibetan.",
    "Do you have any tips for traveling to Nepal?",
    "If you plan to visit Nepal, make sure to carry warm clothing, especially if you are trekking in the mountains. Respect the local customs and traditions, and try some authentic Nepali cuisine.",
    "Can you recommend some traditional Nepali music?",
    "Nepali folk songs and traditional music are rich in cultural significance. You can listen to 'Dohori' songs, 'Bhajans,' and traditional 'Panche Baja' music.",
    "What's the major festival celebrated in Nepal?",
    "One of the major festivals celebrated in Nepal is 'Dashain,' which is a 15-day-long Hindu festival that involves various rituals and celebrations.",
    "What's the literacy rate in Nepal?",
    "As of my last update, the literacy rate in Nepal is around 68%.",
    "Tell me a famous Nepali saying.",
    "Certainly! Here's a famous Nepali saying: 'हानी हार, बानी नपार' (pronounced as 'haani haar, baani napar'), which means 'Don't be sad about losses, but be cautious about words.'",
    "How far is Mount Everest from Kathmandu?",
    "The distance between Kathmandu and Mount Everest is approximately 125 kilometers.",
    "What's the national bird of Nepal?",
    "The national bird of Nepal is the 'Himalayan Monal,' also known as the 'Danphe' in Nepali.",
     "Can you tell me a famous historical site in Nepal?",
    "Certainly! The famous historical site in Nepal is the 'Patan Durbar Square,' a UNESCO World Heritage Site located in Kathmandu."
]

list_trainer = ListTrainer(bot)

list_trainer.train(list_of_response)

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    number = 55
    return HttpResponse(number)

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatbot_response = bot.get_response(userMessage)
    return HttpResponse(chatbot_response)

def getWeather(request):
    lat_ = str(request.GET.get('lat'))
    long_ = str(request.GET.get('long'))
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat_}&lon={long_}&appid=4233d314b515c0a89daba45270e7ae4d"
    response = requests.get(url)
    jsonResponse = response.json()
    name = jsonResponse['name']
    temp = jsonResponse['main']['temp']
    description = jsonResponse['weather'][0]['description']
    return JsonResponse(jsonResponse)

def getNews(request):
    response = requests.get("https://saurav.tech/NewsAPI/everything/cnn.json")
    jsonResponse = response.json()
    return JsonResponse(jsonResponse)