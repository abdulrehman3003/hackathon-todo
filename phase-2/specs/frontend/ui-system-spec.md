# Frontend UI System (Design tokens + principles)

Principles:
- Minimalist, whitespace-first, modern like Linear/Notion/Vercel
- Use system or Google font (Inter recommended)
- Pure CSS only (no Tailwind)

Design tokens (variables.css):
--bg: #ffffff
--surface: #fbfcfe
--text: #0f172a
--muted: #6b7280
--primary: #5B6CFF
--success: #10B981
--danger: #EF4444
--radius: 10px
--gap: 16px
--shadow-sm: 0 6px 18px rgba(16,24,40,0.04)
--font-sans: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto

Breakpoints:
- mobile: <=600px
- tablet: 600px-1024px
- desktop: >=1024px

CSS structure:
- src/styles/variables.css
- src/styles/global.css
- src/styles/layout.css
- src/styles/animations.css
- component-level CSS in src/components/*.css
