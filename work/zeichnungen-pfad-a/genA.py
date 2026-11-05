# Strichzeichnungen für den neuen Pfad A (Kraft daheim mit Hanteln)
from lib import *
PLATE="#5B6B95"
def plate(x,y,r=30): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{PROPF}" stroke="{PLATE}" stroke-width="5"/><circle cx="{x}" cy="{y}" r="6" fill="{PLATE}"/>'
def bar(x1,y1,x2,y2): return f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{PLATE}" stroke-width="6" stroke-linecap="round"/>'
def dumbbell(x,y,horizontal=True):
    if horizontal:
        return f'<g fill="{PLATE}"><rect x="{x-20}" y="{y-3}" width="40" height="6" rx="2"/><rect x="{x-24}" y="{y-11}" width="10" height="22" rx="3"/><rect x="{x+14}" y="{y-11}" width="10" height="22" rx="3"/></g>'
    return f'<g fill="{PLATE}"><rect x="{x-3}" y="{y-20}" width="6" height="40" rx="2"/><rect x="{x-11}" y="{y-24}" width="22" height="10" rx="3"/><rect x="{x-11}" y="{y+14}" width="22" height="10" rx="3"/></g>'
def scaled(body, x0, s): return f'<g transform="translate({x0},360) scale({s}) translate({-x0},-360)">{body}</g>'
def stand(dx, arm, extra=""):
    return person(P((dx+198,88),(dx+200,196),[(dx+200,196),(dx+206,274),(dx+203,350),(dx+234,354)],(dx+204,58),arm))+extra
F={}
# 1 Kniebeuge mit Langhantel
k1=plate(184,96,26)+stand(0,[(198,90),(176,122),(186,98)])
k2=plate(584,182,26)+person(P((600,176),(565,278),[(565,278),(650,282),(603,350),(634,354)],(614,146),[(600,178),(578,210),(588,184)]))
F["kniebeuge-langhantel"]=(floor(120,330)+k1+arrow(400,220)+floor(500,720)+k2,"Kniebeuge mit Langhantel: stehend und in der Hocke")
# 2 Liegestütz
def push(sh,el,hd,hp,kn,an,to,hand): return person(P(sh,hp,[hp,kn,an,to],hd,[sh,el,hand]))
p1=push((135,240),(133,296),(107,229),(237,282),(313,313),(388,338),(398,356),(130,352))
p2=push((530,318),(566,300),(502,314),(620,326),(694,332),(764,338),(774,356),(522,352))
F["liegestuetz"]=(mat(70,420)+p1+arrow(440,220)+mat(470,800)+p2,"Liegestütz: Arme gestreckt und Brust knapp über dem Boden")
# 3 Rudern mit Kurzhantel
def bench(x1,x2,y=290): return f'<g fill="none" stroke="{PROP}" stroke-width="5" stroke-linecap="round"><path d="M{x1},{y} L{x2},{y}"/><path d="M{x1+10},{y} L{x1+10},360"/><path d="M{x2-10},{y} L{x2-10},360"/></g>'
def row(dx, el, wr):
    far={"arm":[(dx+275,236),(dx+292,262),(dx+300,288)]}
    return person(P((dx+275,236),(dx+170,215),[(dx+170,215),(dx+190,282),(dx+176,350),(dx+206,354)],(dx+306,232),[(dx+275,238),el,wr]),far=far)+dumbbell(wr[0],wr[1]+6)
F["rudern-kurzhantel"]=(floor(120,380)+bench(280,370)+row(0,(272,292),(272,338))+arrow(410,180)+floor(520,780)+bench(680,770)+row(400,(636,210),(652,262)),"Einarmiges Rudern mit Kurzhantel: Arm gestreckt und Ellenbogen nach oben gezogen")
# 4 Unterarmstütz
pl=person(P((345,290),(450,307),[(450,307),(525,324),(600,340),(608,356)],(317,281),[(345,292),(347,348),(290,350)]))
F["unterarmstuetz"]=(mat(270,650)+pl,"Unterarmstütz: Körper von Kopf bis Fuß in einer Linie")
# 5 Kreuzheben
d1=person(P((255,190),(165,250),[(165,250),(225,282),(205,350),(236,354)],(282,172),[(255,192),(250,250),(243,309)]))+plate(240,330)
d2=stand(400,[(598,90),(602,150),(606,205)])+plate(606,212)
F["kreuzheben-langhantel"]=(floor(120,340)+d1+arrow(410,220)+floor(500,720)+d2,"Kreuzheben mit Langhantel: Hantel am Boden und aufrecht stehend")
# 6 Klimmzüge
def pullbar(x1,x2): return f'<g stroke="{PROP}" stroke-width="5" stroke-linecap="round"><path d="M{x1},40 L{x2},40"/><path d="M{x1},40 L{x1},8"/><path d="M{x2},40 L{x2},8"/></g>'
c1=person(P((200,160),(200,265),[(200,265),(212,335),(172,368),(160,360)],(206,134),[(200,162),(201,104),(202,44)]))
c2=person(P((598,80),(598,185),[(598,185),(612,255),(574,290),(562,282)],(606,20),[(598,82),(628,82),(604,44)]))
F["klimmzuege"]=(scaled(pullbar(120,290)+c1,200,.85)+arrow(400,220)+scaled(pullbar(520,690)+c2,600,.85),"Klimmzug: gestreckter Hang und Kinn über der Stange")
# 7 Schulterdrücken
s1=stand(0,[(198,90),(222,132),(214,92)],dumbbell(214,90))
s2=stand(400,[(598,90),(602,28),(604,-30)],dumbbell(604,-30))
F["schulterdruecken-kurzhantel"]=(floor(110,330)+scaled(s1,200,.8)+arrow(400,250)+floor(500,720)+scaled(s2,600,.8),"Schulterdrücken mit Kurzhanteln: Hanteln an den Schultern und über dem Kopf")
# Vorderansicht
def front(cx, legs, arms, extra=""):
    s=""
    for leg in legs: s+=seg(leg,20)
    s+=seg([(cx,96),(cx,192)],46)
    s+=head(cx,60)
    for arm in arms: s+=seg(arm,17)
    return s+extra
