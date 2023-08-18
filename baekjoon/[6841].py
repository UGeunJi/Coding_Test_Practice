short = ["CU", ":-)", ":-(", ";-)", ":-P", "(~.~)", "TA", "CCC", "CUZ", "TY", "YW", "TTYL"]
trans = ["see you", "I’m happy", "I’m unhappy", "wink", "stick out my tongue", "sleepy", "totally awesome", "Canadian Computing Competition", "because", "thank-you", "you’re welcome", "talk to you later"]

while True:
    text = input()
    
    if text in short: 
        print(trans[short.index(text)])
    else: 
        print(text)
    
    if text == "TTYL":
        break
