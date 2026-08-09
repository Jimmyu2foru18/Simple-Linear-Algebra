# Simple Linear Algebra Course Website

An interactive, multi-page educational platform for Linear Algebra, featuring video lectures and content curated from world-renowned educators.

## Preview

Experience the course live at: [Simple Linear Algebra Course](https://jimmyu2foru18.github.io/Simple-Linear-Algebra/)

## Features

- **35 Structured Chapters**: Complete coverage of Gilbert Strang's MIT 18.06 Linear Algebra series
- **6 Comprehensive Review Sheets**: Structured review materials by topic with formulas, examples, and practice problems
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
│   └── app.js              # Shared JavaScript (navigation, notes, MathJax)
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
│   ├── chapter-12.html     # Graphs, Networks, Incidence Matrices
│   ├── chapter-13.html     # Quiz 1 Review
│   ├── chapter-14.html     # Orthogonal Vectors and Subspaces
│   ├── chapter-15.html     # Projections onto Subspaces
│   ├── chapter-16.html     # Projection Matrices and Least Squares
│   ├── chapter-17.html     # Orthogonal Matrices and Gram-Schmidt
│   ├── chapter-18.html     # Properties of Determinants
│   ├── chapter-19.html     # Determinant Formulas and Cofactors
│   ├── chapter-20.html     # Cramer's Rule, Inverse Matrix, and Volume
│   ├── chapter-21.html     # Eigenvalues and Eigenvectors
│   ├── chapter-22.html     # Diagonalization and Powers of A
│   ├── chapter-23.html     # Differential Equations and exp(At)
│   ├── chapter-24.html     # Markov Matrices; Fourier Series
│   ├── chapter-25.html     # Quiz 2 Review
│   ├── chapter-26.html     # Symmetric Matrices and Positive Definiteness
│   ├── chapter-27.html     # Complex Matrices; Fast Fourier Transform
│   ├── chapter-28.html     # Positive Definite Matrices and Minima
│   ├── chapter-29.html     # Similar Matrices and Jordan Form
│   ├── chapter-30.html     # Singular Value Decomposition
│   ├── chapter-31.html     # Linear Transformations and Their Matrices
│   ├── chapter-32.html     # Change of Basis; Image Compression
│   ├── chapter-33.html     # Quiz 3 Review
│   ├── chapter-34.html     # Left and Right Inverses; Pseudoinverse
│   └── chapter-35.html     # Final Course Review
├── reviews/                 # Structured review sheets by topic
│   ├── index.html           # Review hub
│   ├── review-basics.html   # Linear Systems & Matrix Basics
│   ├── review-subspaces.html # Vector Spaces & Subspaces
│   ├── review-orthogonality.html # Orthogonality & Projections
│   ├── review-determinants.html # Determinants & Cramer's Rule
│   ├── review-eigenvalues.html # Eigenvalues & Diagonalization
│   └── review-advanced.html # Advanced Topics & Final Review
├── README.md
└── AGENTS.md
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

This course covers all 35 lectures from Gilbert Strang's MIT 18.06 Linear Algebra series:

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
12. Graphs, Networks, Incidence Matrices
13. Quiz 1 Review
14. Orthogonal Vectors and Subspaces
15. Projections onto Subspaces
16. Projection Matrices and Least Squares
17. Orthogonal Matrices and Gram-Schmidt
18. Properties of Determinants
19. Determinant Formulas and Cofactors
20. Cramer's Rule, Inverse Matrix, and Volume
21. Eigenvalues and Eigenvectors
22. Diagonalization and Powers of A
23. Differential Equations and exp(At)
24. Markov Matrices; Fourier Series
25. Quiz 2 Review
26. Symmetric Matrices and Positive Definiteness
27. Complex Matrices; Fast Fourier Transform
28. Positive Definite Matrices and Minima
29. Similar Matrices and Jordan Form
30. Singular Value Decomposition
31. Linear Transformations and Their Matrices
32. Change of Basis; Image Compression
33. Quiz 3 Review
34. Left and Right Inverses; Pseudoinverse
35. Final Course Review

## How to Use

1. Start at the [landing page](index.html) and click "Begin the Course"
2. Browse the [curriculum overview](chapters/index.html) or jump directly to any chapter
3. Use the [Review Sheets](reviews/index.html) for structured topic-by-topic review with formulas, examples, and practice problems
4. Each chapter page contains:
   - Core lecture from Gilbert Strang
   - Concept breakdowns from multiple educators
   - Detailed topic explanations
   - Mathematical derivations
   - Learning strategies and mnemonics
   - Visual aids and diagrams
   - Worked examples with step-by-step solutions
   - Practice problems with collapsible solutions
5. Use the "Take Notes" button on any video section to open a floating notepad
6. Navigate with Previous/Next buttons or keyboard shortcuts (`Ctrl+N`, `Ctrl+P`)

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
- Add real video IDs for concept breakdowns

## License

This project is licensed under the MIT License

## Acknowledgments

- Prof. Gilbert Strang for the excellent lecture content
- MIT OpenCourseWare for making the lectures available
- Prof. Dave Explains, Paul Cartier, Valerie Hower, and Early Orbit Math for supplementary content
