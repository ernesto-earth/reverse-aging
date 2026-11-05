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
if __name__!="__main__": pass
