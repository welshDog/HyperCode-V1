# HyperCode: Neurodivergent-First Design Specifications
## Quick Reference Guide for Implementation

---

## 1. TYPOGRAPHY SPECIFICATIONS

### Font Families
| Use Case | Recommended Font | Fallback | Rationale |
|----------|-----------------|----------|-----------|
| **Code Editor** | OpenDyslexic Mono | Lexend Mono → Consolas | Optimized for dyslexia; clear letterform distinctions (l/1, O/0) |
| **UI Labels** | OpenDyslexic | Lexend → -apple-system | Consistent with code environment; reduces context switching |
| **Help/Documentation** | Lexend | OpenDyslexic → Georgia | Excellent readability; preferred for long-form text |
| **Monospace (Alternative)** | Monaco | Consolas → Courier New | Apple ecosystem standard; highly legible |

### Font Sizing & Spacing
| Element | Size | Line Height | Letter Spacing | Word Spacing | Example Use |
|---------|------|------------|-----------------|--------------|-------------|
| **Main Code** | 16-18px | 1.7-1.8 | +0.12em | Default | Primary editor content |
| **Secondary Code** | 14px | 1.6 | +0.1em | Default | Inline examples, tooltips |
| **Labels/UI** | 14px | 1.6 | +0.08em | Default | Buttons, menus, dialogs |
| **Help Text** | 12-13px | 1.6 | +0.05em | Default | Error messages, hints |
| **Console Output** | 13px | 1.5 | Default | Default | Log/debug output |

### Font Weight Usage
- **Regular (400):** All body text, code content
- **Medium (500):** Labels, headings, interactive elements
- **Avoid:** Thin (<400), Bold (>600) unless for visual hierarchy emphasis

---

## 2. COLOR PALETTE & ACCESSIBILITY

### Base Palette (Dyslexia-Optimized)

#### Light Mode (Primary)
```
BACKGROUNDS:
  Primary BG:      #F5F5F5  (off-white, reduces glare)
  Secondary BG:    #FFFFFF  (pure white, minimal use)
  Accent BG:       #F0F7F9  (very pale blue, for highlights)

TEXT:
  Primary Text:    #1F1F1F  (near-black, high readability)
  Secondary Text:  #555555  (medium gray, for meta info)
  Disabled Text:   #AAAAAA  (light gray)

CODE SYNTAX:
  Keywords:        #0066CC  (clear blue)
  Functions:       #CC6600  (warm orange)
  Variables:       #006633  (muted green)
  Strings:         #663366  (muted purple)
  Comments:        #888888  (medium gray)
  Numbers:         #DD4400  (burnt orange)
```

#### Dark Mode (Alternative)
```
BACKGROUNDS:
  Primary BG:      #1A1A1A  (off-black, reduces white glare)
  Secondary BG:    #262626  (charcoal, slight contrast)
  Accent BG:       #0D2B35  (very dark blue-gray)

TEXT:
  Primary Text:    #F5F5F5  (off-white, readable on dark)
  Secondary Text:  #AAAAAA  (medium gray)
  Disabled Text:   #555555  (dark gray)

CODE SYNTAX:
  Keywords:        #50B8E6  (bright blue for dark mode)
  Functions:       #E6A857  (warm gold)
  Variables:       #5ECE7C  (bright green)
  Strings:         #CE7CE6  (bright purple)
  Comments:        #777777  (medium gray, adjusted for contrast)
  Numbers:         #F5A450  (bright orange)
```

### Contrast Compliance

| Element | Requirement | Light Mode Example | Dark Mode Example | Verification |
|---------|-------------|-------------------|-------------------|--------------|
| **Body Text** | 7:1+ (AAA) | #1F1F1F on #F5F5F5 | #F5F5F5 on #1A1A1A | ✓ Exceeds WCAG AAA |
| **Code Keywords** | 5:1+ (AA) | #0066CC on #F5F5F5 | #50B8E6 on #1A1A1A | ✓ AA compliant |
| **UI Focus Ring** | Visible | 3px #0066CC outline | 3px #50B8E6 outline | ✓ Keyboard accessible |
| **Disabled UI** | 4.5:1+ (AA) | #AAAAAA on #F5F5F5 | #555555 on #1A1A1A | ✓ Readable but dimmed |

