r"""°°°
# Grundlagen des maschinellen Lernens
## Python Tutorial - Teil 1
°°°"""
# |%%--%%| <thULIud0KJ|05M8IGJMBO>
r"""°°°
### Markdown-Zellen

Jupyter Zellen können Python Code oder auch Markdown Code enthalten. Der Modus kann in der Menüleiste geändert werden. Mit Hilfe von Markdown (z.B. http://markdown.de/) kann u.a. die Dokumentation des Notebooks erstellt werden.
°°°"""
# |%%--%%| <05M8IGJMBO|vfNZmFzA8q>
r"""°°°
Falls gewünscht, können mathematische Formeln u.ä. auch in LaTex zwischen zwei `$`-Zeichen gesetzt werden. Beispiele:
- $0.5 = \frac{1}{2}$
- $b = \sqrt{(\frac{7}{8})^3}$
°°°"""
# |%%--%%| <vfNZmFzA8q|VqQVvZbxO0>
r"""°°°
Auch die doppelten `$$`-Zeichen funktionieren:

$$ \sum_{i=1}^n i = \frac{n(n+1)}{2} $$
°°°"""
# |%%--%%| <VqQVvZbxO0|dZiq9k6Yi8>
r"""°°°
### Kommentare
°°°"""
# |%%--%%| <dZiq9k6Yi8|j6PkrjohEj>

# Einzeiliger Kommentar

# |%%--%%| <j6PkrjohEj|nmnTEVkO6C>

'''
Mehrzeiliger Kommentar
'''

# |%%--%%| <nmnTEVkO6C|M88AoyFZ0P>
r"""°°°
### Mathematische Operatoren
°°°"""
# |%%--%%| <M88AoyFZ0P|urwHQ5Twb6>

1 + 2

# |%%--%%| <urwHQ5Twb6|gvz9ehkhor>

3 - 4

# |%%--%%| <gvz9ehkhor|Ua48iC1E0U>

7 * 6

# |%%--%%| <Ua48iC1E0U|2aaDkwx0rK>

# Python 3 spezifisch wird hier Gleitkommaarithemtik verwendet
45 / 7

# |%%--%%| <2aaDkwx0rK|wGoX4KMWA5>

8 ** 2

# |%%--%%| <wGoX4KMWA5|ntv1NsPMBN>
r"""°°°
### Variablen und Datentypen
In Python müssen Variablen nicht extra deklariert werden. Sobald ein neuer Bezeichner mit einem Wert belegt wird existiert die Variable. Obwohl Python Datentypen kennt, können bestehende Variablen auch direkt mit einem Wert eines anderen Datentyps belegt werden.
°°°"""
# |%%--%%| <ntv1NsPMBN|ztvjGPOmJw>

x = 9

# |%%--%%| <ztvjGPOmJw|Xex64RGxN6>

x

# |%%--%%| <Xex64RGxN6|2N8vTFa433>

type(x)

# |%%--%%| <2N8vTFa433|BjClcXViri>

type(6.2)

# |%%--%%| <BjClcXViri|7ttJTQW1Rj>

x = 'Diesmal ein String'
type(x)

# |%%--%%| <7ttJTQW1Rj|RRTPrGp6Rs>
r"""°°°
### `print`
°°°"""
# |%%--%%| <RRTPrGp6Rs|Hhw9hlzsWr>

print(1 + 2 * 3)

# |%%--%%| <Hhw9hlzsWr|lK3FJqUYxq>

print(x)

# |%%--%%| <lK3FJqUYxq|XMYEgmolaa>

# Zeichenkette mit Formatierung ausgeben
print('Die Zahl {} ist {}.'.format(4, 'gerade'))

# |%%--%%| <XMYEgmolaa|b9Kpyld05X>

# Beschränkung der Anzahl der gedruckten Nachkommastellen
print('{:.4f}'.format(2.7812423))

# |%%--%%| <b9Kpyld05X|Ys7QQ8WAqi>
r"""°°°
### Datentypen

Python kennt die primitiven Datentypen
- Boolean
- Integer
- Float
- String
°°°"""
# |%%--%%| <Ys7QQ8WAqi|N6wpwLCZkF>
r"""°°°
#### Boolean
°°°"""
# |%%--%%| <N6wpwLCZkF|KLAvoL0yT7>

type(True)

# |%%--%%| <KLAvoL0yT7|vKwbbj6sBB>

type(False)

# |%%--%%| <vKwbbj6sBB|cE4bKSW2jH>
r"""°°°
#### Integer
°°°"""
# |%%--%%| <cE4bKSW2jH|yxMwT5bmLt>

type(55)

# |%%--%%| <yxMwT5bmLt|uluz5sYPWj>
r"""°°°
#### Float
°°°"""
# |%%--%%| <uluz5sYPWj|QP9q7BDtPZ>

type(4.12344)

# |%%--%%| <QP9q7BDtPZ|u3G1E6clDf>

1.2345e-2

# |%%--%%| <u3G1E6clDf|ppwbfNxWIQ>
r"""°°°
#### Strings
°°°"""
# |%%--%%| <ppwbfNxWIQ|8jojUFoqT5>

