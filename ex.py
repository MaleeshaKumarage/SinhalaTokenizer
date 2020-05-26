from sinling import SinhalaTokenizer

tokenizer = SinhalaTokenizer()

sentence = 'සාමාන්‍යයෙන් ආගම ප්‍රශ්නයකට පිළිතුරක් විය යුතු නමුත් ශ්‍රී ලංකාවේ ආගම ප්‍රශ්නයක් වී තිබේ. එසේ නම් පිළිතුර කුමක් විය හැකිද? මිනිස් ඉතිහාසය පුරා දේශපාලන අවියක් ලෙස ජනතාව මර්දනය කිරීමට ආගම යොදාගෙන තිබේ. මධ්‍යතන යුගයේ ද ඊට පසුව ද ආගම නාමයෙන් නොයෙකුත් යුද්ධ ඇතිවී තිබේ. රටක ආගම ප්‍රශ්නයක් වූ විට එරට ආගමික නායකයන්ද ඇතුළු එරට වගකිව යුතු පුරවැසියන් විසින් එයට විසඳුමක් සොයා ගත යුතුය. '  # your sentence
print(sentence);
s=tokenizer.tokenize(sentence)

with open ('tokenizedText.txt', 'w', encoding="utf-8") as f:
    f.writelines(str(s))
    
    print(s);
f.close() 
#========================================

from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
s0 = "සාමාන්‍යයෙන් ආගම ප්‍රශ්නයකට පිළිතුරක් විය යුතු නමුත් ශ්‍රී ලංකාවේ ආගම ප්‍රශ්නයක් වී තිබේ. එසේ නම් පිළිතුර කුමක් විය හැකිද? මිනිස් ඉතිහාසය පුරා දේශපාලන අවියක් ලෙස ජනතාව මර්දනය කිරීමට ආගම යොදාගෙන තිබේ. මධ්‍යතන යුගයේ ද ඊට පසුව ද ආගම නාමයෙන් නොයෙකුත් යුද්ධ ඇතිවී තිබේ. රටක ආගම ප්‍රශ්නයක් වූ විට එරට ආගමික නායකයන්ද ඇතුළු එරට වගකිව යුතු පුරවැසියන් විසින් එයට විසඳුමක් සොයා ගත යුතුය."
s1=tknzr.tokenize(s0)
with open ('tokenizedText.txt', 'a', encoding="utf-8") as f:
    f.writelines(str("\n"))
    f.writelines(str(s1))
#print(s1);