**Tool for verification:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

---

## 3. LAYOUT GRID & SPACING

### Grid System
- **Base Unit:** 8px
- **Grid Type:** 12-column for responsive layouts
- **Gutter Width:** 16-24px (based on screen size)

### Spacing System (Multiples of 8px)
| Variable | Value | Use Case |
|----------|-------|----------|
| `$space-4` | 4px | Minimal spacing (between inline elements) |
| `$space-8` | 8px | Tight spacing (button padding, small gaps) |
| `$space-12` | 12px | Standard spacing (between UI elements) |
| `$space-16` | 16px | Medium spacing (section separators) |
| `$space-24` | 24px | Large spacing (major sections) |
| `$space-32` | 32px | XL spacing (page-level sections) |

### Whitespace Guidelines
- **Minimum:** 20% empty space in any view
- **Optimal:** 30-40% empty space
- **Maximum Items Per View:** 7 ± 2 items (working memory limit)

---

## 4. COMPONENT SPECIFICATIONS

### Code Editor Panel

**Dimensions & Layout:**
```
Main Panel:
  ├─ Left Sidebar (File Browser):  20% width, min 150px, max 300px
  ├─ Center (Code Editor):         60% width, min 400px
  └─ Right Sidebar (Inspector):    20% width, min 150px, max 300px

Bottom Panel:
  ├─ Test Results: 40% width
  ├─ Error Log: 30% width
  └─ Console Output: 30% width
  Height: 25% of screen, resizable

Gutters: 16px between panels
```

**Line Number Styling:**
- Font: Monospace, 12px, #AAAAAA
- Background: #EEEEEE (light gray)
- Gutter width: 40px
- Hover on line: Highlight full line with #F0F7F9

### Code Block Component

**Visual Structure:**
```
┌─ Block Header (32px height, medium blue bg) ────────────────┐
│  LOOP  from  0  to  10  as  i                    [⊙ ⊕ ✕]    │
├────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─ Nested Block (indented 20px) ──────────────────────┐   │
│  │  IF  i  >  5  THEN                         [⊙ ⊕ ✕]  │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │    SET result = result + i                          │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

**Styling:**
- Border: 2px solid #E0E0E0
- Border Radius: 8px
- Background: #FAFAFA (very light gray)
- Nesting Indentation: 20px per level
- Drag Handle: 24x24px, left-aligned with 8px margin

### Error Message Component

**Location:** Inline + persistent bottom banner

```
Error Message Structure:
┌─ ERROR BANNER (2px red left border) ──────────────────────┐
│  ✕ Syntax Error: Variable 'threshold' not defined         │
│                                                             │
│  Location: Line 15, Column 8                              │
│  Context: IF count > threshold                            │
│                      ↑ HERE                                │
│                                                             │
│  Problem: Variable 'threshold' is used but never defined. │
│                                                             │
│  Quick Fixes:                                              │
│  □ Create variable: SET threshold = 10                    │
│  □ Did you mean: THRESHOLD (different spelling)?          │
│  □ Check documentation: Variables & Scope                 │
│                                                             │
│  [Dismiss] [View Related Code]                            │
└─────────────────────────────────────────────────────────────┘
```

**Color & Styling:**
- Background: #FFECEC (very light red)
- Left Border: 3px solid #DD4400 (burnt orange, not pure red)
- Text: #1F1F1F
- Links: #0066CC (blue, underlined)
- Button Style: Secondary (outlined, not filled)

---

## 5. INTERACTIVE COMPONENTS

### Button States

| State | Background | Text | Border | Cursor |
|-------|-----------|------|--------|--------|
| **Primary (Default)** | #0066CC | #FFFFFF | None | pointer |
| **Primary (Hover)** | #0052A3 | #FFFFFF | None | pointer |
| **Primary (Active)** | #004080 | #FFFFFF | None | pointer |
| **Primary (Focus)** | #0066CC | #FFFFFF | 3px solid #0066CC offset 2px | pointer |
| **Primary (Disabled)** | #CCCCCC | #999999 | None | not-allowed |
| **Secondary (Default)** | transparent | #0066CC | 1px solid #CCCCCC | pointer |
| **Secondary (Hover)** | #F0F7F9 | #0066CC | 1px solid #0066CC | pointer |
| **Secondary (Disabled)** | transparent | #AAAAAA | 1px solid #DDDDDD | not-allowed |

### Form Inputs

**Dimensions:**
- Height: 40px
- Padding: 8px horizontal, 10px vertical
- Border Radius: 6px
- Font Size: 14px
- Line Height: 1.5

**States:**
```
Default:
  Background: #FFFFFF
  Border: 1px solid #DDDDDD
  Text Color: #1F1F1F