a = 'Ein String'
type(a)

# |%%--%%| <8jojUFoqT5|A7nhxTOBmW>

b = "Ein anderer String"
type(b)

# |%%--%%| <A7nhxTOBmW|MZ3CbUDQ8J>
r"""°°°
### Listen
°°°"""
# |%%--%%| <MZ3CbUDQ8J|VbzZDf95D7>

# Liste
l = [1, 2, 3, 4, 5, 6]
type(l)

# |%%--%%| <VbzZDf95D7|aVMrNdoHvq>

len(l)

# |%%--%%| <aVMrNdoHvq|TAJFU0pIpp>

l.append(7)
l

# |%%--%%| <TAJFU0pIpp|UzxgnrL4Z6>

l.append('WOW')
l

# |%%--%%| <UzxgnrL4Z6|VilzyREQm3>

l[7]

# |%%--%%| <VilzyREQm3|xaa9w8G7GL>
r"""°°°
### Tupel
Tupel sind ähnlich wie Listen aber unveränderlich (Werte können nicht verändert werden und ein Tupel kann auch nicht vergrößert werden)
°°°"""
# |%%--%%| <xaa9w8G7GL|H48bMzSDw3>

t = (1.0, 2.0)
type(t)

# |%%--%%| <H48bMzSDw3|eM4ucdcMZI>

u = ('string', 3.1)
type(u)

# |%%--%%| <eM4ucdcMZI|jb8mJgSUk7>

u[0]

# |%%--%%| <jb8mJgSUk7|43nGhTDR9L>

u[1]

# |%%--%%| <43nGhTDR9L|S7mb5GuWON>
r"""°°°
### Dictionaries
Dictionaries repräsentieren Zuordnungtabellen, d.h. es werden Schlüssel (keys) aus Werte (values) abgebildet. Ein Beispiel aus der realen Welt sind Telefonbücher.
°°°"""
# |%%--%%| <S7mb5GuWON|0IKitLmENv>

tel = {'Anna': '555-1234', 'Bob': '555-5432'}
type(tel)

# |%%--%%| <0IKitLmENv|9F3zrUlnAb>

tel['Anna']

# |%%--%%| <9F3zrUlnAb|zoTeV3sfJi>

tel.keys()

# |%%--%%| <zoTeV3sfJi|9GPchGhRxA>

tel.values()

# |%%--%%| <9GPchGhRxA|hbd8mPZxGr>

tel['Charlie'] = '555-9999'

# |%%--%%| <hbd8mPZxGr|kpcJPCnALz>

tel.values()

# |%%--%%| <kpcJPCnALz|Nm1gjNz3OJ>

tel['Charlie']

# |%%--%%| <Nm1gjNz3OJ|9QgoIP8WqH>
r"""°°°
### import

Mit Hilfe von `import` werden Bibliotheken geladen.
°°°"""
# |%%--%%| <9QgoIP8WqH|K6dIWTJzG3>

import math 
math.ceil(1.23456)

# |%%--%%| <K6dIWTJzG3|0HSptPxZDb>

from math import *
# jetzt muss math nicht mehr davor geschrieben werden
ceil(1.23456)

# |%%--%%| <0HSptPxZDb|GYanOmxkB1>

# es können auch nur Teile einer Bibliothek geladen werden und unter einem frei definierbaren Namen verwendet werden
%matplotlib inline
from matplotlib import pyplot as plt

plt.plot([1,2,3,2,4,6])

# |%%--%%| <GYanOmxkB1|qbXW3tu7dm>
r"""°°°
### Logik
°°°"""
# |%%--%%| <qbXW3tu7dm|zlhz12ypYO>

a = True
b = False

# |%%--%%| <zlhz12ypYO|MgcAV5ElvW>

a and b

# |%%--%%| <MgcAV5ElvW|9sfgXAD4IG>

a or b

# |%%--%%| <9sfgXAD4IG|13vDv7369z>

not a

# |%%--%%| <13vDv7369z|a3VZphOzGg>

# wenn es komplizierter wird besser Klammern setzen
((a and b) or ((not a) and (not b)))

# |%%--%%| <a3VZphOzGg|ekdnHBz7L4>

3.4 >= 4.5

# |%%--%%| <ekdnHBz7L4|JPaM0RJBhI>

9 in [1, 4, 9, 16]

# |%%--%%| <JPaM0RJBhI|z7UFArrUwx>

'Emil' not in ['Adam', 'Berta', 'Carl', 'Dora']

# |%%--%%| <z7UFArrUwx|TMeWm65T2A>
r"""°°°
### String Operationen
°°°"""
# |%%--%%| <TMeWm65T2A|xITwLjSu9A>

'Eins ' + "Zwei"

# |%%--%%| <xITwLjSu9A|oFfupugbfV>

len('Kurzwort')

# |%%--%%| <oFfupugbfV|vOdqGyIkFj>

'Kurzwort'.lower()

# |%%--%%| <vOdqGyIkFj|BOlF7d01AE>

'Kurzwort'.upper()

# |%%--%%| <BOlF7d01AE|cMHWt7ptmb>

