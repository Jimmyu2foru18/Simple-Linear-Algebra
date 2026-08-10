#!/usr/bin/env python3
"""
Script to repair YouTube video links in all 35 chapter HTML files.
Updates core lecture and concept breakdown iframe src and title attributes.
"""

import re
import os

# Base directory for chapters
CHAPTERS_DIR = r"C:\Users\James\Documents\GitHub\Simple-Linear-Algebra\chapters"

# Core lecture mapping: chapter_num -> (video_id, lecture_title)
CORE_LECTURES = {
    1: ("J7DzL2_Na80", "The Geometry of Linear Equations"),
    2: ("QVKj3LADCnA", "Elimination with Matrices"),
    3: ("FX4C-JpTFgY", "Multiplication and Inverse Matrices"),
    4: ("5hO3MrzPa0A", "Factorization into A = LU"),
    5: ("JibVXBElKL0", "Transposes, Permutations, Spaces R^n"),
    6: ("8o5Cmfpeo6g", "Column Space and Nullspace"),
    7: ("VqP2tREMvt0", "Solving Ax = 0"),
    8: ("9Q1q7s1jTzU", "Solving Ax = b"),
    9: ("yjBerM5jWsc", "Independence, Basis, Dimension"),
    10: ("nHlE7EgJFds", "Four Fundamental Subspaces"),
    11: ("2IdtqGM6KWU", "Matrix Spaces; Rank 1"),
    12: ("6-wh6yvk6uc", "Graphs, Networks, Incidence Matrices"),
    13: ("l88D4r74gtM", "Quiz 1 Review"),
    14: ("YzZUIYRCE38", "Orthogonal Vectors and Subspaces"),
    15: ("Y_Ac6KiQ1t0", "Projections onto Subspaces"),
    16: ("osh80YCg_GM", "Projection Matrices and Least Squares"),
    17: ("uNsCkP9mgRk", "Orthogonal Matrices and Gram-Schmidt"),
    18: ("srjxexLishgY", "Properties of Determinants"),
    19: ("23LLB9mNJvc", "Determinant Formulas and Cofactors"),
    20: ("QNpj-gOXW9M", "Cramer's Rule, Inverse Matrix, Volume"),
    21: ("lXNXrLcoerU", "Eigenvalues and Eigenvectors"),
    22: ("13r9QY6cmjc", "Diagonalization and Powers of A"),
    23: ("IZqwi0wJovM", "Differential Equations and exp(At)"),
    24: ("8MF3pz-oYHo", "Markov Matrices; Fourier Series"),
    25: ("sFxA8eIS6tA", "Quiz 2 Review"),
    26: ("umt6BB1nJ4w", "Symmetric Matrices and Positive Definiteness"),
    27: ("M0Sa8fLOajA", "Complex Matrices; Fast Fourier Transform"),
    28: ("vF7eyJ2g3kU", "Positive Definite Matrices and Minima"),
    29: ("z_zYQHmrh08", "Similar Matrices and Jordan Form"),
    30: ("Nx0lRBaXoz4", "Singular Value Decomposition"),
    31: ("Ts3o2I8_Mxc", "Linear Transformations and Their Matrices"),
    32: ("vGkn-3NFGck", "Change of Basis; Image Compression"),
    33: ("HgC1l_6ySkc", "Quiz 3 Review"),
    34: ("Go2aLo7ZOlU", "Left and Right Inverses; Pseudoinverse"),
    35: ("RWvi4Vx4CDc", "Final Course Review"),
}

