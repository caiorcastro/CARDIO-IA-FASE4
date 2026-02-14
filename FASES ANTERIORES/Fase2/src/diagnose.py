
import csv, re, json
from collections import Counter, defaultdict
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def normalize(text: str) -> str:
    return re.sub(r"[^a-zà-ú0-9\s]", " ", text.lower())

def load_knowledge_map(path: Path):
    rules = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            s1 = normalize(row["Sintoma 1"]).strip()
            s2 = normalize(row["Sintoma 2"]).strip()
            disease = row["Doença Associada"].strip()
            rules.append((s1, s2, disease))
    return rules

def match_sentence(sentence: str, rules):
    s = normalize(sentence)
    matches = []
    for s1, s2, disease in rules:
        cond1 = s1 in s if s1 else True
        cond2 = s2 in s if s2 else True
        if cond1 and cond2:
            matches.append((disease, (s1, s2)))
    return matches

def suggest_diagnosis(sentence: str, rules):
    matches = match_sentence(sentence, rules)
    disease_counter = Counter([d for d,_ in matches])
    if not disease_counter:
        return {"disease": "Indefinido", "matched": [], "confidence": 0.0}
    top_disease, count = disease_counter.most_common(1)[0]
    matched_pairs = [m for d,m in matches if d == top_disease]
    # Confidence: capped by number of unique matching pairs for that disease
    unique_pairs = set(matched_pairs)
    confidence = min(1.0, len(unique_pairs) / 3.0)
    return {"disease": top_disease, "matched": sorted(unique_pairs), "confidence": round(confidence, 2)}

def heuristic_risk(sentence: str) -> str:
    s = normalize(sentence)
    high_terms = ["dor no peito", "aperto no tórax", "falta de ar", "suor frio", "náusea", "tontura", "desmaio", "irradia", "mandíbula", "braço", "pressão muito alta"]
    score = sum(1 for t in high_terms if t in s)
    return "alto risco" if score >= 2 or ("dor no peito" in s and "falta de ar" in s) else "baixo risco"

def main():
    rules = load_knowledge_map(DATA_DIR / "knowledge_map.csv")
    sentences = [line.strip() for line in open(DATA_DIR / "symptom_sentences_pt.txt", encoding="utf-8") if line.strip()]
    out_rows = []
    for sent in sentences:
        sug = suggest_diagnosis(sent, rules)
        risk = heuristic_risk(sent)
        out_rows.append({
            "frase": sent,
            "diagnostico_sugerido": sug["disease"],
            "sintomas_casados": json.dumps(sug["matched"], ensure_ascii=False),
            "confianca": sug["confidence"],
            "risco_heuristico": risk
        })
    out_csv = DATA_DIR / "diagnosticos_gerados.csv"
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)
    print(f"Diagnósticos salvos em: {out_csv}")

if __name__ == "__main__":
    main()
