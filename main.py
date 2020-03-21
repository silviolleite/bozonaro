import markovify
from twitter_scraper import get_tweets


def imprima_frase(text):
    print("\n {1} \n {0} \n {1}".format(text, 140 * "*"))


if __name__ == "__main__":
    texts = []
    print("Buscando tweets relacionados ao Bolsonaro, aguarde...")
    for t in get_tweets("jairbolsonaro"):
        texts.append(t["text"])

    text_model = markovify.Text(texts)
    print("Frase gerada geradas através de Cadeias de Markov")

    imprima_frase(text_model.make_short_sentence(140))