# Concept breakdown mapping: chapter_num -> [(video_id, source, topic), ...]
CONCEPT_BREAKDOWNS = {
    1: [
        ("csgNflj69-Y", "Prof Dave Explains", "Intro to Linear Algebra"),
        ("rGWcIeCdwGg", "Dr. Valerie Hower", "Introduction to Linear Systems"),
        ("XkY2DOUCWMU", "3Blue1Brown", "Matrix multiplication as composition"),
    ],
    2: [
        ("T2Gtt8WygiU", "Prof Dave Explains", "Elementary Row Operations"),
        ("zIeHOGhWEtc", "Dr. Valerie Hower", "Gauss Jordan Elimination"),
        ("P5GJJ02OG08", "Prof Dave Explains", "Matrix Multiplication"),
    ],
    3: [
        ("P5GJJ02OG08", "Prof Dave Explains", "Matrix Multiplication"),
        ("kWorj5BBy9k", "Prof Dave Explains", "Inverse Matrices"),
        ("3xR9zTx9y74", "Dr. Valerie Hower", "Matrix Product"),
    ],
    4: [
        ("5hO3MrzPa0A", "Gilbert Strang", "Factorization into A = LU"),
        ("T2Gtt8WygiU", "Prof Dave Explains", "Row Operations"),
        ("zIeHOGhWEtc", "Dr. Valerie Hower", "Gauss Jordan"),
    ],
    5: [
        ("EP2ghkO0lSk", "Prof Dave Explains", "Vector Spaces"),
        ("pXp3nQ5exms", "Prof Dave Explains", "Matrix Transpose"),
        ("Zd7wCsUM4pg", "Dr. Valerie Hower", "Intro to Linear Transformations"),
    ],
    6: [
        ("uQhTuRlWMxw", "3Blue1Brown", "Column space and nullspace"),
        ("4nLq5VDS4ok", "Dr. Valerie Hower", "Rank Nullity Theorem"),
        ("EP2ghkO0lSk", "Prof Dave Explains", "Vector Spaces"),
    ],
    7: [
        ("VqP2tREMvt0", "Gilbert Strang", "Solving Ax = 0"),
        ("4nLq5VDS4ok", "Dr. Valerie Hower", "Rank Nullity"),
        ("9kDpbZCK62Y", "Prof Dave Explains", "Linear Independence"),
    ],
    8: [
        ("9Q1q7s1jTzU", "Gilbert Strang", "Solving Ax = b"),
        ("zIeHOGhWEtc", "Dr. Valerie Hower", "Gauss Jordan"),
        ("T2Gtt8WygiU", "Prof Dave Explains", "Row Operations"),
    ],
    9: [
        ("9kDpbZCK62Y", "Prof Dave Explains", "Linear Independence"),
        ("4C9GKyfUQkc", "Prof Dave Explains", "Basis and Dimension"),
        ("L-vWPl7mAjI", "Dr. Valerie Hower", "Bases and Linear Independence"),
    ],
    10: [
        ("nHlE7EgJFds", "Gilbert Strang", "Four Fundamental Subspaces"),
        ("uQhTuRlWMxw", "3Blue1Brown", "Column space and nullspace"),
        ("4nLq5VDS4ok", "Dr. Valerie Hower", "Rank Nullity"),
    ],
    11: [
        ("2IdtqGM6KWU", "Gilbert Strang", "Matrix Spaces; Rank 1"),
        ("EP2ghkO0lSk", "Prof Dave Explains", "Vector Spaces"),
        ("L-vWPl7mAjI", "Dr. Valerie Hower", "Bases"),
    ],
    12: [
        ("6-wh6yvk6uc", "Gilbert Strang", "Graphs, Networks, Incidence Matrices"),
        ("T2Gtt8WygiU", "Prof Dave Explains", "Row Operations"),
        ("zIeHOGhWEtc", "Dr. Valerie Hower", "Gauss Jordan"),
    ],
    13: [
        ("l88D4r74gtM", "Gilbert Strang", "Quiz 1 Review"),
        ("csgNflj69-Y", "Prof Dave Explains", "Intro to Linear Algebra"),
        ("rGWcIeCdwGg", "Dr. Valerie Hower", "Linear Systems"),
    ],
    14: [
        ("YzZUIYRCE38", "Gilbert Strang", "Orthogonal Vectors and Subspaces"),
        ("6nqMegdbxik", "Prof Dave Explains", "Orthogonality"),
        ("vL4Qp4EoJS8", "Dr. Valerie Hower", "Orthogonal Transformations"),
    ],
    15: [
        ("Y_Ac6KiQ1t0", "Gilbert Strang", "Projections onto Subspaces"),
        ("6nqMegdbxik", "Prof Dave Explains", "Orthogonality"),
        ("vL4Qp4EoJS8", "Dr. Valerie Hower", "Orthogonal Transformations"),
    ],
    16: [
        ("osh80YCg_GM", "Gilbert Strang", "Projection Matrices and Least Squares"),
        ("uQhTuRlWMxw", "3Blue1Brown", "Column space"),
        ("zIeHOGhWEtc", "Dr. Valerie Hower", "Gauss Jordan"),
    ],
    17: [
        ("uNsCkP9mgRk", "Gilbert Strang", "Orthogonal Matrices and Gram-Schmidt"),
        ("zHbfZWZJTGc", "Prof Dave Explains", "Gram-Schmidt"),
        ("P4VBYJo8BnY", "Dr. Valerie Hower", "Gram-Schmidt"),
    ],
    18: [
        ("srjxexLishgY", "Gilbert Strang", "Properties of Determinants"),
        ("CcbyMH3Noow", "Prof Dave Explains", "Determinants"),
        ("FzGF-7pIoic", "Dr. Valerie Hower", "Determinants"),
    ],
    19: [
        ("23LLB9mNJvc", "Gilbert Strang", "Determinant Formulas and Cofactors"),
        ("CcbyMH3Noow", "Prof Dave Explains", "Determinants"),
        ("FzGF-7pIoic", "Dr. Valerie Hower", "Determinants"),
    ],
    20: [
        ("QNpj-gOXW9M", "Gilbert Strang", "Cramer's Rule, Inverse Matrix, Volume"),
        ("kWorj5BBy9k", "Prof Dave Explains", "Inverse Matrices"),
        ("uNHRUXh4uH4", "Dr. Valerie Hower", "Inverse of Linear Transformation"),
    ],
    21: [
        ("lXNXrLcoerU", "Gilbert Strang", "Eigenvalues and Eigenvectors"),
        ("TQvxWaXnrqI", "Prof Dave Explains", "Eigenvalues and Eigenvectors"),
        ("M-e2_GS9Ekg", "Dr. Valerie Hower", "Eigenvalues of a Matrix"),
    ],
    22: [
        ("13r9QY6cmjc", "Gilbert Strang", "Diagonalization and Powers of A"),
        ("WTLl03D4TNA", "Prof Dave Explains", "Diagonalization"),
        ("CW9g9XI5pxw", "Dr. Valerie Hower", "Diagonalization"),
    ],
    23: [
        ("IZqwi0wJovM", "Gilbert Strang", "Differential Equations and exp(At)"),
        ("WTLl03D4TNA", "Prof Dave Explains", "Diagonalization"),
        ("Zd7wCsUM4pg", "Dr. Valerie Hower", "Linear Transformations"),
    ],
    24: [
        ("8MF3pz-oYHo", "Gilbert Strang", "Markov Matrices; Fourier Series"),
        ("is1cg5yhdds", "Prof Dave Explains", "Linear Transformations"),
        ("AP-1ukgcG-s", "Dr. Valerie Hower", "Linear Transformations in Geometry"),
    ],
    25: [
        ("sFxA8eIS6tA", "Gilbert Strang", "Quiz 2 Review"),
        ("csgNflj69-Y", "Prof Dave Explains", "Intro to Linear Algebra"),
        ("rGWcIeCdwGg", "Dr. Valerie Hower", "Linear Systems"),
    ],
    26: [
        ("umt6BB1nJ4w", "Gilbert Strang", "Symmetric Matrices and Positive Definiteness"),
        ("DUuTx2nbizM", "Prof Dave Explains", "Complex/Hermitian/Unitary"),
        ("vL4Qp4EoJS8", "Dr. Valerie Hower", "Orthogonal Transformations"),
    ],
    27: [
        ("M0Sa8fLOajA", "Gilbert Strang", "Complex Matrices; Fast Fourier Transform"),
        ("DUuTx2nbizM", "Prof Dave Explains", "Complex/Hermitian"),
        ("Zd7wCsUM4pg", "Dr. Valerie Hower", "Linear Transformations"),
    ],
    28: [
        ("vF7eyJ2g3kU", "Gilbert Strang", "Positive Definite Matrices and Minima"),
        ("DUuTx2nbizM", "Prof Dave Explains", "Complex/Hermitian"),
        ("vL4Qp4EoJS8", "Dr. Valerie Hower", "Orthogonal Transformations"),
    ],
    29: [
        ("z_zYQHmrh08", "Gilbert Strang", "Similar Matrices and Jordan Form"),
        ("WTLl03D4TNA", "Prof Dave Explains", "Diagonalization"),
        ("CW9g9XI5pxw", "Dr. Valerie Hower", "Diagonalization"),
    ],
    30: [
        ("Nx0lRBaXoz4", "Gilbert Strang", "Singular Value Decomposition"),
        ("J9pyaNyM7vE", "Dr. Valerie Hower", "SVD Full Lecture"),
        ("zHbfZWZJTGc", "Prof Dave Explains", "Gram-Schmidt"),
    ],
    31: [
        ("Ts3o2I8_Mxc", "Gilbert Strang", "Linear Transformations and Their Matrices"),
        ("is1cg5yhdds", "Prof Dave Explains", "Linear Transformations"),
        ("Zd7wCsUM4pg", "Dr. Valerie Hower", "Intro to Linear Transformations"),
    ],
    32: [
        ("vGkn-3NFGck", "Gilbert Strang", "Change of Basis; Image Compression"),
        ("HZa1RwFHgwU", "Prof Dave Explains", "Change of Basis"),
        ("kYB8IZa5AuE", "3Blue1Brown", "Linear transformations and matrices"),
    ],
    33: [
        ("HgC1l_6ySkc", "Gilbert Strang", "Quiz 3 Review"),
        ("HZa1RwFHgwU", "Prof Dave Explains", "Change of Basis"),
        ("kYB8IZa5AuE", "3Blue1Brown", "Linear transformations"),
    ],
    34: [
        ("Go2aLo7ZOlU", "Gilbert Strang", "Left and Right Inverses; Pseudoinverse"),
        ("uNHRUXh4uH4", "Dr. Valerie Hower", "Inverse of Linear Transformation"),
        ("kWorj5BBy9k", "Prof Dave Explains", "Inverse Matrices"),
    ],
    35: [
        ("RWvi4Vx4CDc", "Gilbert Strang", "Final Course Review"),
        ("csgNflj69-Y", "Prof Dave Explains", "Intro to Linear Algebra"),
        ("rGWcIeCdwGg", "Dr. Valerie Hower", "Introduction to Linear Systems"),
    ],
}


