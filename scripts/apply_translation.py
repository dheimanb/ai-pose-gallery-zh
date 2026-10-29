# -*- coding: utf-8 -*-
"""把日文數據回填為繁中：生成 data/pose-zh-TW.json / meta-zh-TW.json / translations-tw.csv

用法（在仓库根目录）: python3 scripts/apply_translation.py
"""
import csv
import json
import os
import sys
from collections import Counter

import i18n

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

with open(os.path.join(DATA, "pose.json"), encoding="utf-8") as f:
    data = json.load(f)
with open(os.path.join(DATA, "meta.json"), encoding="utf-8") as f:
    meta = json.load(f)

maps = {
    "系統": i18n.SYSTEM,
    "分類": i18n.CATEGORY,
    "アングル": i18n.ANGLE,
    "ポーズ名": i18n.POSE,
}

missing = {k: sorted({x.get(k) for x in data} - set(m)) for k, m in maps.items()}
bad = {k: v for k, v in missing.items() if v}
if bad:
    print("!! 缺少譯詞：")
    for k, v in bad.items():
        for s in v:
            print(f"  [{k}] {s}")
    sys.exit(1)

# 繁中鍵名版本
out = []
for x in data:
    out.append({
        "id": x["id"],
        "體系": i18n.SYSTEM[x["系統"]],
        "姿勢編號": x["ポーズ番号"],
        "分類": i18n.CATEGORY[x["分類"]],
        "姿勢名稱": i18n.POSE[x["ポーズ名"]],
        "角度": i18n.ANGLE[x["アングル"]],
        "縮略圖": x["サムネ"],
        "原圖": x["原寸"],
        "檢索": f'{x["id"]} {i18n.SYSTEM[x["系統"]]}{i18n.CATEGORY[x["分類"]]}{i18n.POSE[x["ポーズ名"]]}{i18n.ANGLE[x["アングル"]]}',
    })
with open(os.path.join(DATA, "pose-zh-TW.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

with open(os.path.join(DATA, "meta-zh-TW.json"), "w", encoding="utf-8") as f:
    json.dump({"體系分類": [i18n.SYSTEM[s] for s in meta["lines"]]}, f, ensure_ascii=False, indent=2)

# 保留日文原值的對照表（前端可做 hover 對照）
with open(os.path.join(DATA, "translations-tw.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(["字段", "日文原文", "繁中譯文", "出现次数"])
    for k in ["系統", "分類", "角度", "ポーズ名"]:
        field = {"系統": "系統", "分類": "分類", "角度": "アングル", "ポーズ名": "ポーズ名"}[k]
        cnt = Counter(x[field] for x in data)
        for jp in sorted(maps[field]):
            w.writerow([k, jp, maps[field][jp], cnt[jp]])

print("OK 記錄數:", len(out))
print("唯一譯詞:", sum(len(m) for m in maps.values()))
