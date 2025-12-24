# Visual Design Patterns & Usage Examples
## HyperCode Neurodivergent-Friendly Interface Layouts

---

## PATTERN 1: OPTIMAL CODE EDITOR LAYOUT

### Full Layout (Desktop)

```
╔═══════════════════════════════════════════════════════════════════════════╗
║ FILE MENU                                                            [−] [□] [×] ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  HyperCode Editor › Project_01 › fibonacci.hy                             ║
╠════════════════════╦═══════════════════════════════════╦════════════════════╣
║                    ║                                   ║                    ║
║   FILE BROWSER     ║      CODE EDITOR                  ║  VARIABLE STATE    ║
║                    ║                                   ║                    ║
║  📁 project_01     ║  1  ⦚ DEFINE fibonacci            ║  Active Variables: ║
║   📄 main.hy       ║      INPUT: n                      ║                    ║
║   📄 utils.hy  ─►  ║      OUTPUT: integer               ║  n: 5             ║
║   📄 tests.hy      ║                                   ║  result: 5         ║
║   📄 helpers.hy    ║  2  ├─ LOOP i FROM 2 TO n         ║  i: 3 (current)    ║
║                    ║  3  │  ├─ prev = result           ║  prev: 3           ║
║   (4 visible)      ║  4  │  ├─ result = result + prev  ║  temp: 5           ║
║                    ║  5  │  └─ RETURN result           ║                    ║
║  SEARCH: ...       ║  6  └─ END LOOP                  ║  Function Calls:   ║
║                    ║                                   ║  fibonacci(5)      ║
║ 🔍 PANEL CONTROLS  ║  ← Cursor on line 4              ║  → View Details    ║
║  ⊙ ⊕ ✕             ║                                   ║                    ║
║                    ║  [50% zoom] ← | →                ║  🔍 PANEL CONTROLS ║
║                    ║                                   ║  ⊙ ⊕ ✕             ║
╠════════════════════╩═══════════════════════════════════╩════════════════════╣
║ TESTS (3 visible)                │ ERROR LOG              │ CONSOLE OUTPUT    ║
║                                   │                        │                   ║
║ ✓ test_fibonacci_0: 0 == 0        │ ✓ No errors           │ > fibonacci(5)    ║
║ ✓ test_fibonacci_5: 5 == 5        │ (green indicator)      │ ← 5               ║
║ ✗ test_fibonacci_10: 55 != 42     │                        │ > fibonacci(10)   ║
║                                   │ Run diagnostics        │ ← 55              ║
║ [⊙ Rerun All Tests]               │ [View Full Log]        │                   ║
╚═══════════════════════════════════════════════════════════════════════════╛
```

### Key Design Features Highlighted

**✓ Panel Organization:**
- Left: File browser (minimal, 20% width)
- Center: Main code editor (60% width, primary focus)
- Right: Live variable inspector (20% width)
- Bottom: Test results + error log + console (25% height)