def make_video_card(video_id, source, topic):
    """Generate a video card HTML block matching existing indentation style."""
    return f'''                <div class="video-card">
                    <div class="video-container">
                        <iframe src="https://www.youtube.com/embed/{video_id}"
                                title="{source} — {topic}"
                                frameborder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                                allowfullscreen>
                        </iframe>
                    </div>
                    <div class="video-card-caption">
                        <h5>{source}</h5>
                        <p>{topic}</p>
                    </div>
                </div>'''


def process_chapter(chapter_num):
    """Process a single chapter HTML file."""
    file_path = os.path.join(CHAPTERS_DIR, f"chapter-{chapter_num:02d}.html")
    
    if not os.path.exists(file_path):
        print(f"WARNING: File not found: {file_path}")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Regex to match iframe tags
    iframe_pattern = re.compile(
        r'(<iframe\s+src=")([^"]+)("\s+title=")([^"]+)("[\s\S]*?allowfullscreen>)',
        re.DOTALL
    )
    
    iframes = list(iframe_pattern.finditer(content))
    
    if len(iframes) == 0:
        print(f"WARNING: No iframes found in chapter-{chapter_num:02d}.html")
        return False
    
    # Replace each iframe by order of appearance
    counter = [0]
    def replace_match(match):
        idx = counter[0]
        counter[0] += 1
        if idx == 0:
            core = CORE_LECTURES[chapter_num]
            new_src = f"https://www.youtube.com/embed/{core[0]}"
            new_title = f"{chapter_num}. {core[1]} — Gilbert Strang"
        elif idx <= 3:
            concept = CONCEPT_BREAKDOWNS[chapter_num][idx - 1]
            new_src = f"https://www.youtube.com/embed/{concept[0]}"
            new_title = f"{concept[1]} — {concept[2]}"
        else:
            return match.group(0)
        return f'{match.group(1)}{new_src}{match.group(3)}{new_title}{match.group(5)}'
    
    content = iframe_pattern.sub(replace_match, content)
    
    # For chapters with fewer than 4 iframes, add missing concept videos
    if len(iframes) < 4:
        missing_count = 4 - len(iframes)
        concepts = CONCEPT_BREAKDOWNS[chapter_num][:missing_count]
        
        # Build video-grid HTML
        video_cards = "\n".join([make_video_card(vid, src, topic) for vid, src, topic in concepts])
        video_grid = f'''            <div class="video-grid">
{video_cards}
            </div>'''
        
        # Insert after <h3>Concept Breakdowns</h3> and before <div class="concept-section">
        pattern_insert = r'(<h3>Concept Breakdowns</h3>\s*)(<div class="concept-section">)'
        replacement = r'\1' + video_grid + '\n' + r'\2'
        
        if re.search(pattern_insert, content):
            content = re.sub(pattern_insert, replacement, content, count=1)
        else:
            # Fallback: insert after the h3 heading
            pattern_insert2 = r'(<h3>Concept Breakdowns</h3>)'
            replacement2 = r'\1\n' + video_grid
            content = re.sub(pattern_insert2, replacement2, content, count=1)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated chapter-{chapter_num:02d}.html")
        return True
    else:
        print(f"No changes needed for chapter-{chapter_num:02d}.html")
        return False