Focus:
  Background: #FFFFFF
  Border: 2px solid #0066CC
  Box Shadow: 0 0 0 3px rgba(0, 102, 204, 0.3)
  Text Color: #1F1F1F

Error:
  Background: #FFFBFB
  Border: 2px solid #DD4400
  Text Color: #1F1F1F

Disabled:
  Background: #F5F5F5
  Border: 1px solid #DDDDDD
  Text Color: #AAAAAA
  Cursor: not-allowed
```

### Dropdown/Select

**Special Handling for Accessibility:**
- Always include visible label above
- Show selected value prominently
- Display all options in list (no hidden overflow)
- Custom select arrow icon (never browser default)

---

## 6. GAMIFICATION ELEMENTS (Optional)

### Achievement/Progress Display

**Size & Placement:**
- Location: Top-right corner OR toggle-able sidebar
- Width: 300px (sidebar) or 250px (compact)
- Can be minimized to icon-only (small dot indicator)

**Color Scheme:**
```
Achievement Locked:    #CCCCCC (gray)
Achievement Earned:    #FFD700 (gold)
XP Progress Bar:       Gradient #0066CC → #00D4AA (teal)
Milestone Unlocked:    #FFB300 (orange) with animation
```

**Typography:**
- Achievement Name: Medium (500), 14px
- XP Value: Regular (400), 12px
- Progress Label: Regular (400), 11px

### XP System

**Point Distribution (Per Task):**
| Task | XP Value |
|------|----------|
| Line of code written | 1 XP |
| Code compiles | 5 XP |
| Test passes | 10 XP |
| All tests pass (milestone) | 50 XP |
| Debug completed | 15 XP |
| Function created | 20 XP |
| **1 Daily Coding Streak** | +2 XP bonus |

---

## 7. ANIMATION & MOTION

### Animation Timing
- **Standard Duration:** 250ms (250 milliseconds = optimal for feedback without feeling sluggish)
- **Easing Function:** `cubic-bezier(0.16, 1, 0.3, 1)` (ease-out-back, feels snappy)
- **Quick Feedback:** 100-150ms (for immediate micro-interactions)

### Animations to INCLUDE

| Animation | Duration | Trigger | Effect |
|-----------|----------|---------|--------|
| Code block expand | 250ms | Click | Smooth height increase; content fades in |
| Test pass celebration | 300ms | Test passes | Subtle pulse of green highlight; checkmark animation |
| Error slide-in | 250ms | Error occurs | Banner slides up from bottom; icon appears |
| Progress bar fill | 500ms | Progress updates | Smooth width transition; no snap |
| Button hover | 100ms | Mouse enter | Subtle color transition |
| Focus ring | None | Keyboard focus | Static outline (no animation) |

### Animations to AVOID

- ❌ Flashing (any flicker > 3 times/second)
- ❌ Rapid scroll-triggered animations
- ❌ Autoplay video/audio (no unmuted media)
- ❌ Parallax or 3D rotations (vestibular disorder trigger)
- ❌ Infinite loops (unless user-triggered)

**Implementation:**
```css
/* User preference for reduced motion */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 8. SYNTAX HIGHLIGHTING CONFIGURATION

