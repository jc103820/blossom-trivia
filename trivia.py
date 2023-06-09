import requests

ascii_art = "\n ██████╗██╗     ██╗   ████████╗██████╗ ██╗██╗   ██╗██╗ █████╗ \n██╔════╝██║     ██║   ╚══██╔══╝██╔══██╗██║██║   ██║██║██╔══██╗\n██║     ██║     ██║█████╗██║   ██████╔╝██║██║   ██║██║███████║\n██║     ██║     ██║╚════╝██║   ██╔══██╗██║╚██╗ ██╔╝██║██╔══██║\n╚██████╗███████╗██║      ██║   ██║  ██║██║ ╚████╔╝ ██║██║  ██║\n ╚═════╝╚══════╝╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝"
total_points = 0
category_options = {
    "general_knowledge":True,
    "sport_and_leisure":False,
    "society_and_culture":False,
    "science":False,
    "music":False,
    "history":False,
    "geography":False,
    "food_and_drink":False,
    "film_and_tv":False,
    "arts_and_literature":False
}
difficulty_options = {
    "easy":False,
    "medium":False,
    "hard":False,
    "any":True
}
limit_max = 20

params = {
	"categories": ["General Knowledge"],
	"difficulty": "any",
	"limit": 1,
	"region": "US"
}
def updateparams():
	params["categories"] = []
	for category in category_options:
		if category_options[category]:
			params["categories"].append(category)
	for difficulty in difficulty_options:
		if difficulty_options[difficulty]:
			params["difficulty"]= difficulty
def getquestions(params):
	updateparams()
	url = "https://the-trivia-api.com/api/questions?"
	if len(params["categories"]) != 0:
		url += "categories=" 
		for i in params["categories"]:
			url += "{},".format(i) 
		url += "&"
	if params["difficulty"]:
		url += "difficulty={}&".format(params["difficulty"])
	if params["limit"] <= 20 and params["limit"] > 0:
		url += "limit={}&".format(params["limit"])
	if params["region"]:
		url += "region={}&".format(params["region"])
	print(url)
	res = requests.get(url)
	return res.json()
def getquestions(params):
	updateparams()
	url = "https://the-trivia-api.com/api/questions?"
	if "categories" in params and len(params["categories"]) != 0:
		url += "categories=" 
		for i in params["categories"]:
			url += "{},".format(i) 
		url += "&"
	if "difficulty" in params and params["difficulty"] != "any":
		url += "difficulty={}&".format(params["difficulty"])
	if "limit" in params and params["limit"] <= 20 and params["limit"] > 0:
		url += "limit={}&".format(params["limit"])
	if "region" in params:
		url += "region={}&".format(params["region"])
	res = requests.get(url)
	return res.json()
# https://the-trivia-api.com/api/questions

def difficulty_menu():
    for difficulty in difficulty_options:
        if(difficulty_options[difficulty]):
            print("[+] {}".format(difficulty))
        else:
            print("[+] {}".format(difficulty))

def categories_menu():
    for category in category_options:
        if(category_options[category]):
            print("\t[+] {}".format(category))
        else:
            print("\t[-] {}".format(category))
    user_input = input('Enter the name of a category to add or remove it or Q to quit: ')
    if(user_input.lower() == 'q'):
        return
    elif(user_input in category_options):
        print('preferences updated.')
        category_options[user_input] = not category_options[user_input]
        categories_menu()
    else:
        user_input = input('Enter the name of a category to add or remove it: ')

def menu():
    print('Menu:')
    print('\tEnter C to change your category options.')
    print('\tEnter D to change your difficulty.')
    print('\tEnter Q to quit the menu')
    print('\nPoints [', total_points, ']\n')
    user_input = input('Choice: ')
    if(user_input.lower() == 'c'):
        categories_menu()
        return
    elif(user_input.lower() == 'd'):
        difficulty_menu()
        return
    elif(user_input.lower() == 'q'):
        exit(0)

def questionloop():
	# repeatedly ask questions.
	while True:
		menu()
		questions = getquestions(params)
		for question in questions:
			ask(question)

def ask(question):
	print(question)
print(ascii_art)
questionloop()
         