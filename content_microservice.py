import json
import random
import time

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "Opportunities don't happen. You create them. - Chris Grosser",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
    "Dream big and dare to fail. - Norman Vaughan",
    "Action is the foundational key to all success. - Pablo Picasso"
]

habits = [
    "Wake up at the same time every day.",
    "Follow the two-minute rule for small tasks.",
    "Complete your most difficult task first.",
    "Block out specific times for deep work.",
    "Write a daily 'To-Done' list.",
    "Use a timer to work in 25-minute sprints.",
    "Identify only three priority tasks per day.",
    "Turn off all non-essential phone notifications.",
    "Prepare your outfit and bag the night before.",
    "Clear your email inbox daily.",
    "Take a five-minute walk every hour.",
    "Review your long-term goals every morning.",
    "Batch similar tasks together.",
    "Create a ritual to end your workday.",
    "Drink a glass of water immediately upon waking.",
    "Perform a full review of your week every Sunday.",
    "Focus on the 20% of work that drives results.",
    "Write your daily plan on physical paper.",
    "Clean your desk before leaving the office.",
    "Avoid multitasking at all costs.",
    "Wait 24 hours before making unplanned purchases.",
    "Meditate for ten minutes to improve focus.",
    "Read for thirty minutes every day.",
    "Keep a journal to track your thoughts.",
    "Pack a healthy lunch to avoid decision fatigue."
]

while True:
    with open('request.json', 'r') as file:
        request = json.load(file)

    if request['status'] == 'pending':
        request_type = request['type']

        if request_type == "quote":
            result = random.choice(quotes)
            status = "completed"
        elif request_type == "habit":
            result = random.choice(habits)
            status = "completed"
        else:
            request_type = "unknown"
            result = "Error in validating request"
            status = "error"

        response = {
            "type": request_type,
            "result": result,
            "status": status
        }

        with open('response.json', 'w') as f:
            json.dump(response, f, indent=4)

        request['status'] = "completed"
        with open('request.json', "w") as file:
            json.dump(request, file, indent=4)

    time.sleep(1)
