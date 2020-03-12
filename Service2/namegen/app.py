from flask import Flask, request
from random import choice

app = Flask(__name__)

First={
1:"ing", 2:"ment", 3:"ger", 4:"light", 5:"age", 6:"er", 7:"or", 8:"low", 9:"ob", 10:"ba", 11:"a", 12:"tions", 13:"ni", 14:"of", 15:"but", 16:"ly", 17:"ble", 18:"par", 19:"pos", 20:"cit", 21:"ed", 22:"der", 23:"son", 24:"tain", 25:"cle",
26:"i", 27:"ma", 28:"tle", 29:"den", 30:"co", 31:"es", 32:"na", 33:"day", 34:"ings", 35:"cov", 36:"re", 37:"si", 38:"ny", 39:"mag", 40:"da", 41:"tion", 42:"un", 43:"pen", 44:"ments", 45:"dif", 46:"in", 47:"at", 48:"pre", 49:"set", 50:"ence",
51:"e", 52:"dis", 53:"tive", 54:"some", 55:"ern", 56:"con", 57:"ca", 58:"car", 59:"sub", 60:"eve", 61:"y", 62:"cal", 63:"ci", 64:"sur", 65:"hap", 66:"ter", 67:"man", 68:"mo", 69:"ters", 70:"ies", 71:"ex", 72:"ap", 73:"on", 74:"tu", 75:"ket",
76:"al", 77:"po", 78:"ous", 79:"af", 80:"lec", 81:"de", 82:"sion", 83:"pi", 84:"au", 85:"main", 86:"com", 87:"vi", 88:"se", 89:"cy", 90:"mar", 91:"o", 92:"el", 93:"ten", 94:"fa", 95:"mis", 96:"di", 97:"est", 98:"tor", 99:"im", 100:"my"
}

Last={
1:"people", 2:"history", 3:"way", 4:"art", 5:"world", 6:"information", 7:"map", 8:"two", 9:"family", 10:"government",
11:"health", 12:"system", 13:"computer", 14:"meat", 15:"year", 16:"thanks", 17:"music", 18:"person", 19:"reading", 20:"method",
21:"data", 22:"food", 23:"understanding", 24:"theory", 25:"law", 26:"bird", 27:"literature", 28:"problem", 29:"software", 30:"control",
31:"knowledge", 32:"power", 33:"ability", 34:"economics", 35:"love", 36:"internet", 37:"television", 38:"science", 39:"library", 40:"nature",
41:"fact", 42:"product", 43:"idea", 44:"temperature", 45:"investment", 46:"area", 47:"society", 48:"activity", 49:"story", 50:"industry",
51:"media", 52:"thing", 53:"oven", 54:"community", 55:"definition", 56:"safety", 57:"quality", 58:"development", 59:"language", 60:"management",
61:"player", 62:"variety", 63:"video", 64:"week", 65:"security", 66:"country", 67:"exam", 68:"movie", 69:"organization", 70:"equipment",
71:"physics", 72:"analysis", 73:"policy", 74:"series", 75:"thought", 76:"basis", 77:"boyfriend", 78:"direction", 79:"strategy", 80:"technology",
81:"army", 82:"camera", 83:"freedom", 84:"paper", 85:"environment", 86:"child", 87:"instance", 88:"month", 89:"truth", 90:"marketing",
91:"university", 92:"writing", 93:"article", 94:"department", 95:"difference", 96:"goal", 97:"news", 98:"audience", 99:"fishing", 100:"growth"
}

def CharNameFirst():
	Char_First=""
	for i in range(3):
		char1=choice(First)
		Char_First=Char_First+char1
	return Char_First

def CharNameLast():
	Char_Last=""
	for i in range(2):
		char2=choice(Last)
		Char_Last=Char_Last+char2
	return Char_Last

@app.route('/')
def random_name():
	first_name=CharNameFirst()
	last_name=CharNameLast()
	return str(first_name+" "+last_name)

if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')
