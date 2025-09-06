from nltk.chat.util import Chat, reflections

# Pattern-response pairs for the chatbot (minimal example)
pairs = [
    ['my name is (.*)', ['hi %1']],
    ['(hello|hi|hey|hola|yo)', ['hey there', 'hi there','heyyyyy']],
    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],
    ['(.*).(location|city) ?', ['Tokyo, Japan']],
    ['(.*).created you?', ['Connor Tan did, he the goat']],
    ['how is the weather in (.*)', ['the weather in %1 is amazing like always']],
    ['(.*)help(.*)', ['I can help you']],
    ['(.*)your name?',['My name is Gerard']]    
]

my_dummy_reflections = {
    'go':'gone',
    'hello':'hey there'
}
gerard = Chat(pairs,my_dummy_reflections)
gerard.converse()
