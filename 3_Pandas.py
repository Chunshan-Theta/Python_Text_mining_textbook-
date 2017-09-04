import pandas as pd

source_sentences = ["Monday: The doctor's appointment is at 2:45pm.",
"Tuesday: The dentist's appointment is at 11:30 am.",
"Wednesday: At 7:00pm, there is a basketball game!",
"Thursday: Be back home by 11:15 pm at the latest.",
"Firiday: Take the train at 08:00 am, arrive at 09:00am."]

df = pd.DataFrame(source_sentences, columns=['text'])

print(df['text'])
print(df['text'].str.len())
print(df['text'].str.contains("appointment"))
print(df['text'].str.count('\d'))
print(df['text'].str.findall('\d'))
print(df['text'].str.findall('(\d)'))
print(df['text'].str.findall('(\d\d?):(\d\d)'))
print(df['text'].str.replace('(\w+day)','???'))

print(df['text'].str.extract('((\d?\d):(\d\d? ?)([ap]m))'))
print(df['text'].str.extractall('((\d?\d):(\d\d? ?)([ap]m))'))
print(df['text'].str.extractall('(?P<Time>(?P<Hour>\d?\d):(?P<minute>\d\d? ?)(?P<period>[ap]m))'))
