while True:
    meme_dict = {
                "CRINGE": "Algo vergonhoso ou constrangedor",
                "STALKEAR": "Investigar a vida de alguém online",
                "killstreak": "sequência de mortes/vitórias"
                "Dropar": "verbo: largar, soltar, deixar"
                "Juro": "expressão muito empregada por garotas de modo que demonstre concordância"
                "Speedrun":"fazer algo rápido (referênccia aos speedruners)"
                "Skillar":"usar habilidade, do inglês, Skill"
                "Cosplay":"se vestir de um personagem"
                "Cosplayer":"quem se veste de um personagem/ faz cosplay"
                "Hater": "odiar algo/alguém, do inglês hate"
                "Spammar":"spam/ usar a mesma habilidade muitas vezes"
                "Aura":"energia espiiritual"
                "Ego":"parte consciente do pensamento ao lado do Id (pulsões e desejos) e do Superego (moral e normas)."
                }
    
    palavra = input('Escreva uma palavra que você não entende em letras maiúsculas')
    
    if palavra in meme_dict.keys():
        print(meme_dict[palavra])
        break
    else:
        print('não tem essa palavra no dicionário :(')
