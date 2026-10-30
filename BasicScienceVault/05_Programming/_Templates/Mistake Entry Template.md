---
tags: [type/template]
---
# Mistake Entry Template

Copy this row into the *My mistakes* table of the matching mistake log:
- Math: [[Mistakes - Basics]] · [[Mistakes - Analysis]] · [[Mistakes - Linear Algebra]] · [[Mistakes - Geometry and Vectors]] · [[Mistakes - Foundations]]
- Neuroscience foundations: [[Mistakes - Physics]] · [[Mistakes - Chemistry]] · [[Mistakes - Biology]] · [[Mistakes - Methods]] · [[Mistakes - Computer Science]]
- Programming: [[Mistakes - Programming Basics]] · [[Mistakes - Python]] · [[Mistakes - R]] · [[Mistakes - MATLAB]] · [[Mistakes - Markdown HTML LaTeX]]

```markdown
| YYYY-MM-DD | ❌ wrong step / wrong idea | ✅ correct step / correct model | why it's wrong / quick test or test question | [[Topic note]] |
```

## Good entries are …
- **Specific:** the exact step or belief that went wrong, not "made a mistake with fractions" or "confused channels".
- **Testable:** a quick number check (e.g. plug in $a = b = 1$) or a question that would have exposed it ("What happens to $E_\text{K}$ if outside K⁺ rises?").
  For code: the print, shape check or tiny test case that would have caught the bug (`print(X.shape)`, `x[0:3]` on a 5-element example).
- **Linked:** link the topic note so the mistake shows up in its backlinks.
- **Tagged (optional):** add `#mistake/sign`, `#mistake/rule`, `#mistake/careless`, `#mistake/concept`, `#mistake/misconception`, `#mistake/units` to spot patterns via the tag pane; for code `#mistake/bug`, `#mistake/syntax`, `#mistake/off-by-one`, `#mistake/shape`, `#mistake/nan`.

## Review routine
1. Before each worksheet: skim the log of that field (2 min).
2. Weekly: re-do the tasks behind your last 5 entries without looking.
3. Before an exam: read all logs, and mark entries you no longer make with ✔️.
