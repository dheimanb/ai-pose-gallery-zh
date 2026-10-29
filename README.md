# AI Pose Gallery · 繁中版

> 288 組 / 1439 張 AI 人體姿勢參考圖，日文數據完整翻譯為繁體中文，附可直接部署的響應式靜態畫廊。

![畫廊預覽](docs/preview.jpg)

<details><summary>手機端預覽</summary>

![手機端預覽](docs/mobile.jpg)

</details>

**在線演示：** 尚未部署（待接駁 Cloudflare Pages；部署完成後補上正式網址）
**原始站點：** <https://ai-pose-gallery.pages.dev/>
**原作者：** ギア（@giaaibusi）
**簡體中文版維護：** Anhao · [X @anhao_ai](https://x.com/anhao_ai)
**繁中版維護：** dheimanb（本倉庫為繁中版 fork，源自 anhao 的簡體中文版）
**GitHub：** <https://github.com/dheimanb/ai-pose-gallery-zh>

---

## 這是什麼

原站是一套面向 AI 繪畫 / 3D / 攝影參考的姿勢圖庫，元數據全部為日文，且不提供批量素材下載。本倉庫做了三件事：

1. **全量鏡像** —— 1439 條記錄對應的 1439 張縮略圖（JPG 300×400）與 1439 張原圖（PNG 900×1200）全部落地，共 2878 個文件 / 659.5 MB。
2. **完整繁中化** —— 日文字段逐條譯為繁體中文，覆蓋 4 個體系、26 個分類、288 個姿勢名、5 個視角，零遺漏。繁中譯文由簡體譯文經 OpenCC 機械轉換，未經逐條人手校對；譯文如有問題，歡迎開 Issue 指正。
3. **可用的前端** —— 零依賴響應式畫廊，完整實現原站的分類篩選、多角度切換、分組瀏覽、燈箱導航與原圖下載，並針對手機重新設計佈局；頂部可切換繁中／日文資料（介面文字維持繁中）。

## 頁面功能

- 4 個體系頁籤，顯示各體系的圖片數與姿勢組數
- 姿勢名、編號、ID、分類關鍵詞搜索，支持 `/` 快速聚焦
- 動作分類、5 種視角組合篩選，可一鍵重置
- **按姿勢分組 / 逐張瀏覽**雙模式，分組卡片帶多角度縮略圖
- 懸停或點擊縮略圖切換主圖角度，點擊卡片打開燈箱
- 燈箱先顯示縮略圖、再加載 900×1200 原圖，支持直接下載 PNG、複製 ID、新窗口打開
- `← / →` 切換角度，`↑ / ↓` 切換姿勢，`Esc` 關閉；手機支持左右滑動
- PC 多列網格、手機雙列網格，移動端篩選面板可展開/收起
- 繁中／日文資料切換（頁首語言切換鈕；日文顯示原始日文數據）
- 使用指南與注意事項彈窗，頁腳標註圖片來源與維護者連結

## SEO 與分享

頁面內置了完整的 SEO 與社交分享配置：

- 關鍵詞化標題：`AI 姿勢參考庫｜288 組人體姿勢 · 1439 張多角度參考圖`
- 獨立 description、keywords、author 與 `max-image-preview:large`
- `canonical` 目前使用相對路徑，正式域名確定後改為絕對地址，避免自定義域名與 pages.dev 域名重複收錄
- Open Graph / Twitter Card 使用 1200×630 的 `og-cover.jpg`（目前為相對路徑，正式域名確定後改回絕對地址）
- JSON-LD 結構化數據：`WebSite` + `ImageGallery`，聲明語言（zh-TW）、簡介與頁面主圖
- `robots.txt` 放行全站（Sitemap 行待正式域名確定後補上），`sitemap.xml` 指向首頁（loc 目前為相對路徑，待補正式域名）
- 語義結構：單一 H1、分區 H2、卡片 H3；縮略圖 `alt` 含姿勢名與視角，圖片懶加載

## 數據規模

| 體系 | 條數 |
| --- | ---: |
| 全身單人・標準系 | 365 |
| 全身單人・性感系 | 399 |
| 上半身單人 | 400 |
| 雙人纏綿 | 275 |
| **合計** | **1439** |

每條記錄對應 5 個視角中的若干個：正面 / 斜側 / 側面 / 俯視 / 仰視。

## 目錄結構

```
.
├── index.html              # 單頁畫廊（零依賴，直接打開即可）
├── robots.txt              # 搜索引擎抓取規則
├── sitemap.xml             # 站點地圖
├── og-cover.jpg            # 1200×630 社交分享封面
├── data/
│   ├── pose.json           # 原始日文數據（1439 條，未改動；頁面日文模式讀取）
│   ├── pose-zh-TW.json     # 繁中數據（前端預設讀取，含檢索字段）
│   ├── meta.json           # 原始體系分類
│   ├── meta-zh-TW.json     # 繁中體系分類
│   └── translations-tw.csv # 日⇄繁對照表（323 條，便於校對）
├── thumbs/                 # 縮略圖 1439 張 JPG 300×400（22 MB）
├── img/                    # 原圖 1439 張 PNG 900×1200（637 MB）
├── scripts/
│   ├── download.py         # 並發下載器（48 線程 / 斷點續傳 / 自動重試）
│   ├── i18n.py             # 日譯繁詞典（唯一值去重後的 323 條譯文）
│   ├── apply_translation.py# 回填譯文，生成繁中數據
│   ├── verify.py           # 校驗文件完整性（存在性 / 大小 / 圖片頭）
│   └── build.sh            # 生成 Cloudflare Pages 發佈目錄 dist/
├── docs/                   # README 頁面預覽圖
├── _headers                # Cloudflare Pages 緩存策略
├── LICENSE
└── README.md
```

## 數據結構

`data/pose-zh-TW.json` 字段說明：

| 字段 | 原日文字段 | 示例 | 說明 |
| --- | --- | --- | --- |
| `id` | — | `full_sexy_P001_front` | 唯一標識 |
| `體系` | `系統` | 全身單人・性感系 | 4 大類 |
| `姿勢編號` | `ポーズ番号` | `P001` | 80 組編號 |
| `分類` | `分類` | 站姿 | 26 類動作 |
| `姿勢名稱` | `ポーズ名` | S形站姿・胯部側頂 | 288 種描述 |
| `角度` | `アングル` | 正面 | 5 種視角 |
| `縮略圖` | `サムネ` | `thumbs/…jpg` | 相對路徑 |
| `原圖` | `原寸` | `img/…png` | 相對路徑 |
| `檢索` | — | 拼接串 | 供前端模糊搜索 |

原始日文數據 `data/pose.json` 保持原樣，字段名與站點接口一致，便於對照或回灌；頁面切換至日文時直接讀取該文件。

## 本地預覽

畫廊通過 `fetch` 讀取 JSON，需要 HTTP 環境（直接雙擊 `index.html` 會被 CORS 攔截）：

```bash
python3 -m http.server 8000
# 打開 http://127.0.0.1:8000
```

頁面支持體系/分類/視角組合篩選、關鍵詞搜索、分組與逐張瀏覽、多角度縮略圖、懶加載、燈箱原圖下載、鍵盤與觸屏導航、繁中／日文資料切換。

## 腳本用法

```bash
# 重新拉取全部圖片（已存在的文件自動跳過，可反覆執行）
python3 scripts/download.py
WORKERS=64 python3 scripts/download.py   # 調整並發

# 修改 scripts/i18n.py 中的譯文後，重新生成繁中數據
python3 scripts/apply_translation.py

# 校驗 2878 個文件是否完整
python3 scripts/verify.py
```

## 部署到 Cloudflare Pages

倉庫為純靜態站點，無框架、無依賴。

**方式一：GitHub 自動部署（推薦）**

1. 登錄 Cloudflare Dashboard → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**
2. 選擇本倉庫 → 生產分支 `main`
3. 構建設置照抄：

   | 字段 | 值 |
   | --- | --- |
   | Framework preset | `None` |
   | Build command | `bash scripts/build.sh` |
   | Build output directory | `dist` |

4. **Save and Deploy**，約 2–5 分鐘得到 `https://<project>.pages.dev`
5. 之後每次 `git push` 自動重新發佈

> ⚠️ **不要**把 Build output directory 直接填 `/`。倉庫根目錄含 `.git`（數百 MB），
> Cloudflare 會把它當靜態資源掃描，pack 文件超過 25 MiB 單文件限制會導致構建失敗。
> `scripts/build.sh` 只拷貝 `index.html`、`_headers`、`data/`、`thumbs/`、`img/` 到 `dist/`。
> 若確實想用根目錄，倉庫已附 `.assetsignore` 兜底排除非站點文件。

> 站點限制：單文件 ≤ 25 MiB、每次部署 ≤ 20,000 個文件。本倉庫最大文件 917 KB、共 2883 個文件，均在限制內。

**方式二：命令行直傳**

```bash
bash scripts/build.sh
npx wrangler pages deploy dist --project-name ai-pose-gallery-zh
```

`_headers` 已為 `img/`、`thumbs/` 配置一年期強緩存，圖片不會重複回源。

部署完成、正式域名確定後，將 `index.html` 的 canonical、`og:*`、`twitter:*`、JSON-LD，以及 `robots.txt` 的 Sitemap 行、`sitemap.xml` 的 loc 由相對路徑改為正式域名的絕對地址。

## 內容提示

圖庫包含成人向姿勢參考（部分分類名稱涉及性行為術語），僅供藝術創作、動作參考與前端技術學習使用。請勿用於違法用途。未成年人請勿訪問。

## 版權與致謝

- **圖片與原始數據的著作權歸原作者ギア所有**，來源地址見頁首
- 本倉庫為繁中版 fork，源自 anhao 的簡體中文版，僅為個人學習、繁中化與靜態站點實踐存檔，屬**非商業鏡像**，**不對圖片主張任何權利**，也不構成對原作品的商業使用授權
- 若原作者認為本倉庫侵犯其權益，請通過 Issue 聯繫，將立即刪除相關內容
- `scripts/` 與 `index.html` 的代碼以 MIT 協議開源（見 [LICENSE](LICENSE)），該協議**不覆蓋** `img/`、`thumbs/` 與 `data/` 中的圖片和原始數據
