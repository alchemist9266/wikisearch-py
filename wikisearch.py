#Made by Leak#5749
#yes ahahaa go brrrr
#inspired by numemex
import wikipedia
import pyfiglet

#ascii yes ahahah brrr
result = pyfiglet.figlet_format("WIKI-PY", font = "banner3-D")
print(result)

print("||====================================||")
print("[+] Wikisearch-py By Leak#5749")
print("[+] Github : https://github.com/leak37")
print("||====================================||")

#input lguange yes
print('\n')
lang = input("[>] Language (Language Code. Ex. ID) : ")

search = input("[>] Search : ")
print('\n')
print("[>] Result :")
print('\n')

#langugaeg yes bro
wikipedia.set_lang(lang)

#searchgay
gay = wikipedia.summary(search, sentences = 2)
  
#print gay yes you gay lol lmao
print(gay)