# Calispot design system reference

This directory contains a concise, portfolio-safe snapshot of the later Calispot visual specification. The CSS tokens are a practical reference for the documented design direction, not a complete production component library.

## Design intent

Calispot is designed for outdoor training contexts: bright light, physical fatigue, sweaty hands, and brief glances between sets. The visual direction combines a dark asphalt-like base, bone-white text, a lime accent, assertive display typography, and restrained industrial details.

## Principles

- Keep the primary action and information hierarchy obvious at a glance.
- Use high contrast for functional information; color communicates state rather than decoration.
- Prefer concise copy and large touch targets for mobile use outdoors.
- Use an 8px spacing rhythm, with a 24px lateral screen margin as the baseline.
- Keep texture and expressive accents away from text users need to read.
- Use motion only for functional feedback; avoid decorative animation.

## Semantic tokens

The default documented mode is dark. An alternate light palette is exploratory and is not treated as an MVP requirement.

| Token | Value | Intended role |
|---|---|---|
| `--bg-base` | `#1A1C18` | Screen background |
| `--bg-surface` | `#252822` | Cards and sheets |
| `--bg-elevated` | `#30332B` | Nested surfaces |
| `--text-primary` | `#F4F4EF` | Primary content |
| `--text-secondary` | `#8A8D80` | Metadata and secondary content |
| `--border` | `#3A3D33` | Borders and dividers |
| `--accent` | `#B8D54C` | Primary action and active state |
| `--accent-ink` | `#1A1C18` | Text on the accent color |
| `--alert` | `#E0531F` | Warning and highest difficulty |

## Typography and layout

- **Anton:** display headings and high-impact labels.
- **Space Grotesk:** UI, body copy, and controls.
- **JetBrains Mono:** metrics and technical data.
- **Caveat:** optional street-name alias treatment only.
- **Spacing scale:** 4, 8, 12, 16, 24, 32, 48, and 64px.
- **Cards:** 8px radius; buttons and inputs use compact radii; chips are pill-shaped.
- **Touch targets:** target at least 56px tall for primary interactive elements.

## Relationship to the interactive prototype

The standalone prototype in `../prototype/` uses an earlier typographic direction. This reference documents a later design iteration and does not imply that all prototype screens were updated to these tokens.

## Assets

- [`tokens.css`](tokens.css) — semantic colors, type families, and spacing variables.
- [`assets/calispot-mark.svg`](assets/calispot-mark.svg) — wordmark exploration.
- [`assets/pin.svg`](assets/pin.svg) and [`assets/pin-empty.svg`](assets/pin-empty.svg) — spot marker explorations.

Fonts are referenced from Google Fonts in the CSS; the system fonts remain fallbacks if the remote fonts cannot load.
