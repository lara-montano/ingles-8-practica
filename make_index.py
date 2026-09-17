import re, sys, os
# Genera index.html (portada de GitHub Pages) de ingles-8-practica. Uso: python3 make_index.py  (desde la raiz del repo)
# Edita la lista SIMS cuando agregues un simulador y vuelve a correrlo. Las paginas que aun no existen se omiten.
R = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(R, "02_Simuladores_web")
SEAL_FALLBACK = os.path.expanduser("~/Documents/GitHub/ingles-6-practica/04_Simuladores_web/U2_G7_reported_speech.html")

def seal():
    cands = sorted(f for f in os.listdir(WEB) if f.endswith(".html")) if os.path.isdir(WEB) else []
    src = os.path.join(WEB, cands[0]) if cands else SEAL_FALLBACK
    tpl = open(src, encoding="utf-8").read()
    i = tpl.index("<!-- ============ Sello de autoría"); j = tpl.index("</script>", i) + len("</script>")
    return tpl[i:j]

SIMS = [
 ("u1","Unit 1 · Grammar 1","Coordinate connectors","and · but · or · so · yet · nor, paired conjunctions, ellipsis and agreement.","U1_G1_coordinate_connectors.html"),
 ("u1","Unit 1 · Grammar 2","Adverb clauses of time & cause","when · while · until · as soon as · since · because; no <i>will</i> in a time clause.","U1_G2_time_cause_clauses.html"),
 ("u1","Unit 1 · Grammar 3","Condition, contrast, manner & place","if · unless · provided that · although · whereas · despite · as if · wherever.","U1_G3_condition_contrast_manner_place.html"),
 ("u2","Unit 2 · Grammar 4","Noun clauses","Statement order, whether/if, the subjunctive, extraposition with <i>It … that</i>.","U2_G4_noun_clauses.html"),
 ("u2","Unit 2 · Grammar 5","Adjective clauses","Connector vs connector-subject, preposition + which, quantifier + of which.","U2_G5_adjective_clauses.html"),
 ("u3","Unit 3 · Grammar 6","Reduced adjective clauses","Participles, appositives, <i>the first + to</i>-infinitive: the reduction press.","U3_G6_reduced_adjective_clauses.html"),
 ("u3","Unit 3 · Grammar 7","Reduced adverb clauses","while/when + -ing, dangling participles, absolute constructions.","U3_G7_reduced_adverb_clauses.html"),
 ("u3","Unit 3 · Grammar 8","The passive at C1","Every tense, get-passive, causatives, need + -ing, verbs with no passive.","U3_G8_passive_c1.html"),
 ("u4","Unit 4 · Grammar 9","Parallel structure","Single and paired conjunctions: same form on both sides.","U4_G9_parallel_structure.html"),
 ("u4","Unit 4 · Grammar 10","Parallelism in comparisons","that of / those of, the … the, comparison intensifiers.","U4_G10_parallel_comparisons.html"),
 ("u5","Unit 5 · Grammar 11","Inversion after place & negatives","Rarely has…, Not until…, So do I / Neither did we.","U5_G11_inversion_place_negative.html"),
 ("u5","Unit 5 · Grammar 12","Inversion in conditionals & comparisons","Had she known…, Should you need…, …than did the others.","U5_G12_inversion_conditionals_comparisons.html"),
]

STRUCT = [
 ("u1","Unit 1 · Structure 1","Noun number","Agreement under pressure: the real subject, uncountables, criteria and data.","U1_S1_noun_number.html"),
 ("u2","Unit 2 · Structure 2","Person vs thing","-er / -ee / -tion: who does what to whom.","U2_S2_person_vs_thing.html"),
 ("u4","Unit 4 · Structure 3","Make vs do","Divorcing <i>hacer</i>: make sense, do without.","U4_S3_make_vs_do.html"),
 ("u4","Unit 4 · Structure 4","Like, alike & unlike","Position rules, and <i>like</i> + noun vs <i>as</i> + clause.","U4_S4_like_alike_unlike.html"),
 ("u4","Unit 4 · Structure 5","Other, another & others","A decision grid: singular or plural, specific or not.","U4_S5_other_another_others.html"),
 ("u5","Unit 5 · Structure 6","-ly and predicate adjectives","friendly and likely are adjectives; asleep only follows the verb.","U5_S6_ly_and_predicate_adjectives.html"),
 ("u5","Unit 5 · Structure 7","-ed vs -ing adjectives","The source confuses; the person is confused.","U5_S7_ed_vs_ing_adjectives.html"),
]

