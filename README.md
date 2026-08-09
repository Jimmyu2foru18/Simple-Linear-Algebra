# Simple Linear Algebra Course Website

An interactive, multi-page educational platform for Linear Algebra, featuring video lectures and content curated from world-renowned educators.

## Preview

Experience the course live at: [Simple Linear Algebra Course](https://jimmyu2foru18.github.io/Simple-Linear-Algebra/)

## Features

- **13 Structured Chapters**: Each chapter on its own page with dedicated content
- **Multi-Source Video Integration**:
  - Core Lectures by Gilbert Strang (MIT)
  - Concept Breakdowns by Prof. Dave Explains
  - Textbook Context by Paul Cartier
  - Problem-Solving Methods by Valerie Hower
  - Quick Overviews by Early Orbit Math
- **Interactive Note-Taking**: Floating notepad with auto-save and desktop export
- **Progress Tracking**: Visual progress bar and chapter navigation (Previous/Next)
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Rich Instructional Content**: Topic breakdowns, mathematical derivations, learning strategies, visual aids, worked examples, and practice problems

## Project Structure

```
Simple-Linear-Algebra/
├── index.html              # Landing page / redirect to curriculum
├── css/
│   └── styles.css          # Global stylesheet
├── js/
│   └── main.js             # Shared JavaScript (navigation, notes, search)
├── chapters/
│   ├── index.html          # Course overview / table of contents
│   ├── chapter-01.html     # The Geometry of Linear Equations
│   ├── chapter-02.html     # Elimination with Matrices
│   ├── chapter-03.html     # Multiplication and Inverse Matrices
│   ├── chapter-04.html     # Factorization into A = LU
│   ├── chapter-05.html     # Transposes, Permutations, Spaces R^n
│   ├── chapter-06.html     # Column Space and Nullspace
│   ├── chapter-07.html     # Solving Ax = 0: Pivot Variables, Special Solutions
│   ├── chapter-08.html     # Solving Ax = b: Row Reduced Form R
│   ├── chapter-09.html     # Independence, Basis, and Dimension
│   ├── chapter-10.html     # The Four Fundamental Subspaces
│   ├── chapter-11.html     # Matrix Spaces; Rank 1; Small World Graphs
│   ├── chapter-12.html     # Graphs and Networks; Incidence Matrices
│   └── chapter-13.html     # Orthogonal Vectors and Subspaces
├── assets/                 # Static assets (images, etc.)
├── README.md
└── generate-chapters.ps1   # Helper script for chapter generation
```

## Getting Started

### Local Development

1. Clone the repository:
    ```bash
    git clone https://github.com/Jimmyu2foru18/Simple-Linear-Algebra.git
    cd Simple-Linear-Algebra
    ```

2. Open in browser:
    - Simply open `index.html` in your web browser
    - Or use a local server:
      ```bash
      python -m http.server 8000
      ```
      Then visit `http://localhost:8000`

## Course Content

The course covers essential topics in Linear Algebra including:

1. The Geometry of Linear Equations
2. Elimination with Matrices
3. Multiplication and Inverse Matrices
4. Factorization into A = LU
5. Transposes, Permutations, Spaces R^n
6. Column Space and Nullspace
7. Solving Ax = 0: Pivot Variables, Special Solutions
8. Solving Ax = b: Row Reduced Form R
9. Independence, Basis, and Dimension
10. The Four Fundamental Subspaces
11. Matrix Spaces; Rank 1; Small World Graphs
12. Graphs and Networks; Incidence Matrices
13. Orthogonal Vectors and Subspaces

## How to Use

1. Start at the [landing page](index.html) and click "Begin the Course"
2. Browse the [curriculum overview](chapters/index.html) or jump directly to any chapter
3. Each chapter page contains:
   - Core lecture from Gilbert Strang
   - Concept breakdowns from multiple educators
   - Detailed topic explanations
   - Mathematical derivations
   - Learning strategies and mnemonics
   - Visual aids and diagrams
   - Worked examples with step-by-step solutions
   - Practice problems with collapsible solutions
4. Use the "Take Notes" button on any video section to open a floating notepad
5. Navigate with Previous/Next buttons or keyboard shortcuts (`Ctrl+N`, `Ctrl+P`)

## Keyboard Shortcuts

- `Ctrl + N` — Next chapter
- `Ctrl + P` — Previous chapter
- `Escape` — Close note-taking notepad

## Deployment

This site is automatically deployed to GitHub Pages. You can access it at: https://jimmyu2foru18.github.io/Simple-Linear-Algebra/

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request to:
- Add more practice problems
- Improve explanations
- Add visual aids/diagrams
- Enhance the note-taking features
- Fix video IDs for concept breakdowns

## License

This project is licensed under the MIT License

## Acknowledgments

- Prof. Gilbert Strang for the excellent lecture content
- MIT OpenCourseWare for making the lectures available
- Prof. Dave Explains, Paul Cartier, Valerie Hower, and Early Orbit Math for supplementary content
