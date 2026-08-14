#!/usr/bin/env python3
"""Generate the "Gates of Earth" situation map for the modern universe.

Output: art/generated/gates-of-earth-2034.svg — a dark ops-room world map
showing the 47 confirmed gates (held/contained/destroyed), the D-sites of
the Lattice, and the nations that host or cooperate on the gates.

Source data: Natural Earth 110m admin-0 countries (public domain).
  ne_110m_admin_0_countries.geojson — https://www.naturalearthdata.com/
  (mirror: https://raw.githubusercontent.com/nvkelso/natural-earth-vector/
   master/geojson/ne_110m_admin_0_countries.geojson)
Fetch it into /tmp/ne_countries.geojson before running.

Projection: Robinson (via pyproj), fitted to a 1600x940 viewBox.
Pure SVG (no scripts, no foreignObject) so GitHub renders it inline.
"""

import json
import math
import os
import sys

try:
    from pyproj import Transformer
except ImportError:
    sys.exit("pip install pyproj (in the Hermes venv)")

SRC = "/tmp/ne_countries.geojson"
OUT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "art", "generated", "gates-of-earth-2034.svg",
)
W, H = 1600, 940
PAD = 70

# ---------------------------------------------------------------- projection
_TRANS = Transformer.from_crs("EPSG:4326", "+proj=robin +lon_0=0 +R=6378137", always_xy=True)


def proj(lon, lat):
    x, y = _TRANS.transform(lon, lat)
    return x, y


