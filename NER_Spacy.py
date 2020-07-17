import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from bs4 import BeautifulSoup
import requests
import re


doc= nlp('Peter Strzok, the F.B.I. senior counterintelligence agent who disparaged President Trump in inflammatory text messages and helped oversee the Hillary Clinton email and Russia investigations, has been fired for violating bureau policies, Mr. Strzok’s lawyer said Monday.Mr. Trump and his allies seized on the texts — exchanged during the 2016 campaign with a former F.B.I. lawyer, Lisa Page — in assailing the Russia investigation as an illegitimate “witch hunt.” Mr. Strzok, who rose over 20 years at the F.B.I. to become one of its most experienced counterintelligence agents, was a key figure in the early months of the inquiry.Along with writing the texts, Mr. Strzok was accused of sending a highly sensitive search warrant to his personal email account. \
         The F.B.I. had been under immense political pressure by Mr. Trump to dismiss Mr. Strzok, who was removed last summer from the staff of the special counsel, Robert S. Mueller III. The president has repeatedly denounced Mr. Strzok in posts on Twitter, and on Monday expressed satisfaction that he had been sacked. \
         Mr. Trump’s victory traces back to June, when Mr. Strzok’s conduct was laid out in a wide-ranging inspector general’s report on how the F.B.I. handled the investigation of Hillary Clinton’s emails in the run-up to the 2016 election. The report was critical of Mr. Strzok’s conduct in sending the texts, and the bureau’s Office of Professional Responsibility said that Mr. Strzok should be suspended for 60 days and demoted. Mr. Strzok had testified before the House in July about how he had not allowed his political views to interfere with the investigations he was overseeing. \
         But Mr. Strzok’s lawyer said the deputy director of the F.B.I., David Bowdich, had overruled the Office of Professional Responsibility and fired Mr. Strzok. \
         A spokeswoman for the F.B.I. did not respond to a message seeking comment about why Mr. Strzok was dismissed rather than demoted. Firing Mr. Strzok, however, removes a favorite target of Mr. Trump from the ranks of the F.B.I. and gives Mr. Bowdich and the F.B.I. director, Christopher A. Wray, a chance to move beyond the president’s ire. \
         Aitan Goelman, Mr. Strzok’s lawyer, denounced his client’s dismissal. “The decision to fire Special Agent Strzok is not only a departure from typical bureau practice, but also contradicts Director Wray’s testimony to Congress and his assurances that the F.B.I. intended to follow its regular process in this and all personnel matters,” Mr. Goelman said. \
         “This decision should be deeply troubling to all Americans,” Mr. Goelman added. “A lengthy investigation and multiple rounds of congressional testimony failed to produce a shred of evidence that Special Agent Strzok’s personal views ever affected his work.”')

for x in doc.ents:
    print([(x.text, x.label_)])
    
for info in doc:
    print(info, info.ent_iob_, info.ent_type_)


'''   
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))

'''

#ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')


len(doc.ents)
labels = [x.label_ for x in doc.ents]
Counter(labels)

items = [x.text for x in doc.ents]
Counter(items).most_common(3)
sentences = [x for x in doc.sents]
print(sentences[10])
displacy.render(nlp(str(sentences[10])), style = 'ent')

[(x.orth_,x.pos_, x.lemma_) for x in [y 
                                      for y
                                      in nlp(str(sentences[10])) 
                                      if not y.is_stop and y.pos_ != 'PUNCT']]

print([(x, x.ent_iob_, x.ent_type_) for x in sentences[2]])