**✓ Visual Hierarchy:**
- Line numbers: Light gray (#AAAAAA), muted so they don't distract
- Code content: Dark text (#1F1F1F) on off-white (#F5F5F5)
- Syntax colors: Semantic (keyword=blue, function=orange, variable=green)
- Active line: Subtle highlight (#F0F7F9), not obtrusive

**✓ Information Density:**
- Each panel shows 4-6 items maximum
- Scrollable areas clearly marked
- White space between elements (16px gutters)
- No overlapping or floating elements

**✓ Accessibility:**
- Keyboard focus visible (blue border, not shown in ASCII but present)
- Tab order: Left sidebar → Code editor → Right sidebar → Bottom panels
- All controls keyboard accessible (no mouse required)
- Screen reader friendly: semantic HTML with ARIA labels

---

## PATTERN 2: ERROR MESSAGE DISPLAY

### In-Line Error (Where It Occurs)

```
CODE:                          ERROR INDICATOR:

┌─ Line 15 ─────────────────┐  ┌─ INLINE ERROR ─────────────────┐
│ 15  IF count > THRESHHOLD │  │ ⚠ Variable 'THRESHHOLD'        │
│           ↑ underline    │  │   not defined (typo?)          │
│           (red squiggle) │  │                                 │
│                          │  │ Suggestions:                    │
│                          │  │ • Did you mean: threshold?     │
│                          │  │ • Line 8: threshold = 100      │
│                          │  │                                 │
│                          │  │ [Fix] [Dismiss] [Help]         │
└────────────────────────────┘  └─────────────────────────────────┘
```

### Error Banner (Bottom)

```
╔═══════════════════════════════════════════════════════════════════════════╗
║ ✕ ERROR: Variable 'THRESHHOLD' not defined                               │ │
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  LOCATION:    Line 15, Column 20                                          ║
║  SEVERITY:    Error (blocks execution)                                    ║
║                                                                            ║
║  THE PROBLEM:                                                             ║
║  You're using a variable 'THRESHHOLD' on line 15, but it was never       ║
║  declared. Variables must be defined before use.                          ║
║                                                                            ║
║  QUICK FIXES (choose one):                                                ║
║  [✓] Correct spelling: THRESHHOLD → threshold                             ║
║  [✓] Create variable: SET threshhold = 100 (with typo preserved)         ║
║  [✓] View where 'threshold' is defined (line 8)                           ║
║                                                                            ║
║  MORE HELP:                                                                ║
║  Learn about variable scope › | See related errors ›                      ║
║                                                                            ║
║  [Apply Fix] [Ignore] [Mark as Known Issue]                              ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### Color & Styling Notes

```
Error Banner:
├─ Left border: 3px solid #DD4400 (burnt orange, visible but not aggressive)
├─ Background: #FFECEC (very pale red, low saturation)
├─ Text: #1F1F1F (dark, readable)
├─ Buttons: Secondary style (outlined, not filled)
├─ Icons: ✕ (clear/close symbol, not aggressive danger symbol)
└─ Icon color: #DD4400 (matches theme)

Inline Error:
├─ Underline: Wavy, #DD4400 (indicates suggestion, not hard error)
├─ Tooltip: Appears on hover/focus
├─ Keyboard shortcut: Alt+E to toggle error panel
└─ Audio: Optional gentle beep (if enabled in settings)
```

---

## PATTERN 3: CODE BLOCK VISUAL STRUCTURE

### Nested Block Example

```
┌────────────────────────────────────────────────────────────────┐
│ LOOP  from  0  to  10  as  i                          [⊙ ⊕ ✕] │  ← Header: medium blue
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌─ Nested Block (indented 20px) ─────────────────────────┐  │
│  │ IF  i  MOD  2  ==  0  THEN                    [⊙ ⊕ ✕]   │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │  ┌─ Further Nested ────────────────────────────────┐    │  │
│  │  │ SET result = result + i              [⊙ ⊕ ✕]   │    │  │
│  │  └──────────────────────────────────────────────────┘    │  │
│  │                                                           │  │
│  └─────────────────────────────────────────────────────────┘  │
│                                                                │
│  SET i = i + 1                                                │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Block Components Explained

```
┌── HEADER SECTION ──────────────────────────────────────────────┐
│ Keyword(Blue) Param Param Param Param [Control Icons]          │
│ LOOP         from  0    to   10   as   i    [⊙ ⊕ ✕]           │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│ CONTENT AREA (40px padding, white background)                 │
│ ├─ Can contain other blocks (nested)                          │
│ ├─ Can contain simple statements                              │
│ └─ Visual indentation shows nesting level                     │
│                                                                 │
├────────────────────────────────────────────────────────────────┤
│ Optional: Footer with block summary or actions                │
└────────────────────────────────────────────────────────────────┘

CONTROL ICONS (right-aligned in header):
⊙ = View/Edit parameters
⊕ = Expand/collapse nested blocks
✕ = Delete block (with confirmation)

Drag Handle: Left edge, 8px margin, hover to grab
```

### Spacing & Dimensions

```
Block Sizing:
├─ Header height: 32px (comfortable for touch)
├─ Header padding: 8px horizontal, 8px vertical
├─ Content padding: 16px all sides
├─ Nesting indent: 20px per level
├─ Border: 2px solid #E0E0E0
├─ Border radius: 8px
├─ Min width: 200px
├─ Min height for content area: 40px
└─ Shadow: 0 1px 3px rgba(0,0,0,0.08)

Hover state:
├─ Shadow increases: 0 4px 8px rgba(0,0,0,0.12)
├─ Border color: #0066CC (highlights active block)
└─ Animation duration: 100ms ease-out
```

---

## PATTERN 4: GAMIFICATION ACHIEVEMENT DISPLAY

### Main Achievement Panel

```
╔═══════════════════════════════════════════════════════╗
║ YOUR PROGRESS                              [×]       ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  TODAY'S SESSION                                      ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                 ║
║  45 XP earned  |  Duration: 1h 23m  |  3 tests ✓    ║
║                                                       ║
║  PROGRESS TO NEXT LEVEL                             ║
║  ░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░ (75/100 XP)   ║
║                                                       ║
║  ACTIVE ACHIEVEMENTS                                 ║
║  ┌─────────────┬─────────────┬─────────────────┐   ║
║  │ 🏅 Code     │ 🎯 Debugger │ ⭐ Streak     │   ║
║  │ Master      │ Expert      │ Warrior       │   ║
║  │ Functions   │ 25 bugs     │ 7 Days        │   ║
║  │ created     │ fixed       │ Active        │   ║
║  └─────────────┴─────────────┴─────────────────┘   ║
║                                                       ║
║  RECENT UNLOCKS                                       ║
║  ✓ First 50 XP (yesterday)                           ║
║  ✓ Test Master - pass 10 tests (3 days ago)         ║
║  ✓ Syntax Ninja - no errors in code (5 days ago)    ║
║                                                       ║
║  [Settings] [Achievements Gallery] [Leaderboard]   ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

### Compact Achievement Indicator (Always Visible)

```
┌────────────────────────┐
│ XP TODAY: 45   [»]     │  ← Click to expand
│ ████░░░░ 75/100 LVL 3  │
│ 🏅 Streak: 7 days      │
└────────────────────────┘
```

### Achievement Card (Individual)

```
╔════════════════════════════╗
║ ★ ACHIEVEMENT UNLOCKED!    ║
║                            ║
║         🏆                 ║
║                            ║
║   CODE MASTER              ║
║   Created 10 functions     ║
║                            ║
║   +25 XP earned            ║
║   New badge available      ║
║                            ║
║  [Share] [View Profile]    ║
╚════════════════════════════╝
```

### Color Scheme for Achievements

```
Locked Achievement:    #DDDDDD background, #777777 text
Earned Achievement:    #FFF8E1 background, #FFD700 text + icon glow
In Progress:          #F0F7F9 background, #0066CC text
Milestone Unlocked:   #FFF3E0 background, #FFB300 text + animation

Progress Bar:
├─ Unfilled: #DDDDDD
├─ Filled: Gradient from #0066CC (blue) to #00D4AA (teal)
└─ Animation: Smooth fill over 500ms when updated
```

---

## PATTERN 5: COLOR CONTRAST EXAMPLES

### Text Combinations (All WCAG AAA Compliant)

```
LIGHT MODE:

#1F1F1F (near-black text) on #F5F5F5 (off-white)
████████████████████████████████████████████████████
Result: 17.4:1 contrast ratio ✓✓✓ (Far exceeds AAA)

#555555 (medium gray) on #F5F5F5 (off-white)
████████████████████████████████████████████████████
Result: 8.2:1 contrast ratio ✓✓ (Exceeds AAA)

#0066CC (blue keyword) on #FFFFFF (white)
████████████████████████████████████████████████████
Result: 5.1:1 contrast ratio ✓ (AA/AAA borderline - use on highlighted areas only)


DARK MODE:

#F5F5F5 (off-white text) on #1A1A1A (off-black)
████████████████████████████████████████████████████
Result: 17.4:1 contrast ratio ✓✓✓

#AAAAAA (medium gray) on #1A1A1A (off-black)
████████████████████████████████████████████████████
Result: 8.2:1 contrast ratio ✓✓

#50B8E6 (bright blue keyword) on #1A1A1A (off-black)
████████████████████████████████████████████████████
Result: 5.3:1 contrast ratio ✓
```

### Why NOT Pure White on Pure Black

```
CONTRAST TOO HIGH (Problematic):

#000000 (pure black) on #FFFFFF (pure white)
████████████████████████████████████████████████████
Result: 21:1 contrast ratio

Problems for neurodivergent users:
❌ Excessive brightness contrast causes visual stress
❌ Dyslexic users report "letter swimming" effect
❌ ADHD users may experience sensory overwhelm
❌ Can trigger migraines in sensitive individuals

Better Alternative:
#1F1F1F (near-black) on #F5F5F5 (off-white)
████████████████████████████████████████████████████
Result: 17.4:1 contrast ratio

✓ Still far exceeds accessibility requirements
✓ Reduces visual strain
✓ More comfortable for extended reading/coding
✓ Research shows dyslexic users prefer this range
```

---

## PATTERN 6: KEYBOARD NAVIGATION FLOW

### Tab Order Visual

```
FOCUS SEQUENCE (Tab key):

1. Menu bar (File, Edit, View)
    ↓ Tab
2. File browser panel
    ↓ Tab → ↓ ↑ (arrow keys navigate files)
3. Open file tab selector
    ↓ Tab
4. Code editor (main input area)
    ↓ Tab → Move focus to search box in editor
5. Variable inspector panel
    ↓ Tab → ↓ ↑ (arrow keys navigate variables)
6. Test results panel
    ↓ Tab → ↓ ↑ (arrow keys navigate tests)
7. Error log panel
    ↓ Tab
8. Console output
    ↓ Tab
9. Floating action buttons (Run, Save, etc.)
    ↓ Tab → cycles back to Menu bar

SHIFT+TAB: Navigate backwards through sequence
```

### Focus Ring Styling

```
Default Focus State:
├─ 3px solid #0066CC outline
├─ 2px offset from element
├─ Rounded corners (matches element border radius)
└─ Animation: None (static, not blinking)

Example:

Normal Button:
┌─────────────────┐
│  Click Me       │
└─────────────────┘

Focused Button (after Tab):
┌─────────────────┐
│  Click Me       │  ← 3px blue outline, 2px offset
└─────────────────┘
  (outline shown here for clarity)

Active Button (Enter pressed):
┌─────────────────┐
│  Click Me       │
└─────────────────┘
(background color changes, outline remains visible)
```

---

## PATTERN 7: MOBILE/TABLET ADAPTATION

### Responsive Layout: Tablet View (iPad)

```
┌─────────────────────────────────────────────┐
│ ⊙ HyperCode                          ⚙ [×] │ ← Hamburger menu
├─────────────────────────────────────────────┤
│ PROJECT › fibonacci.hy        [Run] [Save] │
├──────────────────────┬────────────────────┤
│                      │                    │
│  FILE BROWSER        │  CODE EDITOR       │
│  • main.hy           │  1  DEFINE fibonacci
│  • utils.hy          │      INPUT: n
│  • tests.hy          │      OUTPUT: result
│                      │                    │
│  [Keyboard hidden    │  2  ├─ LOOP i FROM 0
│   when typing]       │      │   TO n
│                      │      └─ RETURN result
│                      │
├──────────────────────┴────────────────────┤
│ [Test Results: 2/3 pass] [Errors: 1]    │
└─────────────────────────────────────────┘

DIFFERENCES FROM DESKTOP:
├─ Single-column layout (sequential panels)
├─ File browser hidden by default (swipe or menu)
├─ Larger touch targets (44px minimum)
├─ Floating action buttons bottom-right
├─ Variable inspector becomes dropdown
└─ Orientation support (portrait/landscape)
```

### Mobile View (Phone)

```
┌──────────────────────┐
│ ⊙ fibonacci.hy  ⚙ | │ ← Menu/settings
├──────────────────────┤
│ 1  DEFINE fibonacci  │
│ 2      INPUT: n      │ ← Full width code editor
│ 3      OUTPUT: result│    No side panels
│ 4  LOOP i FROM 0 TO n│
│ 5      RETURN result │
│                      │
│                      │ (scrollable)
│                      │
│                      │
│ [⊙] [⊕] [Run] [Save]│ ← Floating buttons below
└──────────────────────┘

MOBILE OPTIMIZATIONS:
├─ Touch-friendly spacing (16px minimum)
├─ Swipe gestures: Left = previous file, Right = next file
├─ Long-press for context menus
├─ Vertical scrolling primary
├─ Landscape mode: Two-panel side-by-side (limited space)
└─ Haptic feedback on button press (if supported)
```

---

## PATTERN 8: ACCESSIBILITY FEATURES TOGGLE PANEL

### Settings Panel

```
╔════════════════════════════════════════════════════════════╗
║ ACCESSIBILITY SETTINGS                                [×] ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║ TEXT & DISPLAY                                            ║
║ ┌─────────────────────────────────────────────────────┐  ║
║ │ Font Size:          14px  [−] [+]                   │  ║
║ │ Font:               OpenDyslexic ▼                  │  ║
║ │ Line Height:        1.7   [−] [+]                   │  ║
║ │ Letter Spacing:     +0.12 [−] [+]                   │  ║
║ │                                                      │  ║
║ │ Preview: ABCD abcd 1234                             │  ║
║ │ ┌────────────────────────────────────────────────┐  │  ║
║ │ │ The quick brown fox jumps over lazy dog        │  │  ║
║ │ └────────────────────────────────────────────────┘  │  ║
║ └─────────────────────────────────────────────────────┘  ║
║                                                            ║
║ COLORS                                                    ║
║ ┌─────────────────────────────────────────────────────┐  ║
║ │ Theme:              ● Light   ○ Dark   ○ Auto      │  ║
║ │ High Contrast:      ○ Off     ● Normal ○ Maximum  │  ║
║ │ Color Scheme:       Default (Dyslexia-Optimized) ▼│  ║
║ │ Colorblind Friendly: ○ Off    ● On                │  ║
║ │ Reduce Saturation:  ○ Off     ● On                │  ║
║ └─────────────────────────────────────────────────────┘  ║
║                                                            ║
║ MOTION & ANIMATION                                        ║
║ ┌─────────────────────────────────────────────────────┐  ║
║ │ Animations:         ● On      ○ Off                │  ║
║ │ Animation Speed:    ● Normal  ○ Slow  ○ Fast      │  ║
║ │ Reduce Motion:      ○ Off     ● System Preference │  ║
║ │ Disable Autoplaying Media: ✓ Checked              │  ║
║ └─────────────────────────────────────────────────────┘  ║
║                                                            ║
║ FOCUS & ATTENTION                                         ║
║ ┌─────────────────────────────────────────────────────┐  ║
║ │ Focus Ring Visibility: ● Normal ○ Enhanced        │  ║
║ │ Keyboard Navigation Hints: ○ Off ● On            │  ║
║ │ Distraction Reduction: ○ Off   ● On              │  ║
║ │   ├─ Mute notifications: ✓                         │  ║
║ │   ├─ Hide achievement popups: ○                    │  ║
║ │   └─ Collapse sidebars when not in use: ✓         │  ║
║ │ Gamification:      ● On (can customize below)      │  ║
║ │   ├─ XP notifications: ✓                           │  ║
║ │   ├─ Achievement alerts: ✓                         │  ║
║ │   └─ Leaderboard visibility: ○                     │  ║
║ └─────────────────────────────────────────────────────┘  ║
║                                                            ║
║ AUDIO & HAPTICS                                           ║
║ ┌─────────────────────────────────────────────────────┐  ║
║ │ Audio Feedback:     ● On      ○ Off                │  ║
║ │ Volume:             ▐▌▌▌▌  70%  [−] [+]           │  ║
║ │ Haptic Feedback:    ● On      ○ Off (if supported)│  ║
║ │ Haptic Intensity:   ▐▌▌░░  50%  [−] [+]           │  ║
║ └─────────────────────────────────────────────────────┘  ║
║                                                            ║
║ [Reset to Defaults] [Save] [Cancel]                     ║
╚════════════════════════════════════════════════════════════╝
```

---

## SUMMARY: DESIGN PATTERN PRINCIPLES

### The 7 Core Patterns Applied

1. **Visual Hierarchy**: Clear, scannable layouts with 30-40% whitespace
2. **Explicit Information**: No hidden menus; all options visible or accessible via clear controls
3. **Semantic Colors**: Color used to convey meaning, not decoration (blue=keyword, orange=function)
4. **Keyboard Primary**: All functionality accessible without mouse
5. **Immediate Feedback**: Every action gets visual/audio confirmation within 250ms
6. **Focused Content**: Never more than 5-9 items visible; chunked information
7. **Accessible Defaults**: Accessibility features active by default, not afterthought

### Testing These Patterns

**With Users:**
- ADHD tester: Can they complete task without distraction/overwhelm?
- Dyslexic tester: Can they read code without strain? Does syntax highlighting help?
- Autistic tester: Do the consistent patterns feel predictable and comfortable?

**With Tools:**
- WebAIM Contrast Checker
- axe DevTools (automated a11y audit)
- Lighthouse (Google Chrome)
- VoiceOver (macOS) / NVDA (Windows)

**Metrics to Track:**
- Task completion time
- Error recovery time
- Self-reported cognitive load (1-10)
- Feature adoption rate
- Accessibility feature usage

---

**These patterns form the foundation of HyperCode's neurodivergent-friendly design. Iterate based on user feedback, not assumptions.**