def verify_chapter(chapter_num):
    """Verify a chapter has correct video links."""
    file_path = os.path.join(CHAPTERS_DIR, f"chapter-{chapter_num:02d}.html")
    
    if not os.path.exists(file_path):
        return False, "File not found"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    iframe_pattern = re.compile(
        r'(<iframe\s+src=")([^"]+)("\s+title=")([^"]+)("[\s\S]*?allowfullscreen>)',
        re.DOTALL
    )
    
    iframes = list(iframe_pattern.finditer(content))
    
    if len(iframes) != 4:
        return False, f"Has {len(iframes)} iframes (expected 4)"
    
    errors = []
    
    # Check core lecture
    core = CORE_LECTURES[chapter_num]
    core_src = f"https://www.youtube.com/embed/{core[0]}"
    core_title = f"{chapter_num}. {core[1]} — Gilbert Strang"
    
    if iframes[0].group(2) != core_src:
        errors.append(f"Core src: {iframes[0].group(2)} != {core_src}")
    if iframes[0].group(4) != core_title:
        errors.append(f"Core title: {iframes[0].group(4)} != {core_title}")
    
    # Check concepts
    for i, (vid_id, source, topic) in enumerate(CONCEPT_BREAKDOWNS[chapter_num]):
        expected_src = f"https://www.youtube.com/embed/{vid_id}"
        expected_title = f"{source} — {topic}"
        
        if iframes[i+1].group(2) != expected_src:
            errors.append(f"Concept {i+1} src: {iframes[i+1].group(2)} != {expected_src}")
        if iframes[i+1].group(4) != expected_title:
            errors.append(f"Concept {i+1} title: {iframes[i+1].group(4)} != {expected_title}")
    
    # Check all are youtube embeds
    for i, iframe in enumerate(iframes):
        if "youtube.com/embed/" not in iframe.group(2):
            errors.append(f"Iframe {i} is not a YouTube embed")
    
    if errors:
        return False, "; ".join(errors)
    
    return True, "OK"


def main():
    print("Updating chapter HTML files...")
    updated_count = 0
    for chapter_num in range(1, 36):
        if process_chapter(chapter_num):
            updated_count += 1
    
    print(f"\nUpdated {updated_count} files.")
    
    print("\nVerifying all chapters...")
    all_ok = True
    for chapter_num in range(1, 36):
        ok, msg = verify_chapter(chapter_num)
        status = "OK" if ok else "FAIL"
        print(f"Chapter {chapter_num:02d}: {status} - {msg[:120]}")
        if not ok:
            all_ok = False
    
    if all_ok:
        print("\nAll chapters verified successfully!")
    else:
        print("\nSome chapters failed verification.")
    
    return all_ok


if __name__ == "__main__":
    main()