'Kurzwort'.startswith('Kurz')

# |%%--%%| <cMHWt7ptmb|9CdgQWqGCs>

'Kurzwort'.endswith('wort')

# |%%--%%| <9CdgQWqGCs|OokVMBxBHV>

text = 'Drunt in der greana Au stehd a Biarnbaam schee blau - juche!'
text.split()

# |%%--%%| <OokVMBxBHV|2SYHjTQpgo>
r"""°°°
### Sequenzen - Indexing, Cutting und Slicing

Ähnlich wie in Matlab können Sequenzen, darunter zählen String, Listen, numpy-Arrays, etc. komfortabel geschnitten werden.
°°°"""
# |%%--%%| <2SYHjTQpgo|8VYk5woWWo>

'Kurzwort'[1]

# |%%--%%| <8VYk5woWWo|Fa7XuzIa00>

'Kurzwort'[4]

# |%%--%%| <Fa7XuzIa00|5AetDqEbsr>

'Kurzwort'[:3]

# |%%--%%| <5AetDqEbsr|MHkhUtpwCT>

'Kurzwort'[4:]

# |%%--%%| <MHkhUtpwCT|ibkmBA6Id5>

'Kurzwort'[-4:]

# |%%--%%| <ibkmBA6Id5|Ig2znCs3YS>

'Kurzwort'[::2]

# |%%--%%| <Ig2znCs3YS|Iez6oHt7Wu>

'Kurzwort'[::-1]

# |%%--%%| <Iez6oHt7Wu|2mLxGG1HDa>
r"""°°°
### range
Python kennt nicht die klassischen for-Schleifen der Art `for (int x=0; x<n; x++)` sondern es wird hierfür üblicherweise der Sequenz-Generator `range` verwendet.
°°°"""
# |%%--%%| <2mLxGG1HDa|oKpLgthl3A>

# Hilfsfunktion für die Ausgabe aller Elemente eines Generators
def pretty_print(l):
    for x in l:
        print(x, end=' ') # trenne die Elemente mit einem Leerzeichen

# |%%--%%| <oKpLgthl3A|P4xikHt09E>

l1 = range(7)
pretty_print(l1)

# |%%--%%| <P4xikHt09E|REN44Nv6rq>

l2 = range(4, 8)
pretty_print(l2)

# |%%--%%| <REN44Nv6rq|5STkVuGLxN>

l3 = range(0, 20, 2)
pretty_print(l3)

# |%%--%%| <5STkVuGLxN|c2BDtYCBQU>
r"""°°°
### Einrücken von Blöcken

Während in Programmiersprachen, wie z.B. Java, der Code-Block, der zu einer Schleife oder einer Methode gehört zwischen zwei Klammern `{` und `}` geschrieben wird, verwendet Python dafür die Einrückung des Quellcodes mit Hilfe von TABs.
°°°"""
# |%%--%%| <c2BDtYCBQU|Re8tM8F5pM>
r"""°°°
**RAW CELLS NOT SUPPORTED BY JUKIT; CONVERTED TO MARKDOWN**; original raw-cell content:
```
# Falsch, da keine Einrückung
for i in range(5): 
print i
```
°°°"""
# |%%--%%| <Re8tM8F5pM|wsyskLg0tC>

for i in range(5): 
     print(i)

# |%%--%%| <wsyskLg0tC|SYBRLmFbRQ>
r"""°°°
### For-In-Schleife
°°°"""
# |%%--%%| <SYBRLmFbRQ|2d23UkbPyS>

for x in ['Anna', 'Bob', 'Charlie']:
    print('Name: ' + x)

# |%%--%%| <2d23UkbPyS|nQf7CC4u7v>

sum = 0

for x in range(0, 8):
    sum += x
    
print(sum)

# |%%--%%| <nQf7CC4u7v|xSt7MPKhNm>
r"""°°°
### While-Schleife
°°°"""
# |%%--%%| <xSt7MPKhNm|I93PL6i8CV>

y = 30

while y >= 0:
    print(y, end=' ')
    y = y - 3

# |%%--%%| <I93PL6i8CV|2iAg3UXoDA>
r"""°°°
### pass

Der Befehl `pass` ist lediglich als Platzhalter da. Bei seiner Ausführung passiert nichts. Er kann einfach entfernt werden, wenn er durch anderen Code ersetzt wird.
°°°"""
# |%%--%%| <2iAg3UXoDA|Yr2uOp7HHs>

def leere_funktion():
    pass # implementiere ich später

# |%%--%%| <Yr2uOp7HHs|sOkcMDbSmt>

leere_funktion()

# |%%--%%| <sOkcMDbSmt|sVI1QfouwZ>
r"""°°°
### if  / elif / else
°°°"""
# |%%--%%| <sVI1QfouwZ|TZnq52oW0l>

if 8 % 2 == 0:
    print('gerade')
else:
    print('ungerade')

# |%%--%%| <TZnq52oW0l|mHhBYY2FMy>

n = 5
if (n < 5):
    print('kleiner 5')
elif (n > 5):
    print('größer 5')
else:
    print('gleich 5')
