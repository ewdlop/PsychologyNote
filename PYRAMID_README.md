# Pyramid Scheme Implementation

This directory contains two implementations addressing the "Pyramid scheme" issue:

## 1. Scheme Language Implementation (`pyramid_scheme.scm`)

A comprehensive demonstration of pyramid scheme structures using Scheme (Lisp dialect).

### Features:
- **Data Structures**: Implements person records with recruits
- **Hierarchical Operations**: Functions to build and manipulate pyramid structures
- **Statistical Analysis**: Calculate pyramid size, depth, and level populations
- **Financial Modeling**: Demonstrates money flow in pyramid schemes
- **Mathematical Proof**: Shows the mathematical impossibility of sustained pyramid schemes

### Running the Scheme Code:

You can run this code with any Scheme interpreter (Racket, Guile, MIT Scheme, etc.):

```bash
# With Racket
racket pyramid_scheme.scm

# With Guile
guile pyramid_scheme.scm

# With MIT Scheme
mit-scheme --load pyramid_scheme.scm
```

To run the demonstration, uncomment the last line in the file:
```scheme
(run-pyramid-demo)
```

### Key Functions:
- `make-person`: Create a person in the pyramid
- `add-recruit`: Add a recruit to someone's downline
- `pyramid-size`: Calculate total people in pyramid
- `pyramid-depth`: Calculate depth of hierarchy
- `demonstrate-impossibility`: Show mathematical unsustainability

## 2. PsychoPy Visual Implementation (`pyramid_visual.py`)

A visual demonstration of pyramid structures using PsychoPy library.

### Features:
- **Visual Pyramid**: Interactive 3D-style pyramid with blocks
- **Animated Construction**: Watch the pyramid being built level by level
- **Statistical Display**: Shows levels, total blocks, and growth metrics
- **People Representation**: Alternative view showing exponential growth of people
- **Warning Messages**: Educational warnings about pyramid scheme dangers

### Requirements:

```bash
pip install psychopy
```

### Running the PsychoPy Script:

```bash
python pyramid_visual.py
```

### Controls:
- **SPACE**: Animate pyramid construction
- **P**: Switch to people/pyramid scheme view (from main view)
- **B**: Go back to pyramid view (from people view)
- **ESC**: Exit the program

### Visual Elements:
1. **Main Pyramid View**:
   - 5 levels of blocks with gradient colors
   - Statistics panel showing metrics
   - Level labels
   - Animation on SPACE key

2. **Pyramid Scheme People View**:
   - Circles representing people
   - Shows exponential growth (1 → 3 → 9 → 27 → 81)
   - Warning about unsustainability
   - Level-by-level breakdown

## Educational Purpose

Both implementations serve to:

1. **Demonstrate Structure**: Show how pyramid/MLM schemes are organized
2. **Mathematical Analysis**: Prove the inherent unsustainability
3. **Visual Learning**: Help understand exponential growth problems
4. **Programming Examples**: Showcase functional programming (Scheme) and visualization (PsychoPy)

## Related Files

- `NPD and Pyramid Schemes.md`: Psychological analysis of NPD and pyramid schemes
- `README.md`: Main repository documentation

## References

- **Scheme Language**: R5RS/R6RS Scheme specification
- **PsychoPy**: https://www.psychopy.org/
- **Pyramid Schemes**: Federal Trade Commission (FTC) resources

## Warning

⚠️ **Educational Use Only**: These implementations are for educational purposes to understand and recognize pyramid schemes. Pyramid schemes are illegal in many jurisdictions and harmful to participants.

## License

Educational and research use only. See main repository LICENSE file.
