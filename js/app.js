(function() {
    'use strict';

    // ============================================
    // CONFIGURATION
    // ============================================
    const CONFIG = {
        notesKey: 'linear_algebra_notes',
        currentChapterKey: 'linear_algebra_current_chapter',
        mathJaxVersion: '3',
        storagePrefix: 'la_notes_'
    };

    // ============================================
    // CHAPTER DATA
    // ============================================
    const CHAPTERS = [
        { id: 'ch01', number: '01', title: 'The Geometry of Linear Equations', file: 'chapter-01.html', description: 'Understanding systems of linear equations through geometric interpretation.' },
        { id: 'ch02', number: '02', title: 'Elimination with Matrices', file: 'chapter-02.html', description: 'Gaussian elimination and matrix operations for solving systems.' },
        { id: 'ch03', number: '03', title: 'Multiplication and Inverse Matrices', file: 'chapter-03.html', description: 'Matrix multiplication rules and the concept of matrix inverses.' },
        { id: 'ch04', number: '04', title: 'Factorization into A = LU', file: 'chapter-04.html', description: 'LU decomposition and its applications in solving linear systems.' },
        { id: 'ch05', number: '05', title: 'Transposes, Permutations, Spaces R^n', file: 'chapter-05.html', description: 'Matrix transposes, permutation matrices, and vector spaces.' },
        { id: 'ch06', number: '06', title: 'Column Space and Nullspace', file: 'chapter-06.html', description: 'Understanding the fundamental subspaces of a matrix.' },
        { id: 'ch07', number: '07', title: 'Solving Ax = 0: Pivot Variables, Special Solutions', file: 'chapter-07.html', description: 'Homogeneous systems and finding the nullspace.' },
        { id: 'ch08', number: '08', title: 'Solving Ax = b: Row Reduced Form R', file: 'chapter-08.html', description: 'Complete solutions to non-homogeneous systems.' },
        { id: 'ch09', number: '09', title: 'Independence, Basis, and Dimension', file: 'chapter-09.html', description: 'Linear independence, basis vectors, and dimension theory.' },
        { id: 'ch10', number: '10', title: 'The Four Fundamental Subspaces', file: 'chapter-10.html', description: 'Column space, nullspace, row space, and left nullspace.' },
        { id: 'ch11', number: '11', title: 'Matrix Spaces; Rank 1; Small World Graphs', file: 'chapter-11.html', description: 'Matrix vector spaces, rank-1 matrices, and network theory.' },
        { id: 'ch12', number: '12', title: 'Graphs, Networks, Incidence Matrices', file: 'chapter-12.html', description: 'Network analysis using graph theory and incidence matrices.' },
        { id: 'ch13', number: '13', title: 'Quiz 1 Review', file: 'chapter-13.html', description: 'Comprehensive review of chapters 1-12 with practice problems.' },
        { id: 'ch14', number: '14', title: 'Orthogonal Vectors and Subspaces', file: 'chapter-14.html', description: 'Orthogonality, projections, and least squares approximation.' },
        { id: 'ch15', number: '15', title: 'Projections onto Subspaces', file: 'chapter-15.html', description: 'Projection matrices and least squares approximation.' },
        { id: 'ch16', number: '16', title: 'Projection Matrices and Least Squares', file: 'chapter-16.html', description: 'Least squares solutions and projection matrix properties.' },
        { id: 'ch17', number: '17', title: 'Orthogonal Matrices and Gram-Schmidt', file: 'chapter-17.html', description: 'Orthogonal bases and the Gram-Schmidt orthogonalization process.' },
        { id: 'ch18', number: '18', title: 'Properties of Determinants', file: 'chapter-18.html', description: 'Determinant properties and their implications for matrix algebra.' },
        { id: 'ch19', number: '19', title: 'Determinant Formulas and Cofactors', file: 'chapter-19.html', description: 'Cofactor expansion and determinant computation methods.' },
        { id: 'ch20', number: '20', title: "Cramer's Rule, Inverse Matrix, and Volume", file: 'chapter-20.html', description: "Cramer's Rule and geometric interpretations of determinants." },
        { id: 'ch21', number: '21', title: 'Eigenvalues and Eigenvectors', file: 'chapter-21.html', description: 'Introduction to eigenvalues, eigenvectors, and their applications.' },
        { id: 'ch22', number: '22', title: 'Diagonalization and Powers of A', file: 'chapter-22.html', description: 'Diagonalizing matrices and computing matrix powers.' },
        { id: 'ch23', number: '23', title: 'Differential Equations and exp(At)', file: 'chapter-23.html', description: 'Matrix exponentials and solving systems of differential equations.' },
        { id: 'ch24', number: '24', title: 'Markov Matrices; Fourier Series', file: 'chapter-24.html', description: 'Markov chains and applications of linear algebra to Fourier series.' },
        { id: 'ch25', number: '25', title: 'Quiz 2 Review', file: 'chapter-25.html', description: 'Comprehensive review of chapters 14-24 with practice problems.' },
        { id: 'ch26', number: '26', title: 'Symmetric Matrices and Positive Definiteness', file: 'chapter-26.html', description: 'Properties of symmetric matrices and positive definite matrices.' },
        { id: 'ch27', number: '27', title: 'Complex Matrices; Fast Fourier Transform', file: 'chapter-27.html', description: 'Complex matrix algebra and the FFT algorithm.' },
        { id: 'ch28', number: '28', title: 'Positive Definite Matrices and Minima', file: 'chapter-28.html', description: 'Optimization applications of positive definite matrices.' },
        { id: 'ch29', number: '29', title: 'Similar Matrices and Jordan Form', file: 'chapter-29.html', description: 'Matrix similarity and the Jordan canonical form.' },
        { id: 'ch30', number: '30', title: 'Singular Value Decomposition', file: 'chapter-30.html', description: 'The SVD theorem and its applications in data science.' },
        { id: 'ch31', number: '31', title: 'Linear Transformations and Their Matrices', file: 'chapter-31.html', description: 'Linear transformations between vector spaces and matrix representations.' },
        { id: 'ch32', number: '32', title: 'Change of Basis; Image Compression', file: 'chapter-32.html', description: 'Change of basis theory and applications to image compression.' },
        { id: 'ch33', number: '33', title: 'Quiz 3 Review', file: 'chapter-33.html', description: 'Comprehensive review of chapters 25-32 with practice problems.' },
        { id: 'ch34', number: '34', title: 'Left and Right Inverses; Pseudoinverse', file: 'chapter-34.html', description: 'Generalized inverses and the Moore-Penrose pseudoinverse.' },
        { id: 'ch35', number: '35', title: 'Final Course Review', file: 'chapter-35.html', description: 'Comprehensive final review of the entire linear algebra course.' }
    ];

    // ============================================
    // MATHJAX CONFIGURATION
    // ============================================
    function initMathJax() {
        if (typeof window.MathJax === 'undefined') {
            console.warn('MathJax not loaded');
            return;
        }

        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']],
                processEscapes: true,
                tags: 'ams'
            },
            svg: {
                fontCache: 'global'
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
                ignoreHtmlClass: 'no-mathjax'
            }
        };

        if (window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise().catch(err => console.warn('MathJax typeset error:', err));
        } else if (window.MathJax.Hub) {
            window.MathJax.Hub.Queue(['Typeset', window.MathJax.Hub]);
        }
    }

    function refreshMathJax() {
        if (typeof window.MathJax === 'undefined') return;
        if (window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise().catch(err => console.warn('MathJax refresh error:', err));
        } else if (window.MathJax.Hub && window.MathJax.Hub.Queue) {
            window.MathJax.Hub.Queue(['Typeset', window.MathJax.Hub]);
        }
    }

    // ============================================
    // PERSISTENT NOTE-TAKING ENGINE
    // ============================================
    const NoteEngine = {
        getAllNotes() {
            try {
                const data = localStorage.getItem(CONFIG.notesKey);
                return data ? JSON.parse(data) : {};
            } catch (e) {
                console.error('Failed to load notes:', e);
                return {};
            }
        },

        saveAllNotes(notes) {
            try {
                localStorage.setItem(CONFIG.notesKey, JSON.stringify(notes));
                return true;
            } catch (e) {
                console.error('Failed to save notes:', e);
                return false;
            }
        },

        getChapterNotes(chapterId) {
            const notes = this.getAllNotes();
            return notes[chapterId] || '';
        },

        saveChapterNotes(chapterId, content) {
            const notes = this.getAllNotes();
            notes[chapterId] = content;
            return this.saveAllNotes(notes);
        },

        deleteChapterNotes(chapterId) {
            const notes = this.getAllNotes();
            delete notes[chapterId];
            return this.saveAllNotes(notes);
        },

        exportNotes(chapterId, filename) {
            const content = this.getChapterNotes(chapterId);
            const blob = new Blob([content], { type: 'text/markdown;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename || `notes_${chapterId}.md`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        },

        importNotes(chapterId, file) {
            return new Promise((resolve, reject) => {
                const reader = new FileReader();
                reader.onload = (e) => {
                    const content = e.target.result;
                    const success = this.saveChapterNotes(chapterId, content);
                    if (success) {
                        resolve(content);
                    } else {
                        reject(new Error('Failed to save imported notes'));
                    }
                };
                reader.onerror = () => reject(new Error('Failed to read file'));
                reader.readAsText(file);
            });
        }
    };

    // ============================================
    // NOTE SIDEBAR UI
    // ============================================
    function createNoteSidebar(chapterId) {
        const existing = document.getElementById('note-sidebar');
        if (existing) return existing;

        const sidebar = document.createElement('div');
        sidebar.id = 'note-sidebar';
        sidebar.className = 'note-sidebar';
        sidebar.setAttribute('data-chapter-id', chapterId);

        const overlay = document.createElement('div');
        overlay.id = 'note-sidebar-overlay';
        overlay.className = 'note-sidebar-overlay';

        const currentNotes = NoteEngine.getChapterNotes(chapterId);

        sidebar.innerHTML = `
            <div class="note-sidebar-header">
                <h3>Study Notes</h3>
                <button class="close" id="close-sidebar" aria-label="Close notes">&times;</button>
            </div>
            <textarea id="sidebar-notes-textarea" placeholder="Type your notes here... They will auto-save as you type.

You can use markdown formatting:
- **bold**
- *italic*
- \`code\`
- Headings with #

Notes are saved per chapter and persist across sessions.">${escapeHtml(currentNotes)}</textarea>
            <div class="note-sidebar-actions">
                <button class="btn-save" id="btn-save-notes">Save</button>
                <button class="btn-export" id="btn-export-notes">Export .md</button>
                <button class="btn-export" id="btn-import-notes">Import</button>
                <button class="btn-clear" id="btn-clear-notes">Clear</button>
            </div>
            <input type="file" id="import-file-input" accept=".md,.txt" style="display:none" />
            <p class="note-status" id="note-status">Notes auto-save locally</p>
        `;

        document.body.appendChild(overlay);
        document.body.appendChild(sidebar);

        const textarea = sidebar.querySelector('#sidebar-notes-textarea');
        const status = sidebar.querySelector('#note-status');
        let saveTimeout;

        function updateStatus(msg) {
            status.textContent = msg;
            setTimeout(() => { status.textContent = 'Notes auto-save locally'; }, 2000);
        }

        function saveNotes() {
            NoteEngine.saveChapterNotes(chapterId, textarea.value);
            updateStatus('Saved at ' + new Date().toLocaleTimeString());
        }

        textarea.addEventListener('input', () => {
            clearTimeout(saveTimeout);
            saveTimeout = setTimeout(saveNotes, 600);
            updateStatus('Typing...');
        });

        sidebar.querySelector('#btn-save-notes').addEventListener('click', saveNotes);

        sidebar.querySelector('#btn-export-notes').addEventListener('click', () => {
            const title = getCurrentChapterTitle();
            const filename = `${title || chapterId}_notes.md`;
            NoteEngine.exportNotes(chapterId, filename);
            updateStatus('Notes exported');
        });

        sidebar.querySelector('#btn-import-notes').addEventListener('click', () => {
            sidebar.querySelector('#import-file-input').click();
        });

        sidebar.querySelector('#import-file-input').addEventListener('change', (e) => {
            const file = e.target.files[0];
            if (!file) return;
            NoteEngine.importNotes(chapterId, file).then(() => {
                textarea.value = NoteEngine.getChapterNotes(chapterId);
                updateStatus('Notes imported');
            }).catch(() => updateStatus('Import failed'));
            e.target.value = '';
        });

        sidebar.querySelector('#btn-clear-notes').addEventListener('click', () => {
            if (confirm('Clear all notes for this chapter? This cannot be undone.')) {
                textarea.value = '';
                NoteEngine.deleteChapterNotes(chapterId);
                updateStatus('Notes cleared');
            }
        });

        function closeSidebar() {
            saveNotes();
            sidebar.classList.remove('open');
            overlay.classList.remove('open');
        }

        sidebar.querySelector('#close-sidebar').addEventListener('click', closeSidebar);
        overlay.addEventListener('click', closeSidebar);

        return sidebar;
    }

    function openNoteSidebar(chapterId) {
        const sidebar = createNoteSidebar(chapterId);
        const overlay = document.getElementById('note-sidebar-overlay');
        sidebar.classList.add('open');
        overlay.classList.add('open');
        sidebar.querySelector('#sidebar-notes-textarea').focus();
    }

    function getCurrentChapterTitle() {
        const h2 = document.querySelector('.chapter h2');
        if (h2) return h2.textContent.trim().replace(/[^a-zA-Z0-9]/g, '_');
        return 'chapter';
    }

    // ============================================
    // NAVIGATION
    // ============================================
    function initNavigation() {
        const currentFile = window.location.pathname.split('/').pop() || 'chapter-01.html';
        const currentIndex = CHAPTERS.findIndex(ch => ch.file === currentFile);

        const prevBtn = document.getElementById('prev-chapter');
        const nextBtn = document.getElementById('next-chapter');
        const indicator = document.getElementById('chapter-indicator');

        if (indicator) {
            const currentChapter = CHAPTERS[currentIndex];
            if (currentChapter) {
                indicator.textContent = `Chapter ${currentChapter.number} of ${CHAPTERS.length}`;
            }
        }

        if (prevBtn) {
            if (currentIndex > 0) {
                prevBtn.href = CHAPTERS[currentIndex - 1].file;
                prevBtn.classList.remove('disabled');
            } else {
                prevBtn.classList.add('disabled');
            }
        }

        if (nextBtn) {
            if (currentIndex < CHAPTERS.length - 1) {
                nextBtn.href = CHAPTERS[currentIndex + 1].file;
                nextBtn.classList.remove('disabled');
            } else {
                nextBtn.classList.add('disabled');
            }
        }

        // Save current chapter to localStorage
        if (currentIndex >= 0) {
            localStorage.setItem(CONFIG.currentChapterKey, CHAPTERS[currentIndex].file);
        }
    }

    function resumeProgress() {
        const lastChapter = localStorage.getItem(CONFIG.currentChapterKey);
        if (lastChapter && window.location.pathname.endsWith('index.html')) {
            const chapter = CHAPTERS.find(ch => ch.file === lastChapter);
            if (chapter) {
                const confirmed = confirm(`Resume where you left off? You were last on Chapter ${chapter.number}: ${chapter.title}`);
                if (confirmed) {
                    window.location.href = lastChapter;
                }
            }
        }
    }

    // ============================================
    // PROGRESS BAR
    // ============================================
    function initProgressBar() {
        const progressBar = document.createElement('div');
        progressBar.className = 'progress-bar';
        progressBar.id = 'progress-bar';
        document.body.prepend(progressBar);

        const updateProgress = debounce(function() {
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = docHeight > 0 ? Math.min((scrollTop / docHeight) * 100, 100) : 0;
            progressBar.style.width = progress + '%';
        }, 10);

        window.addEventListener('scroll', updateProgress, { passive: true });
    }

    // ============================================
    // SEARCH FUNCTIONALITY
    // ============================================
    function initSearch() {
        const searchInput = document.getElementById('search-input');
        if (!searchInput) return;

        const chapters = document.querySelectorAll('.chapter');
        const tocLinks = document.querySelectorAll('.toc a');

        searchInput.addEventListener('input', debounce(function(e) {
            const query = e.target.value.toLowerCase().trim();

            chapters.forEach(chapter => {
                const text = chapter.textContent.toLowerCase();
                chapter.style.display = text.includes(query) || query === '' ? 'block' : 'none';
            });

            tocLinks.forEach(link => {
                const text = link.textContent.toLowerCase();
                link.parentElement.style.display = text.includes(query) || query === '' ? 'list-item' : 'none';
            });
        }, 300));
    }

    // ============================================
    // UTILITY FUNCTIONS
    // ============================================
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function debounce(func, wait) {
        let timeout;
        return function(...args) {
            clearTimeout(timeout);
            timeout = setTimeout(() => func.apply(this, args), wait);
        };
    }

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href === '#') return;
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    }

    // ============================================
    // KEYBOARD SHORTCUTS
    // ============================================
    function initKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl+N: Next chapter
            if (e.ctrlKey && e.key === 'n') {
                e.preventDefault();
                const nextBtn = document.getElementById('next-chapter');
                if (nextBtn && !nextBtn.classList.contains('disabled')) {
                    window.location.href = nextBtn.href;
                }
            }
            // Ctrl+P: Previous chapter
            if (e.ctrlKey && e.key === 'p') {
                e.preventDefault();
                const prevBtn = document.getElementById('prev-chapter');
                if (prevBtn && !prevBtn.classList.contains('disabled')) {
                    window.location.href = prevBtn.href;
                }
            }
            // Escape: Close sidebar
            if (e.key === 'Escape') {
                const sidebar = document.getElementById('note-sidebar');
                const overlay = document.getElementById('note-sidebar-overlay');
                if (sidebar && sidebar.classList.contains('open')) {
                    sidebar.classList.remove('open');
                    overlay.classList.remove('open');
                }
            }
            // Ctrl+Shift+N: Open notes
            if (e.ctrlKey && e.shiftKey && e.key === 'N') {
                e.preventDefault();
                const currentFile = window.location.pathname.split('/').pop();
                const chapter = CHAPTERS.find(ch => ch.file === currentFile);
                if (chapter) {
                    openNoteSidebar(chapter.id);
                }
            }
        });
    }

    // ============================================
    // NOTE BUTTONS
    // ============================================
    function addNoteButtons() {
        const existing = document.querySelector('.note-sidebar-toggle');
        if (existing) return;

        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'note-btn note-sidebar-toggle';
        toggleBtn.textContent = 'Notes';
        toggleBtn.type = 'button';
        toggleBtn.style.cssText = 'position:fixed;bottom:20px;right:20px;z-index:999;padding:0.75rem 1.25rem;background-color:#2980b9;color:white;border:none;border-radius:8px;cursor:pointer;font-size:1rem;box-shadow:0 2px 8px rgba(0,0,0,0.2);transition:all 0.3s ease;';

        toggleBtn.addEventListener('mouseenter', () => {
            toggleBtn.style.backgroundColor = '#2471a3';
            toggleBtn.style.transform = 'translateY(-2px)';
        });
        toggleBtn.addEventListener('mouseleave', () => {
            toggleBtn.style.backgroundColor = '#2980b9';
            toggleBtn.style.transform = 'translateY(0)';
        });

        toggleBtn.addEventListener('click', () => {
            const currentFile = window.location.pathname.split('/').pop();
            const chapter = CHAPTERS.find(ch => ch.file === currentFile);
            const chapterId = chapter ? chapter.id : 'general';
            openNoteSidebar(chapterId);
        });

        document.body.appendChild(toggleBtn);
    }

    // ============================================
    // INITIALIZATION
    // ============================================
    function init() {
        initMathJax();
        initNavigation();
        initProgressBar();
        addNoteButtons();
        initSearch();
        initSmoothScroll();
        initKeyboardShortcuts();
        resumeProgress();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Public API
    window.LinearAlgebra = {
        CHAPTERS,
        NoteEngine,
        getChapter: (id) => CHAPTERS.find(ch => ch.id === id || ch.file === id),
        getCurrentChapter: () => {
            const currentFile = window.location.pathname.split('/').pop();
            return CHAPTERS.find(ch => ch.file === currentFile);
        },
        refreshMath: refreshMathJax,
        openNotes: () => {
            const currentFile = window.location.pathname.split('/').pop();
            const chapter = CHAPTERS.find(ch => ch.file === currentFile);
            if (chapter) openNoteSidebar(chapter.id);
        }
    };
})();