def struct_cards():
    out=[]
    for u,k,t,d,f in STRUCT:
        if not os.path.exists(os.path.join(WEB, f)):
            print("  (Structure omitida, no existe aun):", f); continue
        out.append(f'    <a class="sim {u}" href="02_Simuladores_web/{f}"><div class="unit">{k}</div><h3>{t}</h3><p>{d}</p><span class="go">Abrir \u2192</span></a>')
    return "\n".join(out)
def sim_cards():
    out = []
    for u,k,t,d,f in SIMS:
        if not os.path.exists(os.path.join(WEB, f)):
            print("  (omitida, no existe aun):", f); continue
        out.append(f'    <a class="sim {u}" href="02_Simuladores_web/{f}"><div class="unit">{k}</div><h3>{t}</h3><p>{d}</p><span class="go">Abrir →</span></a>')
    return "\n".join(out)

html = f"""<!DOCTYPE html>
<!-- =====================================================================
  INGLÉS 8 · Material de práctica (C1 · preparación SELLI) · página de inicio del sitio
  Autor: Prof. Daniel Lara · Instagram y Google Scholar: profe.daniellara
  No elimines los créditos.
====================================================================== -->
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="Prof. Daniel Lara (@profe.daniellara)">
<meta name="copyright" content="© Prof. Daniel Lara — Instagram/Google Scholar: profe.daniellara">
<title>Inglés 8 · Práctica · Prof. Daniel Lara</title>
<style>
  :root{{
    --navy:#1F3A5F; --navydark:#142741; --navylt:#E8ECF3;
    --steel:#2C5F8C; --plum:#7A3B69; --copper:#9C4511; --garnet:#8C2F3F; --royal:#4B3A8C;
    --grammar:#D9761A; --grammarlt:#FBEEDF;
    --ink:#262626; --soft:#F4F6F5; --rule:#CBD3CE;
  }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  html{{-webkit-text-size-adjust:100%;scroll-behavior:smooth}}
  body{{font-family:Lato,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--soft);line-height:1.55}}
  header{{background:linear-gradient(135deg,#1B3B58,#0F2338);color:#fff;padding:26px 20px 22px;position:relative;overflow:hidden}}
  header .deco{{position:absolute;right:16px;top:-14px;font-size:118px;opacity:.12;pointer-events:none}}
  .wrap{{max-width:1000px;margin:0 auto;padding:0 14px 90px}}
  header .wrap{{padding-bottom:0}}
  .kicker{{font-size:12px;letter-spacing:.13em;font-weight:800;color:#BFD3EE;text-transform:uppercase}}
  header h1{{font-size:clamp(24px,4.6vw,36px);margin:4px 0 4px;font-weight:900}}
  header .sub{{color:#D6E1F0;font-size:clamp(13px,2.3vw,16px);max-width:720px}}
  .chipline{{margin-top:10px;display:flex;gap:6px;flex-wrap:wrap}}
  .chipline a,.chipline span{{background:rgba(255,255,255,.16);border-radius:999px;padding:4px 12px;font-size:12px;font-weight:700;color:#fff;text-decoration:none}}
  .chipline a:hover{{background:rgba(255,255,255,.28)}}
  nav{{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--rule);box-shadow:0 1px 4px rgba(0,0,0,.05)}}
  nav .wrap{{display:flex;gap:4px;flex-wrap:wrap;padding:6px 14px}}
  nav a{{color:var(--navy);text-decoration:none;font-weight:800;font-size:14px;padding:8px 12px;border-radius:9px}}
  nav a:hover{{background:var(--navylt)}}
  main{{padding-top:18px}}
  section{{margin-bottom:26px;scroll-margin-top:60px}}
  section>h2{{font-size:22px;color:var(--navydark);margin-bottom:4px}}
  section>p.lead{{color:#555;font-size:15px;margin-bottom:12px}}
  .card{{background:#fff;border:1px solid var(--rule);border-radius:14px;padding:16px 18px;margin-bottom:14px;box-shadow:0 1px 4px rgba(0,0,0,.05)}}
  .card h3{{font-size:17px;color:var(--navydark);margin-bottom:4px}}
  .muted{{color:#666;font-size:14px}}
  .grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}}
  .sim{{display:block;background:#fff;border:1px solid var(--rule);border-left:6px solid var(--steel);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--ink);box-shadow:0 1px 4px rgba(0,0,0,.05);transition:transform .12s,box-shadow .12s}}
  .sim:hover{{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.09)}}
  .sim.u1{{border-left-color:var(--steel)}} .sim.u2{{border-left-color:var(--plum)}} .sim.u3{{border-left-color:var(--copper)}} .sim.u4{{border-left-color:var(--garnet)}} .sim.u5{{border-left-color:var(--royal)}}
  .sim .unit{{font-size:11px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:#777}}
  .sim.u1 .unit{{color:var(--steel)}} .sim.u2 .unit{{color:var(--plum)}} .sim.u3 .unit{{color:var(--copper)}} .sim.u4 .unit{{color:var(--garnet)}} .sim.u5 .unit{{color:var(--royal)}}
  .sim h3{{font-size:16px;margin:2px 0 4px;color:var(--navydark)}}
  .sim p{{font-size:13.5px;color:#555}}
  .sim .go{{display:inline-block;margin-top:8px;font-weight:800;font-size:13px;color:var(--grammar)}}
  .btns{{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0 6px}}
  .btn{{display:inline-block;border:0;border-radius:10px;padding:9px 14px;font:800 14px Lato,sans-serif;text-decoration:none;color:#fff;background:var(--navy);cursor:pointer}}
  .btn.ghost{{background:#fff;color:var(--navy);border:2px solid var(--navy)}}
  .rows{{list-style:none}}
  .row{{display:grid;grid-template-columns:1fr auto;gap:6px 12px;align-items:center;padding:9px 0;border-top:1px solid var(--rule)}}
  .row:first-child{{border-top:0}}
  .row .t{{font-weight:800;font-size:14.5px}}
  .row .d{{font-size:12.5px;color:#777}}
  .row audio{{width:100%;max-width:340px;height:36px}}
  .tip{{background:var(--grammarlt);border-left:4px solid var(--grammar);border-radius:8px;padding:10px 12px;font-size:14px;margin-top:12px}}
  footer.credits{{text-align:center;color:#666;font-size:13px;padding:22px 14px 0}}
  footer.credits a{{color:var(--navy);font-weight:700}}
  @media(max-width:560px){{.row{{grid-template-columns:1fr}}.row audio{{max-width:100%}}}}
</style>
</head>
<body>
<header>
  <div class="deco">🏗️</div>
  <div class="wrap">
    <div class="kicker">Inglés 8 · C1 · preparación SELLI</div>
    <h1>Material de práctica</h1>
    <p class="sub">Una página interactiva por cada tema del manual, de gramática (Grammar 1–12) y de vocabulario (Structure 1–7), más el simulacro tipo SELLI de las Units 1–2 con su audio. Todo se abre desde aquí.</p>
    <div class="chipline">
      <span>Prof. Daniel Lara</span>
      <a href="https://www.instagram.com/profe.daniellara/" target="_blank" rel="noopener">Instagram @profe.daniellara</a>
      <a href="https://scholar.google.com/citations?user=ifG2_hwAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
      <a href="https://github.com/lara-montano/ingles-8-practica" target="_blank" rel="noopener">Descargar todo (GitHub)</a>
    </div>
  </div>
</header>
<nav><div class="wrap">
  <a href="#simuladores">🧪 Simuladores</a><a href="#structure">🔤 Structure</a><a href="#mock">📝 SELLI Mock</a>
</div></nav>
<main class="wrap">

<section id="simuladores">
  <h2>Simuladores de gramática</h2>
  <p class="lead">Una página por tema del manual, en los dos formatos del examen: <b>Structure</b> (completar la oración) y <b>Written Expression</b> (hallar el error). Tres modos: <b>Explore</b> (la regla en acción) → <b>Build</b> (arma oraciones) → <b>Drill</b> (práctica graduada ★ ★★ ★★★ con marcador y racha). Funcionan sin internet: puedes guardar la página en tu teléfono.</p>
  <div class="grid">
{sim_cards()}
  </div>
</section>

<section id="structure">
  <h2>Vocabulario y precisión léxica</h2>
  <p class="lead">Las páginas de <b>Structure</b> del manual: concordancia bajo presión, sufijos de papel, los confundibles (<i>make/do</i>, <i>like/as</i>, <i>other/another</i>) y los adjetivos que cambian de sentido según la posición o el participio. Mismos tres modos y el Drill en los dos formatos del examen.</p>
  <div class="grid">
{struct_cards()}
  </div>
</section>

<section id="mock">
  <h2>SELLI Mock · Units 1–2</h2>
  <p class="lead">Simulacro de práctica en formato SELLI restringido a las Units 1–2: 81 reactivos, 85 minutos (Listening 16 · Structure 20 · Written Expression 25 · Reading 20). No cuenta para la calificación; sirve para ver qué fila del perfil sale baja.</p>
  <div class="card">
    <h3>Cómo se aplica</h3>
    <p class="muted">Sección A (Listening): reproduce el audio <b>una sola vez y sin pausar</b>; trae las instrucciones, el ejemplo y 12 segundos de respuesta por reactivo. Después resuelve las Secciones B–D en unos 70 minutos y llena la hoja de perfil del final.</p>
    <div class="btns"><a class="btn" href="01_SELLI_Mock_U1-U2/selli_mock_u1u2.pdf" target="_blank" rel="noopener">📄 Cuadernillo (PDF, 11 págs.)</a><a class="btn ghost" href="01_SELLI_Mock_U1-U2/selli_mock_u1u2_listening.m4a" download>⬇️ Descargar el audio</a></div>
    <ul class="rows"><li class="row"><div><div class="t">Sección A · Listening</div><div class="d">11:45 · instrucciones + 16 reactivos con sus pausas</div></div><audio controls preload="none" src="01_SELLI_Mock_U1-U2/selli_mock_u1u2_listening.m4a"></audio></li></ul>
    <div class="tip"><b>Reglas de oro.</b> En Structure, identifica primero qué le falta a la oración (sujeto, verbo o conector); en Written Expression, revisa concordancia, paralelismo y forma verbal antes que el vocabulario; nunca dejes un reactivo en blanco.</div>
  </div>
</section>

</main>
<footer class="credits">
  Material creado por <b>Prof. Daniel Lara</b> ·
  <a href="https://www.instagram.com/profe.daniellara/" target="_blank" rel="noopener">Instagram @profe.daniellara</a> ·
  <a href="https://scholar.google.com/citations?user=ifG2_hwAAAAJ" target="_blank" rel="noopener">Google Scholar</a><br>
  Inglés 8 · C1 · © 2026 · Si lo compartes, conserva la atribución.
</footer>

{seal()}
</body>
</html>
"""
open(os.path.join(R, "index.html"), "w", encoding="utf-8").write(html)
print("index.html:", len(html), "bytes; tarjetas:", html.count('class="sim '))