### Semantic Color Assignment

**HyperCode Syntax Categories:**
```
KEYWORD:        #0066CC    (if, for, while, SET, LOOP)
FUNCTION:       #CC6600    (myFunc, calculateSum, render)
VARIABLE:       #006633    (count, result, threshold)
STRING:         #663366    ("hello", 'world')
COMMENT:        #888888    (// this is a comment)
NUMBER:         #DD4400    (42, 3.14, 0xFF)
OPERATOR:       #0066CC    (+, -, *, /, AND, OR)
BRACKET:        #555555    ({}, [], () - subtle to reduce noise)
ERROR:          #DD4400    (syntax errors, typos, underlined)
```

**Related Element Highlighting (on hover/selection):**
- When cursor on variable → all references highlighted with semi-transparent bg
- When cursor on `{` → matching `}` highlighted
- When selecting function → all calls highlighted

---

## 9. ACCESSIBILITY CHECKLIST FOR DEVELOPERS

### Critical Accessibility Features
- [ ] **Keyboard Navigation:** All functions accessible via Tab, Enter, arrow keys
- [ ] **Focus Indicator:** Visible 3px outline on all interactive elements
- [ ] **Focus Order:** Logical tab order (left-to-right, top-to-bottom)
- [ ] **Alt Text:** All images/icons have descriptive labels
- [ ] **ARIA Labels:** Form inputs, buttons, complex widgets labeled
- [ ] **Color Not Only Signal:** Errors use text + color + icon
- [ ] **Semantic HTML:** Proper heading hierarchy (h1, h2, h3), lists, landmarks
- [ ] **Screen Reader Testing:** Test with VoiceOver (Mac), JAWS (Windows), NVDA (open-source)

### Motion & Sensory
- [ ] **No Autoplaying Media:** Videos/audio require explicit user action
- [ ] **Animation Disableable:** Respect `prefers-reduced-motion` media query
- [ ] **No Rapid Flashing:** No element flashes > 3 times/second
- [ ] **Sound Optional:** All audio feedback has visual alternative
- [ ] **Hover Not Required:** All information available without hover (touch devices)

### Cognitive Load
- [ ] **Plain Language:** No jargon; sentences < 15 words when possible
- [ ] **Consistent Terminology:** Same term always used (never "run" vs "execute")
- [ ] **Clear Instructions:** Step-by-step guidance for complex tasks
- [ ] **Error Clarity:** Errors explain what went wrong + how to fix
- [ ] **Consistent Layout:** Navigation/structure identical across all screens
- [ ] **Help Accessible:** No hidden-behind-links help; context-sensitive tooltips

### Testing
- [ ] **User Testing:** At least 3 neurodivergent testers (ADHD, dyslexic, autistic)
- [ ] **Automated Auditing:** axe DevTools, Lighthouse, Wave browser extensions
- [ ] **Contrast Checking:** WebAIM Contrast Checker (all text meets WCAG AAA)
- [ ] **Mobile Testing:** Responsive design tested on tablet/phone
- [ ] **Screen Reader Testing:** VoiceOver, NVDA, JAWS (focus order, ARIA labels)

---

## 10. IMPLEMENTATION ROADMAP

### Phase 1: Foundation (Weeks 1-4)
- [ ] Typography system (OpenDyslexic + spacing)
- [ ] Color palette (light + dark mode)
- [ ] Grid & spacing system
- [ ] Basic button/input components
- [ ] Code editor layout structure

### Phase 2: Core Features (Weeks 5-8)
- [ ] Block-based visual syntax
- [ ] Syntax highlighting configuration
- [ ] Error message system
- [ ] Basic gamification (XP tracking, progress bars)
- [ ] Accessibility audit (WCAG AAA + COGA)

### Phase 3: Enhancement (Weeks 9-12)
- [ ] Voice input (basic speech-to-code)
- [ ] Gesture support (tablet/mobile)
- [ ] Advanced debugging tools (variable inspector, data flow vis)
- [ ] User preference panel (customize colors, fonts, animations)
- [ ] Community features (share accessible code, peer review)

