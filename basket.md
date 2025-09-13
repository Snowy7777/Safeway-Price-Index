# Core Basket (target = stable items, unit-normalizable)
> Aim for 25 items. Track at least 60% coverage per month; fall back to a "Core 15" if needed.

Fresh / Dairy
1. Milk, whole, per gallon (128 oz) — convert listed sizes to $/gal.
2. Eggs, large, per dozen (12 ct).
3. Yogurt, plain, 32 oz tub — $/oz.
4. Cheddar cheese, 8 oz block — $/oz.
5. Butter, unsalted, 16 oz (1 lb) — $/lb.
6. Chicken breast, boneless/skinless — $/lb.
7. Ground beef, 80/20 — $/lb.
8. Bananas — $/lb.
9. Apples (e.g., Gala) — $/lb.
10. Yellow onions — $/lb.
11. Russet potatoes — $/lb (convert bag sizes to per-lb).

Center Store
12. Sandwich bread, ~20 oz loaf — $/oz.
13. Rice, long-grain, 2 lb (or nearest) — $/lb.
14. Pasta, dry, 16 oz — $/oz.
15. Canned tomatoes, 14.5 oz — $/oz.
16. Peanut butter, 16 oz — $/oz.
17. Breakfast cereal (Cheerios-like), 10–14 oz — $/oz.
18. Coffee, ground, 10–12 oz — $/oz.
19. Cooking oil, canola, 48 oz — $/oz.
20. Olive oil, 16.9 oz — $/oz.
21. Sugar, granulated, 4 lb — $/lb.
22. All-purpose flour, 5 lb — $/lb.
23. Beans, canned, 15–16 oz — $/oz.
24. Frozen vegetables, 12 oz — $/oz.

Non-Food (index appendix; optional weight 5–10%)
25. Toilet paper, “12 mega rolls” (normalize to sheets/roll if possible; otherwise track as pack price with clear caveat).

**Normalization rules**
- Always compute a **unit_price** (e.g., $/oz or $/lb). For multi-packs, divide by count when sensible (e.g., eggs).
- If exact size not available, include item and record `size_actual` (used for unit conversion).
- Prefer a **store-brand** SKU when clearly labeled (e.g., Lucerne milk/eggs; Signature Select pantry). If store-brand missing, use the most common national brand; track brand in `brand_observed`.
