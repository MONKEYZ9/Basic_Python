# 구글 번역을 불러와서 하는 거야
from googletrans import Translator

translator = Translator()

# sentence = '안녕하세요, 이상민입니다.'
sentence = input()

strlang = 'en'

detected = translator.detect(sentence)
result = translator.translate(sentence,strlang)

print(detected.lang)
print(result.text)
# print(translated.pronunciation)
# print(translated.dest)


mli = {'한국어': 'ko', '프랑스어':'fr', '베트남어':'vi', '스페인어':'es', '중국어':'zh-CN', '힌디어':'hi', '몽골어':'mn', '독일어':'de', '아랍어':'ar'}

for lang in mli:
    result = translator.translate(sentence,mli[lang])
    print(detected.lang, " : ", sentence)
    print(result.dest, ' : ', result.text)