
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
    except sr.UnknownValueError:
        print("Could not understand your speech. Please try again.")
        return ""
    except sr.RequestError:
        print("Couldn't request results; Internet connection issue.")
        return ""
    return command

def find_recipes():
    talk("Sure! Here are a few example recipes:")
    recipes = {
        "vada pav": "To make pancakes, you'll need 1 cup all-purpose flour, 2 tablespoons granulated sugar, 2 teaspoons baking powder, 1/2 teaspoon salt, 3/4 cup milk, 2 tablespoons unsalted butter (melted), and 1 large egg.",
        "chhole bhature": "To make spaghetti bolognese, you'll need 8 ounces spaghetti, 1 tablespoon olive oil, 1 onion (finely chopped), 2 garlic cloves (minced), 1 pound ground beef, 1 can crushed tomatoes, 1 teaspoon dried oregano, salt, and pepper to taste.",
        "Biryani": "To make chicken stir-fry, you'll need 1 pound boneless, skinless chicken breasts (sliced), 2 cups broccoli florets, 1 red bell pepper (sliced), 1 cup sliced carrots, 3 tablespoons soy sauce, 2 tablespoons oyster sauce, 1 tablespoon cornstarch, and 2 tablespoons vegetable oil.",
        "Dosa" : "To make dosa u need rice batter , finely chopped onions for sambhar n stuffing",
    }

    for recipe, ingredients in recipes.items():
        talk(f"Recipe for {recipe}: {ingredients}")



def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play' , '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            talk("Multiple matches found. Please be more specific.")
        except wikipedia.exceptions.PageError:
            print("Could not find any information.")
            talk("Sorry, I couldn't find any information about that person.")
    elif 'marvel date' in command:
        talk('sorry, I have a headache')
    elif 'superman' in command:
        talk('His original name on the planet Krypton was Kal-El.Every Superman before and after the Reeve era are invariably compared to his depiction.')
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'find me recipes' in command:
        find_recipes()
    else:
        talk('Please say the command again.')


while True:
    run_alexa()