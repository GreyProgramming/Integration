from random import random

First={
1:"ing", 2:"ment", 3:"ger", 4:"light", 5:"age", 6:"er", 7:"or", 8:"low", 9:"ob", 10:"ba", 11:"a", 12:"tions", 13:"ni", 14:"of", 15:"but", 16:"ly", 17:"ble", 18:"par", 19:"pos", 20:"cit", 21:"ed", 22:"der", 23:"son", 24:"tain", 25:"cle",
26:"i", 27:"ma", 28:"tle", 29:"den", 30:"co", 31:"es", 32:"na", 33:"day", 34:"ings", 35:"cov", 36:"re", 37:"si", 38:"ny", 39:"mag", 40:"da", 41:"tion", 42:"un", 43:"pen", 44:"ments", 45:"dif", 46:"in", 47:"at", 48:"pre", 49:"set", 50:"ence",
51:"e", 52:"dis", 53:"tive", 54:"some", 55:"ern", 56:"con", 57:"ca", 58:"car", 59:"sub", 60:"eve", 61:"y", 62:"cal", 63:"ci", 64:"sur", 65:"hap", 66:"ter", 67:"man", 68:"mo", 69:"ters", 70:"ies", 71:"ex", 72:"ap", 73:"on", 74:"tu", 75:"ket",
76:"al", 77:"po", 78:"ous", 79:"af", 80:"lec", 81:"de", 82:"sion", 83:"pi", 84:"au", 85:"main", 86:"com", 87:"vi", 88:"se", 89:"cy", 90:"mar", 91:"o", 92:"el", 93:"ten", 94:"fa", 95:"mis", 96:"di", 97:"est", 98:"tor", 99:"im", 100:"my",
101:"en", 102:"la", 103:"ver", 104:"li", 105:"nal", 106:"an", 107:"lar", 108:"ber", 109:"lo", 110:"ness", 111:"ty", 112:"pa", 113:"can", 114:"men", 115:"ning", 116:"ry", 117:"ture", 118:"dy", 119:"min", 120:"n’t", 121:"u", 122:"for", 123:"et", 124:"mon", 125:"nu",
126:"ti", 127:"is", 128:"it", 129:"op", 130:"oc", 131:"ri", 132:"mer", 133:"mu", 134:"out", 135:"pres", 136:"be", 137:"pe", 138:"no", 139:"rec", 140:"sup", 141:"per", 142:"ra", 143:"ple", 144:"ro", 145:"te", 146:"to", 147:"so", 148:"cu", 149:"sen", 150:"ted",
151:"pro", 152:"ta", 153:"fac", 154:"side", 155:"tem", 156:"ac", 157:"as", 158:"fer", 159:"tal", 160:"tin", 161:"ad", 162:"col", 163:"gen", 164:"tic", 165:"tri", 166:"ar", 167:"fi", 168:"ic", 169:"ties", 170:"tro", 171:"ers", 172:"ful", 173:"land", 174:"ward", 175:"up",
176:"va", 177:"cir", 178:"tra", 179:"lead", 180:"tract", 181:"ven", 182:"cor", 183:"tures", 184:"lect", 185:"tray", 186:"vis", 187:"coun", 188:"val", 189:"lent", 190:"us", 191:"am", 192:"cus", 193:"var", 194:"less", 195:"vel", 196:"bor", 197:"dan", 198:"vid", 199:"lin", 200:"west",
201:"by", 202:"dle", 203:"wil", 204:"mal", 205:"where", 206:"cat", 207:"ef", 208:"win", 209:"mi", 210:"writ", 211:"cent", 212:"end", 213:"won", 214:"mil", 215:"ev", 216:"ent", 217:"work", 218:"moth", 219:"gan", 220:"ered", 221:"act", 222:"near", 223:"gle", 224:"fin", 225:"ag",
226:"nel", 227:"head", 228:"form", 229:"air", 230:"net", 231:"high", 232:"go", 233:"als", 234:"new", 235:"il", 236:"har", 237:"bat", 238:"one", 239:"lu", 240:"ish", 241:"bi", 242:"point", 243:"me", 244:"lands", 245:"cate", 246:"prac", 247:"nore", 248:"let", 249:"cen", 250:"ral",
251:"part", 252:"long", 253:"char", 254:"rect", 255:"por", 256:"mat", 257:"come", 258:"ried", 259:"read", 260:"meas", 261:"cul", 262:"round", 263:"rep", 264:"mem", 265:"ders", 266:"row", 267:"su", 268:"mul", 269:"east", 270:"sa", 271:"tend", 272:"ner", 273:"fect", 274:"sand", 275:"ther",
276:"play", 277:"fish", 278:"self", 279:"ton", 280:"ples", 281:"fix", 282:"sent", 283:"try", 284:"ply", 285:"gi", 286:"ship", 287:"um", 288:"port", 289:"grand", 290:"sim", 291:"uer", 292:"press", 293:"great", 294:"sions", 295:"way", 296:"sat", 297:"heav", 298:"sis", 299:"ate", 300:"sec",
301:"ho", 302:"sons", 303:"bet", 304:"ser", 305:"hunt", 306:"stand", 307:"bles", 308:"south", 309:"ion", 300:"sug", 311:"bod", 312:"sun", 313:"its", 314:"tel", 315:"cap", 316:"the", 317:"jo", 318:"tom", 319:"cial", 320:"ting", 321:"lat", 322:"tors"
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
91:"university", 92:"writing", 93:"article", 94:"department", 95:"difference", 96:"goal", 97:"news", 98:"audience", 99:"fishing", 100:"growth",
101:"income", 102:"marriage", 103:"user", 104:"combination", 105:"failure", 106:"meaning", 107:"medicine", 108:"philosophy", 109:"teacher",
110:"communication", 111:"night", 112:"chemistry", 113:"disease", 114:"disk", 115:"energy", 116:"nation", 117:"road", 118:"role", 119:"soup", 120:"advertising",
121:"location", 122:"success", 123:"addition", 124:"apartment", 125:"education", 126:"math", 127:"moment", 128:"painting", 129:"politics", 130:"attention",
131:"decision", 132:"event", 133:"property", 134:"shopping", 135:"student", 136:"wood", 137:"competition", 138:"distribution", 139:"entertainment", 140:"office",
141:"population", 142:"president", 143:"unit", 144:"category", 145:"cigarette", 146:"context", 147:"introduction", 148:"opportunity", 149:"performance", 150:"driver",
151:"flight", 152:"length", 153:"magazine", 154:"newspaper", 155:"relationship", 156:"teaching", 157:"cell", 158:"dealer", 159:"finding", 160:"lake",
161:"member", 162:"message", 163:"phone", 164:"scene", 165:"appearance", 166:"association", 167:"concept", 168:"customer", 169:"death", 170:"discussion",
171:"housing", 172:"inflation", 173:"insurance", 174:"mood", 175:"woman", 176:"advice", 177:"blood", 178:"effort", 179:"expression", 180:"importance",
181:"opinion", 182:"payment", 183:"reality", 184:"responsibility", 185:"situation", 186:"skill", 187:"statement", 188:"wealth", 189:"application",
190:"city", 191:"county", 192:"depth", 193:"estate", 194:"foundation", 195:"grandmother", 196:"heart", 197:"perspective", 198:"photo", 199:"recipe", 200:"studio",
201:"topic", 202:"collection", 203:"depression", 204:"imagination", 205:"passion", 206:"percentage", 207:"resource", 208:"setting", 209:"ad", 210:"agency",
211:"college", 212:"connection", 213:"criticism", 214:"debt", 215:"description", 216:"memory", 217:"patience", 218:"secretary", 219:"solution", 220:"administration",
221:"aspect", 222:"attitude", 223:"director", 224:"personality", 225:"psychology", 226:"recommendation", 227:"response", 228:"selection", 229:"storage", 230:"version",
231:"alcohol", 232:"argument", 233:"complaint", 234:"contract", 235:"emphasis", 236:"highway", 237:"loss", 238:"membership", 239:"possession", 240:"preparation",
241:"steak", 242:"union", 243:"agreement", 244:"cancer", 245:"currency", 246:"employment", 247:"engineering", 248:"entry", 249:"interaction", 250:"mixture",
251:"preference", 252:"region", 253:"republic", 254:"tradition", 255:"virus", 256:"actor", 257:"classroom", 258:"delivery", 259:"device", 260:"difficulty",
261:"drama", 262:"election", 263:"engine", 264:"football", 265:"guidance", 266:"hotel", 267:"owner", 268:"priority", 269:"protection", 270:"suggestion",
271:"tension", 272:"variation", 273:"anxiety", 274:"atmosphere", 275:"awareness", 276:"bath", 277:"bread", 278:"candidate", 279:"climate", 280:"comparison",
281:"confusion", 282:"construction", 283:"elevator", 284:"emotion", 285:"employee", 286:"employer", 287:"guest", 288:"height", 289:"leadership", 290:"mall",
291:"manager", 292:"operation", 293:"recording", 294:"sample", 295:"transportation", 296:"charity", 297:"cousin", 298:"disaster", 299:"editor", 300:"efficiency",
301:"excitement", 302:"extent", 303:"feedback", 304:"guitar", 305:"homework", 306:"leader", 307:"mom", 308:"outcome", 309:"permission", 310:"presentation",
311:"promotion", 312:"reflection", 313:"refrigerator", 314:"resolution", 315:"revenue", 316:"session", 317:"singer", 318:"tennis", 319:"basket", 320:"bonus",
321:"cabinet", 322:"childhood", 323:"church", 324:"clothes", 325:"coffee", 326:"dinner", 327:"drawing", 328:"hair", 329:"hearing", 330:"initiative",
331:"judgment", 332:"lab", 333:"measurement", 334:"mode", 335:"mud", 336:"orange", 337:"poetry", 338:"police", 339:"possibility", 340:"procedure",
341:"queen", 342:"ratio", 343:"relation", 344:"restaurant", 345:"satisfaction", 346:"sector", 347:"signature", 348:"significance", 349:"song", 350:"tooth",
351:"town", 352:"vehicle", 353:"volume", 354:"wife", 355:"accident", 356:"airport", 357:"appointment", 358:"arrival", 359:"assumption", 360:"baseball",
361:"chapter", 362:"committee", 363:"conversation", 364:"database", 365:"enthusiasm", 366:"error", 367:"explanation", 368:"farmer", 369:"gate", 370:"girl",
371:"hall", 372:"historian", 373:"hospital", 374:"injury", 375:"instruction", 376:"maintenance", 377:"manufacturer", 378:"meal", 379:"perception", 380:"pie",
381:"poem", 382:"presence", 383:"proposal", 384:"reception", 385:"replacement", 386:"revolution", 387:"river", 388:"son", 389:"speech", 390:"tea",
391:"village", 392:"warning", 393:"winner", 394:"worker", 395:"writer", 396:"assistance", 397:"breath", 398:"buyer", 399:"chest", 400:"chocolate",
401:"conclusion", 402:"contribution", 403:"cookie", 404:"courage", 405:"dad", 406:"desk", 407:"drawer", 408:"establishment", 409:"examination", 410:"garbage",
411:"grocery", 412:"honey", 413:"impression", 414:"improvement", 415:"independence", 416:"insect", 417:"inspection", 418:"inspector", 419:"king", 420:"ladder",
421:"menu", 422:"penalty", 423:"piano", 424:"potato", 425:"profession", 426:"professor", 427:"quantity", 428:"reaction", 429:"requirement", 430:"salad",
431:"sister", 432:"supermarket", 433:"tongue", 434:"weakness", 435:"wedding", 436:"affair", 437:"ambition", 438:"analyst", 439:"apple", 440:"assignment",
441:"assistant", 442:"bathroom", 443:"bedroom", 444:"beer", 445:"birthday", 446:"celebration", 447:"championship", 448:"cheek", 449:"client", 450:"consequence",
451:"departure", 452:"diamond", 453:"dirt", 454:"ear", 455:"fortune", 456:"friendship", 457:"funeral", 458:"gene", 459:"girlfriend", 460:"hat",
461:"indication", 462:"intention", 463:"lady", 464:"midnight", 465:"negotiation", 466:"obligation", 467:"passenger", 468:"pizza", 469:"platform", 470:"poet",
471:"pollution", 472:"recognition", 473:"reputation", 474:"shirt", 475:"sir", 476:"speaker", 477:"stranger", 478:"surgery", 479:"sympathy", 480:"tale",
481:"throat", 482:"trainer", 483:"uncle", 484:"youth", 485:"time", 486:"work", 487:"film", 488:"water", 489:"money", 490:"example",
491:"while", 492:"business", 493:"study", 494:"game", 495:"life", 496:"form", 497:"air", 498:"day", 499:"place", 500:"number"
}



def CharNameFirst():
	Char_First=""
	for i in range(3):
		char1=random.choice(list(First.keys()))
		Char_First.append(char1)
	return Char_First

def CharNameLast():
	Char_Last=""
	for i in range(2):
		char2=random.choice(list(Last.keys()))
		Char_Last.append(char2)
        return Char_Last
