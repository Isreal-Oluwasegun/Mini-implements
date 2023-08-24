import langdetect
from translate import Translator
print(langdetect.detect("Bonjour"))
translator= Translator(from_lan="French", to_lang="English")
translation = translator.translate("Bonjour")
print(translation)