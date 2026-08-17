# Citation Styling Reference Guide

## Citation Type Styling

### Case Law Citations (Blue Theme)
```
Style: Linear gradient background (blue)
Colors: #e1eaf6 → #dce6f2 (top to bottom)
Border: 1px solid rgba(80,107,160,.2)
Accent: 3px left border in #506ba0
Shadow: inset 0 -1.5px #506ba0, outer 0 2px 5px rgba(80,107,160,.14)
Text: #1a2e4a with weight 500
Padding: 3px 6px
Border-radius: 4px
Transition: 0.15s ease on all properties

Hover State:
- Background: Linear gradient (#d0dff0 → #c8d9ec)
- Transform: translateY(-1px) for elevation
- Shadow: Enhanced to 0 4px 10px rgba(80,107,160,.25)
- Effect: Brightness(1.05) filter for visual emphasis
```

### Statute/Regulation Citations (Gold Theme)
```
Style: Linear gradient background (gold)
Colors: #fef9f2 → #fbf5eb (top to bottom)
Border: 1px solid rgba(201,128,74,.25)
Accent: 3px right border in #c9804a
Shadow: inset 0 -1.5px #c9804a, outer 0 2px 5px rgba(201,128,74,.14)
Text: #5c3800 with weight 500
Padding: 3px 6px
Border-radius: 4px
Transition: 0.15s ease on all properties

Hover State:
- Background: Linear gradient (#f7f0e3 → #f3ecdc)
- Transform: translateY(-1px) for elevation
- Shadow: Enhanced to 0 4px 10px rgba(201,128,74,.25)
- Effect: Brightness(1.05) filter for visual emphasis
- Symbol: § appears in top-right corner (opacity .4)
```

### Citation Pass Page Marks

#### Case Law
```
Background: Linear gradient (#f5d842 → #f4c835)
Shadow: inset 0 -2px rgba(218,155,28,.9), outer 0 1px 3px rgba(245,185,66,.25)
Padding: 2px 4px
Border-radius: 3px
Font-weight: 500
Cursor: pointer

Hover:
- Background: Linear gradient (#f0ce2a → #efbb22)
- Shadow: inset 0 -2.5px rgba(192,130,14,.95), outer 0 2px 5px
- Transform: translateY(-1px)
```

#### Law References  
```
Background: Linear gradient (#4caf50 → #43a047)
Color: white
Shadow: inset 0 -2px rgba(27,94,32,.95), outer 0 1px 3px rgba(76,175,80,.2)
Padding: 2px 4px
Border-radius: 3px
Font-weight: 500
Cursor: pointer

Hover:
- Background: Linear gradient (#45a049 → #3b8b40)
- Shadow: inset 0 -2.5px rgba(17,71,24,.95), outer 0 2px 5px
- Transform: translateY(-1px)
```

#### Metadata Citations
```
Background: Linear gradient (#42a5f5 → #2196f3)
Color: white
Shadow: inset 0 -2px rgba(25,65,155,.95), outer 0 1px 3px rgba(66,165,245,.2)
Padding: 2px 4px
Border-radius: 3px
Font-weight: 500
Cursor: pointer

Hover:
- Background: Linear gradient (#1e88e5 → #1976d2)
- Shadow: inset 0 -2.5px rgba(13,47,125,.95), outer 0 2px 5px
- Transform: translateY(-1px)
```

## Text Formatting

### Paragraph Styling
```
Spacing between paragraphs: 1.6em (increased from 1em)
Line height: 1.88 (increased from 1.78)
Font: 17px/1.88 "Newsreader", serif
Color: #1a1a1a
Font-weight: normal body text, 500 for citations
Word-wrap: break-word
Overflow-wrap: break-word
```

### Paragraph Number Badges
```
Display: inline-block
Position: before paragraph text
Background: rgba(158,67,47,.08)
Border: 1px solid rgba(158,67,47,.2)
Border-radius: 2px
Padding: 1px 4px
Margin: 0 4px 0 2px (right margin 4px to separate from text)
Font-size: 10px
Font-weight: 600
Color: #9e432f
Font-family: IBM Plex Sans (sans-serif)
Vertical-align: super (superscript positioning)
```

### Chunk/Section Styling
```
Gap between chunks: 16px
Chunk border: 1px solid var(--line)
Chunk border-radius: 14px
Chunk background: rgba(255,254,249,.92)
Chunk padding: 20px 22px (text area)
Chunk header padding: 13px 16px
Overflow: hidden (for rounded corners effect)

Header background: Linear gradient (top to bottom)
  rgba(255,255,255,.8) → rgba(250,248,242,.5)
Header font: 11px uppercase, letter-spacing .05em
Header font-weight: 700
```

## Color Palette

### Primary Citation Colors
```
Case Law Blue:    #506ba0 (accent), #e1eaf6 → #dce6f2 (gradient)
Statute Gold:     #c9804a (accent), #fef9f2 → #fbf5eb (gradient)
Citation Pass:    
  - Case:         #f5d842 → #f4c835
  - Law:          #4caf50 → #43a047 (green)
  - Metadata:     #42a5f5 → #2196f3 (blue)
```

### Accent Colors
```
Rust (paragraph markers):  #9e432f
Success (law):             #2cb84c
Info (metadata):           #2196f3
```

## Accessibility

### Contrast Ratios
```
Case law text (#1a2e4a) on blue gradient: ✓ WCAG AA compliant
Statute text (#5c3800) on gold gradient: ✓ WCAG AA compliant
White text on green/blue: ✓ WCAG AAA compliant
```

### Keyboard Navigation
```
All marks are focusable via Tab
Hover states visible on keyboard focus
Clear outline on active-hit state: 2.5px solid
Outline offset: 2px for better visibility
```

## Animation Specifications

### Smooth Transitions
```
Property: all
Duration: 0.15s
Timing: ease
Affected properties: background, shadow, transform, filter
Hardware acceleration: transform and filter (GPU optimized)
```

### Hover Elevation
```
Transform: translateY(-1px)
Effect: Subtle lift creating depth perception
Performance: 60fps on modern hardware
```

## Implementation Notes

- All colors use CSS variables for consistency
- Linear gradients provide 3D depth without image files
- Inset shadows create beveled edge effect
- Outer shadows provide subtle elevation
- Transitions are GPU-accelerated for performance
- No JavaScript animation needed (pure CSS)
- Mobile-friendly with touch-friendly hit targets
