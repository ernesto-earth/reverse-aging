# Erzeugt einfache Strichzeichnungen (Start- und Endposition) für Pfad B
OUT="#33467A"; IN="#E9EDF6"; FAR="#D3DAEA"; PROP="#8C97B5"; PROPF="#F1F3F8"
def seg(pts, w=20, inner=IN):
    d="M"+" L".join(f"{x},{y}" for x,y in pts)
    return (f'<path d="{d}" fill="none" stroke="{OUT}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{inner}" stroke-width="{w-6}" stroke-linecap="round" stroke-linejoin="round"/>')
def head(x,y,r=22): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{IN}" stroke="{OUT}" stroke-width="3"/>'
def person(p, far=None):
    s=""
    if far:
        if "leg" in far: s+=seg(far["leg"],18,FAR)
        if "arm" in far: s+=seg(far["arm"],16,FAR)
    s+=seg([p["shoulder"],p["hip"]],34)
    s+=seg(p["leg"],20)
    s+=head(*p["head"])
    s+=seg(p["arm"],17)
    return s
def floor(x1,x2,y=360): return f'<path d="M{x1},{y} L{x2},{y}" stroke="{PROP}" stroke-width="3" stroke-linecap="round"/>'
def mat(x1,x2,y=356): return f'<rect x="{x1}" y="{y}" width="{x2-x1}" height="9" rx="4" fill="{PROPF}" stroke="{PROP}" stroke-width="2.5"/>'
def chair(x):
    return (f'<g fill="none" stroke="{PROP}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M{x},180 L{x},360"/><path d="M{x},282 L{x+90},282 L{x+90},360"/><path d="M{x+8},292 L{x+82},292"/></g>')
def table(x1,x2,y=250):
    return (f'<g fill="none" stroke="{PROP}" stroke-width="5" stroke-linecap="round"><path d="M{x1},{y} L{x2},{y}"/>'
            f'<path d="M{x1+12},{y} L{x1+12},360"/><path d="M{x2-12},{y} L{x2-12},360"/></g>')
def band(a,b):
    (x1,y1),(x2,y2)=a,b
    return f'<path d="M{x1},{y1-4} Q{(x1+x2)/2},{(y1+y2)/2-10} {x2},{y2} M{x1},{y1+4} Q{(x1+x2)/2},{(y1+y2)/2+8} {x2},{y2}" fill="none" stroke="#C2410C" stroke-width="3.5" stroke-linecap="round"/>'
def arrow(x,y): return f'<path d="M{x-18},{y} L{x+18},{y} M{x+8},{y-9} L{x+18},{y} L{x+8},{y+9}" fill="none" stroke="{PROP}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
def svg(body, title): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" role="img" aria-label="{title}">{body}</svg>'
def P(sh,hp,leg,hd,arm): return dict(shoulder=sh,hip=hp,leg=leg,head=hd,arm=arm)
figs={}
# 1 Aufstehen vom Stuhl
a=P((212,168),(200,276),[(200,276),(282,272),(287,350),(318,354)],(222,138),[(212,170),(244,214),(208,196)])
b=P((590,86),(590,196),[(590,196),(596,274),(593,350),(624,354)],(592,56),[(590,88),(618,134),(584,118)])
figs["aufstehen-vom-stuhl"]=svg(floor(110,350)+chair(150)+person(a)+arrow(400,250)+floor(450,700)+chair(470)+person(b),"Aufstehen vom Stuhl: sitzend und stehend")
# 2 Tisch-Liegestütz
def incline(sh, el, hp, kn, an, to, hd, hand):
    return person(P(sh,hp,[hp,kn,an,to],hd,[sh,el,hand]))
figs["tisch-liegestuetz"]=svg(floor(40,400)+table(55,190)+incline((215,142),(202,196),(299,228),(359,290),(420,352),(446,350),(195,120),(185,248))+arrow(420,180)
    +floor(450,790)+table(450,565)+incline((588,206),(616,236),(668,262),(724,304),(768,350),(784,350),(565,190),(560,248)),"Liegestütz am Tisch: oben und unten")
# 3 Rudern mit Band
def row(dx, el, wr):
    p=P((dx+155,236),(dx+150,343),[(dx+150,343),(dx+232,333),(dx+312,343),(dx+320,316)],(dx+160,206),[(dx+155,238),el,wr])
    return person(p)+band(wr,(dx+324,330))
figs["rudern-mit-band"]=svg(mat(90,370)+row(0,(208,262),(266,278))+arrow(400,230)+mat(490,770)+row(400,(520,276),(586,270)),"Rudern mit Widerstandsband im Sitzen: Arme gestreckt und gezogen")
# 4 Hüftheben
def bridge(dx, hp, kn):
    return person(P((dx+122,344),hp,[hp,kn,(dx+344,350),(dx+372,353)],(dx+90,338),[(dx+122,346),(dx+176,352),(dx+228,354)]))
figs["hueftheben"]=svg(mat(50,390)+bridge(0,(232,346),(300,288))+arrow(400,230)+mat(450,790)+bridge(400,(622,300),(700,276)),"Hüftheben in Rückenlage: Becken unten und angehoben")
# 5 Dead Bug
s1=P((130,340),(242,345),[(242,345),(244,262),(326,262),(334,250)],(98,334),[(130,338),(132,280),(134,220)])
s2=P((530,340),(642,345),[(642,345),(714,328),(784,316),(790,302)],(498,334),[(530,338),(472,322),(414,308)])
figs["dead-bug"]=svg(mat(50,370)+person(s1)+arrow(400,200)+mat(380,790)+person(s2,far={"leg":[(642,345),(644,262),(726,262),(734,250)],"arm":[(530,338),(532,280),(534,220)]}),"Dead Bug in Rückenlage: Grundposition und Arm und Bein gegengleich gestreckt")
for k,v in figs.items(): open(k+".svg","w").write(v)
print(list(figs))
