# Elizabethtown, KY — Source Inventory

**Status:** Phase 0.1 in progress.  
**Last updated:** 2026-09-29  
**Primary site:** https://www.elizabethtownky.org  
**City Clerk:** Jessica Graham (City Clerk / ABC Administrator)  
**Open Records:** City of Elizabethtown, 200 West Dixie Ave., Elizabethtown, KY 42701 — 270-765-6121 (form at elizabethtownky.org/request-for-open-record)

This inventory lists the public document sources for the pilot. Each entry records the canonical URL, format, coverage, and notes for ingestion. Prefer linking to canonical sources; mirror only when it adds stability.

---

## 1. City Council — Agendas & Minutes (primary target)

**Page:** https://www.elizabethtownky.org/government/city_clerk/meeting_minutes_/  
**Storage pattern:** `/Documents/Government/Agenda and Minutes/[Year]/...`  
**Formats:** PDF, DOCX, DOCX.PDF (timestamped query params, e.g. `?t=...`)  
**Meeting cadence:** Regular meetings 1st & 3rd Mondays, work sessions 2nd & 4th Mondays, 4:30 p.m., Council Chambers, 212 West Dixie Ave.

| Year | Coverage on page | Notes |
|------|------------------|-------|
| 2026 | Apr–Sep (partial); ~28 entries incl. notices/work sessions | Gaps Jan–Mar; minutes posted for several regular/special meetings. Sample: `.../Minutes 2026 Council/MINUTES 2026-09-14 SPECIAL MEETING.docx.pdf` |
| 2025 | Only Jan 13 & Jan 21 listed | Likely incomplete listing or older archive elsewhere. |
| 2024 & prior | Not listed on this page | Older minutes exist in `wp-content/uploads/` (e.g. Planning Commission) and possibly other folders; needs deeper crawl or clerk request. |

**Video archive (audio/video path):** YouTube playlist "City Council Meetings | Elizabethtown, KY" — https://www.youtube.com/playlist?list=PLhVkHi5RhvS8JXv6XGDVsfvd639uHGhIp (~448 videos, back to at least 2020). Channel: City of Elizabethtown. Useful for Phase 5 transcription.

**Action:** Crawl the Documents folder for 2024–2026; request missing 2025/earlier minutes from the clerk.

---

## 2. City Ordinances

**Page:** https://www.elizabethtownky.org/government/city_clerk/city_ordinances.php  
**Storage pattern:** `/Documents/Government/Mayor and City Council/Ordinances/[YEAR]/ORD_[YEAR]-[N]_[desc].pdf`  
**Format:** PDF / DOCX.PDF  
**Coverage:** 2026 (17 ordinances, #01–#17), 2025 (31, #01–#31); "2024 & prior" links to external code library (American Legal Publishing: https://codelibrary.amlegal.com/codes/elizabethtownky/latest/elizabethtown_ky).  
**Note:** Hosted code may lag official printed copy — verify with clerk for authoritative versions.

---

## 3. Municipal Orders

**Page:** https://www.elizabethtownky.org/government/city_clerk/municipal_orders.php  
**Storage pattern:** `/Documents/Government/Mayor and City Council/Municipal Orders/[year]/...`  
**Format:** PDF  
**Coverage:** 2023–2026 (hundreds of orders, e.g. #01-2026 through #75-2026). Lower priority than minutes/ordinances for Phase 1.

---

## 4. Boards & Commissions (secondary)

| Body | Page | Coverage | Notes |
|------|------|----------|-------|
| Board of Zoning Adjustment | https://www.elizabethtownky.org/government/boards_commissioners/board_of_zoning_adjustment.php | 2022–2026 | Agendas + minutes; good secondary source. |
| Planning Commission | https://www.elizabethtownky.org/government/boards_commissioners/planning_commission.php | 2024–2026 (minutes); agendas in wp-content/uploads | Minutes often combined agenda+minutes PDFs. |
| Historic Preservation, Code Enforcement | public_notices.php | As needed | Sparse. |

---

## 5. Permits & Planning

**Online Permit Center:** https://ci-elizabethtown-ky.smartgovcommunity.com/  
**Type:** SmartGov community portal (MCCI).  
**Available:** Construction, demolition, electrical, fire alarm, sprinkler, sign, pool, temporary banner/structure; Planning Commission & BZA applications.  
**Public data:** No public search/export of issued permits visible; account-based. Contact: emily.prather-rodgers@elizabethtownky.gov, 270-982-3266.  
**Phase:** 3.

**Planning & Development:** https://elizabethtownky.org/planning-development-department  
Staff: Jeff Camp (Building Official), Hadley Ford / Cristy Keegan (Permit Clerks).

---

## 6. GIS / Zoning Maps

| Resource | URL | Notes |
|----------|-----|-------|
| Official Zoning Map (ArcGIS) | https://gis.elizabethtownky.org/apps/infomap/index.html?webmap=e1019a7f760a43babd7d51560a898320 | Zoning, overzone, amendments; search by address. |
| Basic Map (parcels, streets, imagery) | https://www.arcgis.com/apps/instant/sidebar/index.html?appid=18d5db4964c44a8591494eed583985db | Nearmap imagery; parcel info links to PVA. |
| KyGovMaps (state portal) | https://opengisdata.ky.gov/ | Discover/download KY geospatial data. |

No public downloadable open-data catalog found on the city GIS site; layers are view-only in the apps. Phase 4.

---

## 7. County-level (Hardin County Clerk)

**Office:** Hardin County Clerk's Office, 150 N. Provident Way, Suite 103, Elizabethtown, KY 42701 — 270-765-2171, https://hccoky.org/  
**Clerk:** Brian D. Smith  
**Open Records:** Written requests accepted in person, mail, fax (270-765-6193), email; $0.50/page copies. Form available on site.  
**Relevance:** County records (deeds, etc.) are separate from city; useful for property/zoning cross-reference later. Not primary for Phase 1.

---

## 8. Contacts for access & verification

| Role | Name | Contact |
|------|------|---------|
| City Clerk | Jessica Graham | City Hall, 200 W Dixie Ave; 270-765-6121 |
| Mayor | Jeff Gregory | jeff.gregory@elizabethtownky.gov; (270) 765-6121 |
| Public Relations | Amy Inman | amy.inman@elizabethtownky.gov; 270-317-2617 |
| Permit support | Emily Prather-Rodgers / Jim Shaw | emily.prather-rodgers@elizabethtownky.gov; 270-982-3266 |
| County Clerk | Brian D. Smith | brian.smith@hccoky.org; 270-765-2171 |

**Next step:** Visit or email the City Clerk to confirm coverage of 2025 minutes and request any missing PDFs; then begin the fetcher for the Documents/Agenda and Minutes tree.
