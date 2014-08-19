# coding: utf8

from __future__ import unicode_literals, print_function
import os, sys, re,codecs
from hazm import *#an other project that I use some of it's parts here
from nltk.tokenize.punkt import PunktSentenceTokenizer,PunktTrainer





def sents1():
	try:
		learningsents=[]
		i=0
		for sent in PeykareReader("/home/mebrahimi/Karamoozi/hazm/corpora/peykare").sents():#this generator returns list of words and their tags in tuples for one sentence every time
			tempsent=""
			for x in [word[0] for word in sent]:
				tempsent+=x
				tempsent+=" "
			learningsents.append(tempsent)
			i+=1
			if i==14999:
				break
		return learningsents
	except Exception as b:
		print (b)

def text():
	learningtext=''
	for sent in sents1():
		learningtext+=sent
	return learningtext

trainer=PunktTrainer()

trainer.ABBREV=0.3
trainer.ABBREV_BACKOFF=5
trainer.COLLOCATION=7.88
trainer.IGNORE_ABBREV_PENALTY=True
trainer.INCLUDE_ABBREV_COLLOCS=True
trainer.INCLUDE_ALL_COLLOCS=True
trainer.MIN_COLLOC_FREQ=1
trainer.SENT_STARTER=30

s=sents1()
trainer.train_tokens(s)
f=trainer.get_params()
tokenizer=PunktSentenceTokenizer(trainer.get_params())
b=tokenizer._lang_vars
a=tokenizer.tokenize("مواد گفته شده را خرد کنید و نمک بزنید و بگذارید بماند.در ظرف دیگر مقداری آب و آب‌لیمو و روغن زیتون را در قدری نان سفید بیات یا نان بربری بریزید. این مخلوط باید در هم ترید شود.سالادرا هم بزنید تا آب بیندازد. آبش را نیز در نان‌ها خالی کنید، وقتی نان‌ها کاملاً نرم شد آن را در ظرفسالادریخته هم می‌زنید و ترشی و نمک آن را با سرکه و نمک و فلفل اندازه می‌کنید.بعد از این مرحله همه را در میکسر ریخته کاملاً هم می‌زنید تا به شکل سوپ دربیاید.اگر به اندازه یک سوپ رقیق نبود مقداری آب گوجه فرنگی نیز به آن اضافه می‌کنید. سپس روی آن کمی روغن زیتون ریخته آن را در یخچال می‌گذارید تا مزه دار شود.بعد از خنک شدن کمی خرده خیار و فلفل ریز و جعفری و ریحان ساطوری شده روی آن می‌ریزید و حالا برای خوردن آماده است.این سوپ حرارت شما را فرو می‌نشاند و خاصیتی شبیه ماست و خیار خودمان دارد. سبزیجات خام به کار رفته در آن تماماً تازه و نپخته است وترکیبات آن بسته به ذائقه شما می‌تواند کم و زیاد شود. مثلاً ممکن است دوست داشته باشید روی آن ذرات گردوی خیس خورده بریزید یا آن را با کنجد تزیین کنید.")
2+3