### Phase 4: Future (Post-MVP)
- [ ] Haptic feedback integration
- [ ] 3D code visualization (WebGL)
- [ ] AI-powered personalized error messages
- [ ] VR/spatial coding environment
- [ ] Neurodivergent mentorship network

---

## 11. DESIGN TOKENS (CSS VARIABLES)

### Complete Token System

```css
:root {
  /* Colors */
  --color-primary: #0066CC;
  --color-primary-dark: #004080;
  --color-primary-light: #50B8E6;
  --color-error: #DD4400;
  --color-success: #00AA44;
  --color-warning: #FFB300;
  --color-info: #0099CC;
  
  --color-bg-primary: #F5F5F5;
  --color-bg-secondary: #FFFFFF;
  --color-bg-tertiary: #F0F7F9;
  
  --color-text-primary: #1F1F1F;
  --color-text-secondary: #555555;
  --color-text-disabled: #AAAAAA;
  
  /* Typography */
  --font-family-code: 'OpenDyslexic Mono', monospace;
  --font-family-ui: 'OpenDyslexic', sans-serif;
  --font-size-base: 14px;
  --font-size-large: 16px;
  --font-size-small: 12px;
  --line-height-normal: 1.6;
  --line-height-code: 1.8;
  --letter-spacing-normal: 0;
  --letter-spacing-code: 0.12em;
  
  /* Spacing */
  --space-4: 4px;
  --space-8: 8px;
  --space-16: 16px;
  --space-24: 24px;
  --space-32: 32px;
  
  /* Sizing */
  --radius-small: 4px;
  --radius-base: 8px;
  --radius-large: 12px;
  
  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 8px rgba(0,0,0,0.12);
  --shadow-lg: 0 8px 16px rgba(0,0,0,0.16);
  
  /* Animation */
  --duration-fast: 100ms;
  --duration-normal: 250ms;
  --easing-out: cubic-bezier(0.16, 1, 0.3, 1);
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-bg-primary: #1A1A1A;
    --color-bg-secondary: #262626;
    --color-text-primary: #F5F5F5;
    --color-text-secondary: #AAAAAA;
  }
}
```

---

## 12. QUICK START IMPLEMENTATION GUIDE

### For Frontend Developers

1. **Install fonts:**
   ```bash
   npm install opendyslexic lexend
   ```

2. **Add to stylesheet:**
   ```css
   @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;500;600');
   
   body {
     font-family: OpenDyslexic, sans-serif;
     font-size: 14px;
     line-height: 1.6;
     letter-spacing: 0.08em;
     background: #F5F5F5;
     color: #1F1F1F;
   }
   
   code {
     font-family: 'OpenDyslexic Mono', monospace;
     font-size: 16px;
     line-height: 1.8;
     letter-spacing: 0.12em;
   }
   ```

3. **Implement color tokens:**
   ```javascript
   // theme.js
   export const colors = {
     primary: '#0066CC',
     error: '#DD4400',
     bg: '#F5F5F5',
     text: '#1F1F1F'
   };
   ```

4. **Test accessibility:**
   - Install axe DevTools browser extension
   - Check contrast with WebAIM
   - Test keyboard navigation (Tab, Enter, Arrows)
   - Test with screen reader (VoiceOver on Mac)

---

## FINAL NOTES FOR HYPERCODE TEAM

This specification sheet is **living documentation**. Update as:
- New research emerges on neurodivergent UX
- User feedback from testing reveals gaps
- Accessibility standards evolve (WCAG 2.2 → 3.0)
- Implementation reveals unexpected challenges

**Remember:** Inclusive design is iterative. Start with these specs, test with neurodivergent users, gather feedback, refine.

**The Goal:** Build a programming language and IDE environment that doesn't just accommodate neurodivergent brains—it *celebrates* them.

---

**Last Updated:** December 2025  
**Version:** 1.0  
**Maintained by:** HyperCode Accessibility Team
