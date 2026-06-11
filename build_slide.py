from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

# ── Thre360 Energy brand colours ─────────────────────────────────────────────
T360_BLUE    = RGBColor(0x1A, 0x65, 0xAC)   # primary blue (from logo)
T360_GREEN   = RGBColor(0x3A, 0x99, 0x35)   # green segment
T360_ORANGE  = RGBColor(0xE8, 0x82, 0x1A)   # orange segment
T360_CHARCO  = RGBColor(0x3D, 0x3D, 0x3D)   # dark charcoal (logo text)
WHITE        = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BG     = RGBColor(0xF3, 0xF7, 0xFB)   # very light blue-grey background
RULE_GREY    = RGBColor(0xC8, 0xD6, 0xE5)
MID_GREY     = RGBColor(0xA0, 0xB4, 0xC8)
STATUS_GREEN = RGBColor(0x21, 0x96, 0x53)
STATUS_AMBER = RGBColor(0xD4, 0x5A, 0x00)
TEXT_BODY    = RGBColor(0x2B, 0x2B, 0x2B)

# ── Helpers ───────────────────────────────────────────────────────────────────
def add_rect(slide, left, top, width, height, fill_rgb=None, line_rgb=None, lw=0.5):
    s = slide.shapes.add_shape(1, left, top, width, height)
    s.line.width = Pt(lw)
    if fill_rgb:
        s.fill.solid(); s.fill.fore_color.rgb = fill_rgb
    else:
        s.fill.background()
    if line_rgb:
        s.line.color.rgb = line_rgb
    else:
        s.line.fill.background()
    return s

def textbox(slide, text, l, t, w, h, size=10, bold=False, color=TEXT_BODY,
            align=PP_ALIGN.LEFT, italic=False):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tb.word_wrap = True
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = align
    r = p.add_run(); r.text = text
    r.font.name = "Calibri"; r.font.size = Pt(size)
    r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    return tb, tf

def add_para(tf, label, status, status_col, size=9, indent=False, first=False, sp=3):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.space_before = Pt(sp)
    p.level = 1 if indent else 0
    pPr = p._p.get_or_add_pPr()
    bc = etree.SubElement(pPr, qn('a:buChar'))
    bc.set('char', '○' if indent else '▪')
    r1 = p.add_run(); r1.text = label + ":  "
    r1.font.name = "Calibri"; r1.font.size = Pt(size)
    r1.font.bold = True; r1.font.color.rgb = TEXT_BODY
    r2 = p.add_run(); r2.text = status
    r2.font.name = "Calibri"; r2.font.size = Pt(size)
    r2.font.bold = False; r2.font.color.rgb = status_col
    return p

def add_bullet(tf, text, size=9, bold=False, color=TEXT_BODY, char='▪', sp=3, first=False):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.space_before = Pt(sp)
    pPr = p._p.get_or_add_pPr()
    bc = etree.SubElement(pPr, qn('a:buChar')); bc.set('char', char)
    r = p.add_run(); r.text = text
    r.font.name = "Calibri"; r.font.size = Pt(size)
    r.font.bold = bold; r.font.color.rgb = color
    return p

def sub_header(tf, text, sp_before=5):
    p = tf.add_paragraph(); p.space_before = Pt(sp_before)
    pPr = p._p.get_or_add_pPr()
    noBu = etree.SubElement(pPr, qn('a:buNone'))
    r = p.add_run(); r.text = text
    r.font.name = "Calibri"; r.font.size = Pt(9)
    r.font.bold = True; r.font.color.rgb = T360_BLUE
    return p

# ── Presentation ──────────────────────────────────────────────────────────────
prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)
slide = prs.slides.add_slide(prs.slide_layouts[6])

W = prs.slide_width
H = prs.slide_height
M = Inches(0.32)

# Background
add_rect(slide, 0, 0, W, H, fill_rgb=LIGHT_BG)

# ── Header ────────────────────────────────────────────────────────────────────
HDR_H = Inches(0.72)
add_rect(slide, 0, 0, W, HDR_H, fill_rgb=T360_BLUE)
# Green accent stripe
add_rect(slide, 0, HDR_H, W, Pt(4), fill_rgb=T360_GREEN)
# Orange thin line below green
add_rect(slide, 0, HDR_H + Pt(4), W, Pt(2), fill_rgb=T360_ORANGE)

textbox(slide, "Operations Digital Delivery  –  June 2026",
        M, Inches(0.13), Inches(9), Inches(0.5),
        size=22, bold=True, color=WHITE)

