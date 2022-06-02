from talon import Context, speech_system
from talon.engines.w2l import W2lEngine
from talon.engines.webspeech import WebSpeechEngine
webspeech = WebSpeechEngine()
w2l = W2lEngine(model='en_US', debug=False)

speech_system.add_engine(w2l)
speech_system.add_engine(webspeech)

ctx = Context()
ctx.settings = {
    'speech.engine': 'w2l',
}