def fit_points(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    scale = min((W - 2 * PAD) / (x1 - x0), (H - 2 * PAD) / (y1 - y0))
    ox = (W - (x1 - x0) * scale) / 2 - x0 * scale
    oy = (H - (y1 - y0) * scale) / 2 - y0 * scale
    return scale, ox, oy


SCALE, OX, OY = 0, 0, 0


def px(lon, lat):
    x, y = proj(lon, lat)
    # SVG y grows downward; projected y grows northward — invert.
    return round(OX + x * SCALE, 2), round(OY - y * SCALE, 2)


def simplify(ring, tol=0.35):
    """Point decimation on projected coords; keep ring closure."""
    out = [ring[0]]
    for p in ring[1:]:
        if (p[0] - out[-1][0]) ** 2 + (p[1] - out[-1][1]) ** 2 >= tol * tol:
            out.append(p)
    if out[0] != out[-1]:
        out.append(out[0])
    return out


def path_for_feature(feature, tol=0.35):
    geom = feature["geometry"]
    rings = []
    if geom["type"] == "Polygon":
        rings = geom["coordinates"]
    elif geom["type"] == "MultiPolygon":
        for poly in geom["coordinates"]:
            rings.extend(poly)
    parts = []
    for ring in rings:
        pts = [px(lon, lat) for lon, lat in ring]
        pts = simplify(pts, tol)
        if len(pts) < 4:
            continue
        d = "M" + "L".join(f"{x},{y}" for x, y in pts[1:])
        parts.append(f"M{pts[0][0]},{pts[0][1]}{d}Z")
    return "".join(parts)

# ---------------------------------------------------------------- styling
OCEAN = "#0a1220"
OCEAN_EDGE = "#0e1a2e"
GRID = "#14233c"
LAND = "#1e2a3d"
LAND_STROKE = "#33445e"
ANTARCTICA = "#26354c"
ANTARCTICA_STROKE = "#3d5378"
HOST = "#96692b"
HOST_STROKE = "#d4a952"
HOST_LABEL = "#e0c898"
COOP = "#2c4c74"
COOP_STROKE = "#5a8fc4"
COOP_LABEL = "#a9c6e8"
TEXT = "#e8eef7"
SUB = "#8fa3c0"
DIM = "#6d7f9c"
PANEL = "#0c1526"
PANEL_STROKE = "#2a3b58"
MARK_HALO = "#0a1220"

OPEN = "#ff6b4a"
OPEN_EDGE = "#ffb38f"
CONT = "#6ec3ff"
DEST = "#8b97a8"
DEST_FILL = "#4a5568"
BLACKBOX = "#b48cff"
DSITE = "#7d8da6"

FONT = "'Inter', 'Helvetica Neue', Helvetica, Arial, sans-serif"

# ---------------------------------------------------------------- country sets
# NAME values follow Natural Earth 110m admin_0 naming.
HOSTS = {
    "Russia", "Norway", "Ethiopia", "Iran", "Saudi Arabia",
    "Dem. Rep. Congo", "Peru", "Denmark", "Greenland",
}
EU27 = {
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia",
    "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
    "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
    "Netherlands", "Poland", "Portugal", "Romania", "Slovakia",
    "Slovenia", "Spain", "Sweden",
}
COOPS = EU27 | {"United States of America", "United Arab Emirates",
                "Qatar", "Djibouti"}

# ---------------------------------------------------------------- markers
# lon, lat, tag, kind (open|contained|blackbox|destroyed)
GATES = [
    (2.8, 61.3,   "G-01", "open"),
    (40.9, 13.8,  "G-02", "open"),
    (48.5, 32.5,  "G-03", "contained"),
    (51.0, 21.0,  "G-04", "contained"),
    (-26.5, 70.8, "G-05", "contained"),
    (160.0, -84.0, "G-06", "contained"),
    (130.0, 62.0, "G-07", "blackbox"),
    (24.5, -2.5,  "G-08", "contained"),
    (-75.5, -12.0, "G-09", "contained"),
    (60.5, 55.5,  "SCAR", "destroyed"),
    (10.0, 25.0,  "GLASS", "destroyed"),
]

DSITES = [
    # lon, lat, designation, name, dx, anchor
    (15.5, 55.5, "D-01", "The Sunken Church", 7, "start"),
    (9.5, 46.5,  "D-02", "The Fought-Back", 7, "start"),
    (-158.0, -8.0, "D-04", "The Lagoon Arch", 7, "start"),
    (105.0, 42.5, "D-06", "The Gobi Anomaly", 7, "start"),
    (-89.0, 20.5, "D-07", "The Cenote", 7, "start"),
    (-5.2, 50.2,  "D-08", "The Knocking Mine", -14, "end"),
]

# register rows: (code, name, line2, kind)
REGISTER = [
    ("G-01", "ALPHA — THE DEEP GATE", "Norwegian Trench · 50 m — the European pillar · OPEN", "open"),
    ("G-02", "BRAVO — THE SALT GATE", "Danakil, Ethiopia — US-led, Gulf partners · OPEN", "open"),
    ("G-03", "CHARLIE — THE ZAGROS GATE", "Iran — the gate politics saved", "contained"),
    ("G-04", "DELTA — THE DUNE GATE", "Rub' al Khali, Saudi Arabia", "contained"),
    ("G-05", "ECHO — THE ICE GATE", "Greenland — 800 m under the ice", "contained"),
    ("G-06", "FOXTROT — THE WHITE GATE", "Antarctica — sealed, watched", "contained"),
    ("G-07", "GOLF — THE MINE GATE", "Siberia — BLACK BOX · status unknown", "blackbox"),
    ("G-08", "HOTEL — THE JUNGLE GATE", "Congo Basin — the horde in the bush", "contained"),
    ("G-09", "INDIA — THE HIGH GATE", "Peru — a window at 4,700 m", "contained"),
    ("—", "THE URAL SCAR", "Russia — nuked 24 Oct 2031", "destroyed"),
    ("—", "THE SAHARAN GLASS", "North Africa — nuked 11 Dec 2031", "destroyed"),
]

# country labels: lon, lat, text, anchor, class
COUNTRY_LABELS = [
    (96.0, 61.0, "RUSSIA", "middle", "host"),
    (8.5, 64.0, "NORWAY", "middle", "host"),
    (36.5, 7.5, "ETHIOPIA", "middle", "host"),
    (59.0, 30.5, "IRAN", "middle", "host"),
    (23.5, 0.5, "DEM. REP. CONGO", "middle", "host"),
    (-72.0, -12.0, "PERU", "middle", "host"),
    (-48.0, 75.5, "GREENLAND", "middle", "host"),
    (-101.0, 38.0, "UNITED STATES", "middle", "coop"),
    (9.0, 49.3, "EUROPEAN UNION", "middle", "eu"),
    (45.2, 12.8, "DJIBOUTI", "start", "coop_small"),
    (52.5, 27.5, "GULF PARTNERS", "start", "coop_small"),
    (75.0, -78.0, "ANTARCTICA — NO STATE CLAIMS IT", "middle", "dim"),
]

# ---------------------------------------------------------------- svg helpers
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fmt(n):
    s = f"{n:.2f}"
    return s.rstrip("0").rstrip(".")


def text(x, y, s, size, fill, anchor="start", weight=400, spacing=0.0, opacity=1.0):
    return (f'<text x="{fmt(x)}" y="{fmt(y)}" font-family="{FONT}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" '
            f'letter-spacing="{spacing}" opacity="{opacity}">{esc(s)}</text>')


def build_graticule():
    out = []
    for lon in range(-150, 151, 30):
        pts = [px(lon, lat) for lat in range(-90, 91, 2)]
        out.append("M" + "L".join(f"{x},{y}" for x, y in pts))
    for lat in range(-60, 61, 30):
        pts = [px(lon, lat) for lon in range(-180, 181, 2)]
        out.append("M" + "L".join(f"{x},{y}" for x, y in pts))
    return "".join(
        f'<path d="{d}" stroke="{GRID}" stroke-width="0.8" fill="none"/>' for d in out)


# ---------------------------------------------------------------- QA mode
def _in_ring(lon, lat, ring):
    """Ray casting against one closed ring of [lon, lat] pairs."""
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if (yi > lat) != (yj > lat) and \
           lon < (xj - xi) * (lat - yi) / (yj - yi + 1e-12) + xi:
            inside = not inside
        j = i
    return inside


def qa(data):
    """Deterministic QA: gate placement vs real countries + label collisions."""
    print("=== gate placement (point-in-polygon vs Natural Earth 110m) ===")
    exteriors = []  # (name, ring) — exterior ring only
    for f in data["features"]:
        name = f["properties"].get("NAME", "")
        geom = f["geometry"]
        if geom["type"] == "Polygon":
            exteriors.append((name, geom["coordinates"][0]))
        elif geom["type"] == "MultiPolygon":
            for poly in geom["coordinates"]:
                exteriors.append((name, poly[0]))

    def host_country(lon, lat):
        hits = []
        for name, ring in exteriors:
            if _in_ring(lon, lat, ring):
                hits.append(name)
        return hits

    for lon, lat, tag, kind in GATES:
        print(f"  {tag:6s} ({lon:7.1f}, {lat:6.1f}) -> {host_country(lon, lat) or 'OCEAN'}")
    for lon, lat, desig, name, dx, anchor in DSITES:
        print(f"  {desig:6s} ({lon:7.1f}, {lat:6.1f}) -> {host_country(lon, lat) or 'OCEAN'}  ({name})")

    print("=== label collision check (estimated text boxes) ===")
    boxes = []  # (label, x0, y0, x1, y1)

    def add_box(tag_s, lon, lat, size, anchor, weight=600, spacing=0.0, dy=0.0,
                dx=0.0):
        x, y = px(lon, lat)
        x += dx
        y += dy
        w = len(tag_s) * size * 0.62 + spacing * max(len(tag_s) - 1, 0)
        h = size
        if anchor == "middle":
            x0, x1 = x - w / 2, x + w / 2
        elif anchor == "end":
            x0, x1 = x - w, x
        else:
            x0, x1 = x, x + w
        boxes.append((tag_s, x0, y - h, x1, y + h * 0.35))

    for lon, lat, s, anchor, cls in COUNTRY_LABELS:
        size = {"host": 10.5, "coop": 10.5, "eu": 9.5, "coop_small": 9,
                "dim": 9.5}[cls]
        spacing = 1.6 if cls in ("host", "coop") else 1.2 if cls == "eu" \
            else 1.2 if cls == "coop_small" else 1.4
        add_box(s, lon, lat, size, anchor, 600, spacing)
    for lon, lat, desig, name, dx, anchor in DSITES:
        add_box(desig, lon, lat, 8, anchor, 500, 1, dx=dx, dy=3)
    for lon, lat, tag, kind in GATES:
        add_box(tag, lon, lat, 9.5, "middle", 700, 1.2, dy=14)
    # pillar banners (single line each)
    for lon, lat, line in ((2.0, 73.0, "THE EUROPEAN PILLAR"),
                           (49.0, 23.5, "THE AMERICAN PILLAR")):
        add_box(line, lon, lat, 11, "middle", 700, 2.2)

    n_over = 0
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, b = boxes[i], boxes[j]
            if not (a[4] < b[2] or b[4] < a[2] or a[3] < b[1] or b[3] < a[1]):
                print(f"  OVERLAP: '{a[0]}' vs '{b[0]}'")
                n_over += 1
    print(f"  {len(boxes)} labels checked, {n_over} overlaps")

    print("=== marker bounds ===")
    for lon, lat, tag, kind in GATES:
        x, y = px(lon, lat)
        flag = "" if (PAD - 20 < x < W - PAD + 20 and 40 < y < H - 20) else "  <-- OUT OF CANVAS"
        print(f"  {tag:6s} at ({x:7.1f}, {y:7.1f}){flag}")


def glyph(x, y, kind, r=5.5):
    g = []
    if kind == "open":
        g.append(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="15" fill="{OPEN}" opacity="0.16"/>')
        g.append(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="9.5" fill="none" stroke="{OPEN_EDGE}" stroke-width="1.4" opacity="0.9"/>')
        g.append(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="{r}" fill="{OPEN}" stroke="{MARK_HALO}" stroke-width="1.4"/>')
        g.append(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="1.8" fill="#fff"/>')
    elif kind == "contained":
        g.append(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="{r}" fill="#0e2238" stroke="{CONT}" stroke-width="2"/>')
        g.append(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="1.6" fill="{CONT}"/>')
    elif kind == "blackbox":
        g.append(f'<rect x="{fmt(x-4)}" y="{fmt(y-4)}" width="8" height="8" fill="#221140" stroke="{BLACKBOX}" stroke-width="1.6"/>')
    elif kind == "destroyed":
        g.append(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="{r}" fill="{DEST_FILL}" stroke="{DEST}" stroke-width="1.5"/>')
        g.append(f'<line x1="{fmt(x-2.8)}" y1="{fmt(y-2.8)}" x2="{fmt(x+2.8)}" y2="{fmt(y+2.8)}" stroke="{DEST}" stroke-width="1.8"/>')
        g.append(f'<line x1="{fmt(x+2.8)}" y1="{fmt(y-2.8)}" x2="{fmt(x-2.8)}" y2="{fmt(y+2.8)}" stroke="{DEST}" stroke-width="1.8"/>')
    return "".join(g)


def main():
    global SCALE, OX, OY
    data = json.load(open(SRC))
    feats = data["features"]

    for f in feats:
        geom = f["geometry"]
        if geom["type"] == "Polygon":
            for ring in geom["coordinates"]:
                f.setdefault("_pts", []).extend(proj(lon, lat) for lon, lat in ring)
        elif geom["type"] == "MultiPolygon":
            for poly in geom["coordinates"]:
                for ring in poly:
                    f.setdefault("_pts", []).extend(proj(lon, lat) for lon, lat in ring)

    SCALE, OX, OY = fit_points([p for f in feats for p in f["_pts"]])

    if "--qa" in sys.argv:
        qa(data)
        return

    groups = {"host": [], "coop": [], "land": [], "antarctica": []}
    for f in feats:
        name = f["properties"].get("NAME", "")
        d = path_for_feature(f)
        if not d:
            continue
        if name in HOSTS:
            groups["host"].append(d)
        elif name in COOPS:
            groups["coop"].append(d)
        elif name == "Antarctica":
            groups["antarctica"].append(d)
        else:
            groups["land"].append(d)

    def land_paths(entries, fill, stroke, sw):
        return "".join(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'fill-rule="evenodd"/>' for d in entries)

    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
                 f'width="{W}" height="{H}" font-family="{FONT}">')
    parts.append(f'<defs><radialGradient id="sea" cx="50%" cy="46%" r="75%">'
                 f'<stop offset="0%" stop-color="{OCEAN_EDGE}"/>'
                 f'<stop offset="100%" stop-color="{OCEAN}"/></radialGradient></defs>')
    parts.append(f'<rect width="{W}" height="{H}" fill="url(#sea)"/>')
    parts.append(build_graticule())
    parts.append(land_paths(groups["antarctica"], ANTARCTICA, ANTARCTICA_STROKE, 1))
    parts.append(land_paths(groups["land"], LAND, LAND_STROKE, 0.75))
    parts.append(land_paths(groups["coop"], COOP, COOP_STROKE, 0.9))
    parts.append(land_paths(groups["host"], HOST, HOST_STROKE, 0.9))

    # country labels
    for lon, lat, s, anchor, cls in COUNTRY_LABELS:
        x, y = px(lon, lat)
        if cls == "host":
            fill, size, w, sp = HOST_LABEL, 10.5, 600, 1.6
        elif cls == "coop":
            fill, size, w, sp = COOP_LABEL, 10.5, 600, 1.6
        elif cls == "eu":
            fill, size, w, sp = COOP_LABEL, 9.5, 600, 1.2
        elif cls == "coop_small":
            fill, size, w, sp = COOP_LABEL, 9, 500, 1.2
        else:
            fill, size, w, sp = DIM, 9.5, 500, 1.4
        parts.append(text(x, y, s, size, fill, anchor, w, sp))

    # D-sites
    for lon, lat, desig, name, dx, anchor in DSITES:
        x, y = px(lon, lat)
        parts.append(f'<path d="M{fmt(x)},{fmt(y-3.6)}L{fmt(x+3.6)},{fmt(y)}'
                     f'L{fmt(x)},{fmt(y+3.6)}L{fmt(x-3.6)},{fmt(y)}Z" fill="none" '
                     f'stroke="{DSITE}" stroke-width="1.1"/>')
        parts.append(text(x + dx, y + 3, desig, 8, DSITE, anchor, 500, 1))

    # gates: glyph + tiny tag
    for lon, lat, tag, kind in GATES:
        x, y = px(lon, lat)
        parts.append(f'<g>{glyph(x, y, kind)}')
        parts.append(text(x, y + 14, tag, 9.5, TEXT, "middle", 700, 1.2))
        parts.append("</g>")

    # pillar banners (single line each, in empty sea/desert) — lon, lat
    for lon, lat, line in ((2.0, 73.0, "THE EUROPEAN PILLAR"),
                           (49.0, 23.5, "THE AMERICAN PILLAR")):
        bx, by = px(lon, lat)
        parts.append(text(bx, by, line, 11, OPEN_EDGE, "middle", 700, 2.2))

    # ---- title block
    parts.append(text(44, 52, "THE REOPENING", 34, TEXT, "start", 700, 8))
    parts.append(text(45, 74, "GATES OF EARTH — SITUATION MAP · 2034", 13.5, SUB, "start", 600, 4))
    parts.append(text(45, 90, "JOINT PORTAL COMMAND · PUBLIC BRIEFING · ROBINSON PROJECTION", 9.5, DIM, "start", 500, 2.4))
    # compass
    cx, cy = W - 60, 56
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="none" stroke="{SUB}" stroke-width="1" opacity="0.8"/>')
    parts.append(f'<line x1="{cx}" y1="{cy+18}" x2="{cx}" y2="{cy-18}" stroke="{SUB}" stroke-width="1.2" opacity="0.8"/>')
    parts.append(f'<polygon points="{cx},{cy-22} {cx-4.5},{cy-12} {cx+4.5},{cy-12}" fill="{OPEN}"/>')
    parts.append(text(cx, cy + 36, "N", 12, SUB, "middle", 600, 1))

    # ---- gate register (bottom-left)
    rx, ry, rw = 44, 556, 356
    rh = 30 + len(REGISTER) * 26 + 12
    parts.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="6" '
                 f'fill="{PANEL}" stroke="{PANEL_STROKE}" stroke-width="1" opacity="0.94"/>')
    parts.append(text(rx + 16, ry + 26, "GATE REGISTER — THE 47", 11, SUB, "start", 700, 3))
    y = ry + 48
    for code, name, line2, kind in REGISTER:
        chip = {"open": OPEN, "contained": CONT, "blackbox": BLACKBOX,
                "destroyed": DEST}[kind]
        parts.append(f'<rect x="{rx+16}" y="{y-12}" width="9" height="9" rx="1.5" fill="{chip}" opacity="0.9"/>')
        head = f'{code}  {name}' if code != "—" else name
        parts.append(text(rx + 34, y, head, 10.5, TEXT, "start", 600, 0.8))
        parts.append(text(rx + 34, y + 13, line2, 8.5, SUB, "start", 400, 0.4))
        y += 26

    # ---- legend (bottom-right)
    lx, ly = W - 330, H - 270
    rows = [
        ("swatch", HOST, HOST_STROKE, "Gate host nation (8 of 9 surviving gates; Russia hosts two)"),
        ("swatch", COOP, COOP_STROKE, "Cooperating nation — EU-27 · US · Gulf partners · Djibouti"),
        ("glyph", "open", None, "Open gate — held two-way (2)"),
        ("glyph", "contained", None, "Contained gate (6)"),
        ("glyph", "blackbox", None, "Black box — status unknown (1)"),
        ("glyph", "destroyed", None, "Destroyed gate (2)"),
        ("glyph", "dsite", None, "Dormant anchor — D-site (6 of the 38 that never woke)"),
    ]
    parts.append(f'<rect x="{lx}" y="{ly}" width="322" height="{34 + len(rows) * 27 + 10}" '
                 f'rx="6" fill="{PANEL}" stroke="{PANEL_STROKE}" stroke-width="1" opacity="0.94"/>')
    parts.append(text(lx + 16, ly + 26, "LEGEND", 11, SUB, "start", 700, 3))
    y = ly + 52
    for kind, a, b, label in rows:
        if kind == "swatch":
            parts.append(f'<rect x="{lx+16}" y="{y-9}" width="16" height="10" rx="2" fill="{a}" stroke="{b}" stroke-width="0.8"/>')
        elif a == "open":
            parts.append(f'<circle cx="{lx+24}" cy="{y-4}" r="5.5" fill="{OPEN}" stroke="{MARK_HALO}" stroke-width="1.2"/>')
        elif a == "contained":
            parts.append(f'<circle cx="{lx+24}" cy="{y-4}" r="5" fill="#0e2238" stroke="{CONT}" stroke-width="1.8"/>')
        elif a == "blackbox":
            parts.append(f'<rect x="{lx+20}" y="{y-9}" width="8" height="8" fill="#221140" stroke="{BLACKBOX}" stroke-width="1.4"/>')
        elif a == "destroyed":
            parts.append(f'<circle cx="{lx+24}" cy="{y-4}" r="5" fill="{DEST_FILL}" stroke="{DEST}" stroke-width="1.3"/>')
            parts.append(f'<line x1="{lx+21.2}" y1="{y-6.8}" x2="{lx+26.8}" y2="{y-1.2}" stroke="{DEST}" stroke-width="1.5"/>')
            parts.append(f'<line x1="{lx+26.8}" y1="{y-6.8}" x2="{lx+21.2}" y2="{y-1.2}" stroke="{DEST}" stroke-width="1.5"/>')
        elif a == "dsite":
            parts.append(f'<path d="M{lx+24},{y-8.6}L{lx+27.6},{y-4}L{lx+24},{y+0.6}L{lx+20.4},{y-4}Z" fill="none" stroke="{DSITE}" stroke-width="1.1"/>')
        parts.append(text(lx + 42, y, label, 10.5, "#b9c6da", "start", 400, 0.2))
        y += 27

    # ---- footer counts
    foot = ("THE 47 — 2 HELD · 6 CONTAINED · 1 BLACK BOX · 1 DORMANT · 2 NUKED · 35 DESTROYED   |   "
            "THE LATTICE — 85 ANCHORS · 9 DENIED · 6 D-SITES · 2 MISSING")
    parts.append(text(W / 2, H - 22, foot, 9.5, DIM, "middle", 500, 1.2))

    parts.append("</svg>")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("".join(parts))
    print(f"wrote {OUT} ({os.path.getsize(OUT) // 1024} KB)")


if __name__ == "__main__":
    main()
