from datetime import datetime



def sample_responses(input_text):
    user_message = str(input_text).lower()
        

    if user_message in ("when moon", "moon when", "when lambo"):
        return "start shilling, type /shill to get shill groups"

    if user_message in ("who are you", "who are you?"):
        return "Im the yorkie bot"

    if user_message in ("time", "what time?"):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        return str(date_time)

    #return "I dont understand"