def tband(a,b): return f'<path d="M{a[0]},{a[1]} L{b[0]},{b[1]}" stroke="#C2410C" stroke-width="5" stroke-linecap="round"/>'
def legs_std(cx,w=18,knee=0,yk=274): return [[(cx-16,196),(cx-w-knee,yk),(cx-w,350),(cx-w-22,354)],[(cx+16,196),(cx+w+knee,yk),(cx+w,350),(cx+w+22,354)]]
# 9 Band auseinanderziehen (Pull-Apart)
pa1=front(200,legs_std(200),[[(176,100),(184,132),(194,112)],[(224,100),(216,132),(206,112)]],tband((194,112),(206,112)))
pa2=front(600,legs_std(600),[[(576,100),(520,102),(462,104)],[(624,100),(680,102),(738,104)]],tband((462,104),(738,104)))
F["band-auseinanderziehen"]=(floor(120,280)+pa1+arrow(330,220)+floor(440,760)+pa2,"Theraband auseinanderziehen: Hände vor der Brust und Arme seitlich gestreckt")
# 10 Seitwärtsgehen mit Band
def walk(cx,w):
    legs=[[(cx-16,200),(cx-w-6,272),(cx-w,350),(cx-w-22,354)],[(cx+16,200),(cx+w+6,272),(cx+w,350),(cx+w+22,354)]]
    arms=[[(cx-24,104),(cx-46,150),(cx-22,192)],[(cx+24,104),(cx+46,150),(cx+22,192)]]
    return f'<g transform="translate(0,14)">{front(cx,legs,arms)}</g>'+tband((cx-w-4,300),(cx+w+4,300))
F["seitwaertsgehen-band"]=(floor(110,300)+walk(200,24)+arrow(370,220)+floor(430,780)+walk(600,62)+arrow(720,150),"Seitwärtsgehen mit Theraband um die Beine: Füße hüftbreit und Schritt zur Seite")

# Tür mit Türschnalle (Seitenansicht: schmale Kante; Vorderansicht: Türblatt)
HANDLE=164
def door_side(x): return f'<rect x="{x}" y="20" width="12" height="340" rx="2" fill="{PROPF}" stroke="{PROP}" stroke-width="4"/><path d="M{x},{HANDLE} L{x-20},{HANDLE}" stroke="{PLATE}" stroke-width="6" stroke-linecap="round"/>'
def door_front(x1,x2): return f'<rect x="{x1}" y="20" width="{x2-x1}" height="340" rx="3" fill="{PROPF}" stroke="{PROP}" stroke-width="4"/><path d="M{x2-14},{HANDLE} L{x2-34},{HANDLE}" stroke="{PLATE}" stroke-width="6" stroke-linecap="round"/>'
# 11 Rudern stehend, Band an der Türschnalle
def rowd(dx, el, wr):
    p=person(P((dx+150,90),(dx+150,198),[(dx+150,198),(dx+160,274),(dx+154,350),(dx+184,354)],(dx+156,60),[(dx+150,92),el,wr]))
    return p+tband(wr,(dx+338,HANDLE))
F["rudern-band-tuer"]=(floor(80,372)+door_side(360)+rowd(0,(196,136),(240,166))+arrow(400,70)+floor(480,772)+door_side(760)+rowd(400,(512,140),(566,162)),"Rudern stehend mit Theraband an der Türschnalle: Arme vorne und Ellenbogen zurückgezogen")
# 12 Außenrotation der Schulter
def ar(cx, hand, dx):
    legs=legs_std(cx)
    arms=[[(cx-24,104),(cx-30,152),(cx-32,204)],[(cx+24,104),(cx+30,170),hand]]
    return front(cx,legs,arms)+tband((dx+96,HANDLE),hand)
F["aussenrotation-band-tuer"]=(floor(20,330)+door_front(20,110)+ar(230,(206,176),0)+arrow(400,70)+floor(420,730)+door_front(420,510)+ar(630,(702,170),400),"Außenrotation der Schulter mit Theraband an der Türschnalle: Unterarm vor dem Bauch und nach außen gedreht")
# 13 Holzhacker diagonal
def chop(cx, la, ra, hands, dx):
    legs=legs_std(cx,30,6)
    return front(cx,legs,[la,ra])+tband((dx+96,HANDLE),hands)
c1=chop(240,[(216,104),(196,150),(192,194)],[(264,104),(232,154),(196,192)],(194,193),0)
c2=chop(640,[(616,104),(660,72),(706,46)],[(664,104),(690,70),(710,44)],(708,45),400)
F["holzhacker-band-tuer"]=(floor(20,340)+door_front(20,110)+c1+arrow(400,250)+floor(420,760)+door_front(420,510)+c2,"Holzhacker mit Theraband an der Türschnalle: Hände an der Hüfte und diagonal nach oben gezogen")

for k,(b,t) in F.items(): open(k+".svg","w").write(svg(b,t))
print(len(F))