# Logo placeholder (top-right of header) — text representation
textbox(slide, "THRE360  ENERGY",
        W - Inches(2.4), Inches(0.16), Inches(2.2), Inches(0.42),
        size=13, bold=True, color=WHITE, align=PP_ALIGN.RIGHT)

# ── Layout constants ──────────────────────────────────────────────────────────
Y_KPI   = HDR_H + Inches(0.22)
KPI_H   = Inches(1.0)
Y_BODY  = Y_KPI + KPI_H + Inches(0.18)
BODY_H  = Inches(3.48)
Y_FWD   = Y_BODY + BODY_H + Inches(0.16)
FWD_H   = Inches(1.3)

GAP     = Inches(0.18)
L_W     = Inches(6.28)   # left (Digital Initiatives)
R_W     = Inches(6.28)   # right (Chronos)
L_X     = M
R_X     = M + L_W + GAP

# ── KPI tiles ─────────────────────────────────────────────────────────────────
kpis = [
    ("Under Budget",       "All initiatives"),
    ("No Added Cost",      "Emergent work absorbed"),
    ("Reg 5 KPIs",         "No observations raised"),
    ("2 Adoption Gates",   "COSHH 365 & Omega IM"),
]
n = len(kpis)
tw = (W - 2*M - (n-1)*GAP) / n
for i, (line1, line2) in enumerate(kpis):
    tx = M + i*(tw + GAP)
    add_rect(slide, tx, Y_KPI, tw, KPI_H - Inches(0.04), fill_rgb=T360_BLUE)
    # colour bar top — alternates green / orange
    bar_col = T360_GREEN if i % 2 == 0 else T360_ORANGE
    add_rect(slide, tx, Y_KPI, tw, Pt(5), fill_rgb=bar_col)
    textbox(slide, line1, tx + Inches(0.1), Y_KPI + Inches(0.07),
            tw - Inches(0.2), Inches(0.42),
            size=12, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    textbox(slide, line2, tx + Inches(0.08), Y_KPI + Inches(0.48),
            tw - Inches(0.16), Inches(0.38),
            size=8.5, color=RULE_GREY, align=PP_ALIGN.CENTER)

# ── Card helper ───────────────────────────────────────────────────────────────
def card(slide, x, y, w, h, title, title_col=T360_BLUE):
    add_rect(slide, x, y, w, h, fill_rgb=WHITE, line_rgb=RULE_GREY, lw=0.5)
    add_rect(slide, x, y, w, Inches(0.33), fill_rgb=title_col)
    # left accent bar
    add_rect(slide, x, y, Pt(4), Inches(0.33), fill_rgb=T360_ORANGE)
    textbox(slide, title, x + Inches(0.16), y + Inches(0.045),
            w - Inches(0.28), Inches(0.26),
            size=10.5, bold=True, color=WHITE)

def card_tf(slide, x, y, w, h, top_pad=Inches(0.38)):
    tb = slide.shapes.add_textbox(x + Inches(0.16), y + top_pad,
                                   w - Inches(0.32), h - top_pad - Inches(0.1))
    tb.word_wrap = True
    tf = tb.text_frame; tf.word_wrap = True
    return tf

# ── Digital Initiatives card ──────────────────────────────────────────────────
card(slide, L_X, Y_BODY, L_W, BODY_H, "Digital Initiatives")
tf_di = card_tf(slide, L_X, Y_BODY, L_W, BODY_H)

items_di = [
    ("KPI Dashboard",                    "Centralisation & AIRB complete; NEO Next rollout live; automation in progress.", STATUS_GREEN, False),
    ("Omega 365 — Incident Management",  "Live",                                         STATUS_GREEN, True),
    ("Omega 365 — Action Management",    "Live  (Quality rollout delayed)",               STATUS_AMBER, True),
    ("COSHH 365",                        "Live; adoption gate approved",                  STATUS_GREEN, False),
    ("Salus Suite",                      "In progress; delayed by Safety Case priorities; training commenced", STATUS_AMBER, False),
    ("BP Andrew & NEO Transition",       "Active",                                        STATUS_GREEN, False),
    ("Reg 5 Support",                    "Active",                                        STATUS_GREEN, False),
    ("Training & Competence",            "Vendor selection in progress",                  STATUS_AMBER, False),
    ("CMMS",                             "Final vendor selection in progress",             STATUS_AMBER, False),
]

first = True
for label, status, col, indent in items_di:
    add_para(tf_di, label, status, col, indent=indent, first=first, sp=0 if first else 3)
    first = False

# ── Chronos Developments card ─────────────────────────────────────────────────
card(slide, R_X, Y_BODY, R_W, BODY_H, "Chronos Developments")
tf_ch = card_tf(slide, R_X, Y_BODY, R_W, BODY_H)

# first para — sub-header "Live"
p0 = tf_ch.paragraphs[0]; p0.space_before = Pt(0)
pPr0 = p0._p.get_or_add_pPr()
etree.SubElement(pPr0, qn('a:buNone'))
r0 = p0.add_run(); r0.text = "Live"
r0.font.name = "Calibri"; r0.font.size = Pt(9)
r0.font.bold = True; r0.font.color.rgb = T360_BLUE

live_items = [
    "HR Dashboards", "Service Orders / Agreements",
    "New Start Forms", "Resource Utilisation", "Purchase Requisitions",
]
for item in live_items:
    add_para(tf_ch, item, "Live", STATUS_GREEN, sp=2)

sub_header(tf_ch, "In Progress", sp_before=5)
prog_items = [
    ("Expenses Enhancements", "Complete; rollout in progress"),
    ("AP Register",           "User testing"),
    ("Sales Invoicing",       "User testing"),
]
for label, status in prog_items:
    add_para(tf_ch, label, status, STATUS_AMBER, sp=2)

sub_header(tf_ch, "New Development Scoping", sp_before=5)
scope_items = [
    "AP Month-End Automation",
    "Goods Receipt & Manifest",
    "Budget Management (Actual vs Budget)",
]
for item in scope_items:
    add_bullet(tf_ch, item, sp=2)

# ── Forward View card (full width) ────────────────────────────────────────────
card(slide, M, Y_FWD, W - 2*M, FWD_H, "Forward View & Pipeline", title_col=T360_CHARCO)
# orange accent bar overrides left bar
add_rect(slide, M, Y_FWD, Pt(4), Inches(0.33), fill_rgb=T360_ORANGE)

fwd_items = [
    "Complete remaining capitalisation initiatives",
    "Continue BP Andrew transition support",
    "Progress Salus Suite rollout",
    "Finalise CMMS selection",
    "Finalise Training & Competence system selection and roll-out",
    "Prepare next 6-month capitalisation programme",
]
half = (len(fwd_items) + 1) // 2
iw = (W - 2*M - Inches(0.32) - GAP) / 2
col_y = Y_FWD + Inches(0.38)
col_h = FWD_H - Inches(0.46)

for col_idx, items in enumerate([fwd_items[:half], fwd_items[half:]]):
    cx = M + Inches(0.16) + col_idx * (iw + GAP)
    tb = slide.shapes.add_textbox(cx, col_y, iw, col_h)
    tb.word_wrap = True
    tf = tb.text_frame; tf.word_wrap = True
    first = True
    for item in items:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_before = Pt(3)
        pPr = p._p.get_or_add_pPr()
        bc = etree.SubElement(pPr, qn('a:buChar')); bc.set('char', '▸')
        r = p.add_run(); r.text = item
        r.font.name = "Calibri"; r.font.size = Pt(9.5)
        r.font.bold = False; r.font.color.rgb = TEXT_BODY

# ── Footer ────────────────────────────────────────────────────────────────────
FOOT_H = Inches(0.28)
add_rect(slide, 0, H - FOOT_H, W, FOOT_H, fill_rgb=T360_CHARCO)
# green + orange footer accent
add_rect(slide, 0, H - FOOT_H, Inches(2.4), Pt(3), fill_rgb=T360_GREEN)
add_rect(slide, Inches(2.4), H - FOOT_H, Inches(1.2), Pt(3), fill_rgb=T360_ORANGE)

textbox(slide, "Thre360 Energy  |  Confidential  |  June 2026",
        M, H - FOOT_H + Inches(0.04), W/2, Inches(0.22),
        size=7.5, color=MID_GREY)
textbox(slide, "Operations Digital Delivery",
        W/2, H - FOOT_H + Inches(0.04), W/2 - M, Inches(0.22),
        size=7.5, color=MID_GREY, align=PP_ALIGN.RIGHT)

# ── Save ──────────────────────────────────────────────────────────────────────
out = "/home/user/strateq-dx-cdo-coworker/Operations_Digital_Delivery_June2026.pptx"
prs.save(out)
print("Saved:", out)
