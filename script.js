// Function to create and manage notes
function createNotepad(videoTitle) {
    // Create a floating notepad container
    const notepad = document.createElement('div');
    notepad.className = 'floating-notepad';
    notepad.style.display = 'none';
    notepad.innerHTML = `
        <div class="notepad-content">
            <div class="notepad-header">
                <h3>Notes: ${videoTitle}</h3>
                <div class="notepad-controls">
                    <button class="minimize-btn">_</button>
                    <span class="close">&times;</span>
                </div>
            </div>
            <textarea id="notepad-${videoTitle.replace(/\s+/g, '-')}" 
                      class="notepad-textarea"
                      placeholder="Take your notes here...">${localStorage.getItem(`notes-${videoTitle}`) || ''}</textarea>
            <button class="save-btn">Save to Desktop</button>
        </div>
    `;

    // Add the notepad to the document body
    document.body.appendChild(notepad);

    // Make the notepad draggable
    const header = notepad.querySelector('.notepad-header');
    let isDragging = false;
    let currentX;
    let currentY;
    let initialX;
    let initialY;
    let xOffset = 0;
    let yOffset = 0;

    header.addEventListener('mousedown', dragStart);
    document.addEventListener('mousemove', drag);
    document.addEventListener('mouseup', dragEnd);

    function dragStart(e) {
        initialX = e.clientX - xOffset;
        initialY = e.clientY - yOffset;
        if (e.target === header) {
            isDragging = true;
        }
    }

    function drag(e) {
        if (isDragging) {
            e.preventDefault();
            currentX = e.clientX - initialX;
            currentY = e.clientY - initialY;
            xOffset = currentX;
            yOffset = currentY;
            setTranslate(currentX, currentY, notepad);
        }
    }

    function dragEnd() {
        isDragging = false;
    }

    function setTranslate(xPos, yPos, el) {
        el.style.transform = `translate3d(${xPos}px, ${yPos}px, 0)`;
    }

    // Handle minimize button
    const minimizeBtn = notepad.querySelector('.minimize-btn');
    minimizeBtn.onclick = () => {
        const content = notepad.querySelector('.notepad-content');
        content.classList.toggle('minimized');
    };

    // Get the close button and add click event
    const closeBtn = notepad.querySelector('.close');
    closeBtn.onclick = () => notepad.style.display = 'none';

    // Save notes when the save button is clicked
    const saveBtn = notepad.querySelector('.save-btn');
    saveBtn.onclick = () => {
        const textarea = notepad.querySelector('.notepad-textarea');
        const content = textarea.value;
        localStorage.setItem(`notes-${videoTitle}`, content);

        // Create a Blob and download it
        const blob = new Blob([content], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${videoTitle.replace(/\s+/g, '_')}_notes.txt`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    };

    return notepad;
}

// Function to add note buttons to all video sections
function addNoteButtons() {
    const videoSections = document.querySelectorAll('.chapter h3');
    
    videoSections.forEach(section => {
        const videoTitle = section.textContent;
        const noteButton = document.createElement('button');
        noteButton.className = 'note-btn';
        noteButton.textContent = 'Take Notes';
        
        // Create notepad modal for this video
        const notepadModal = createNotepad(videoTitle);
        
        // Add click event to the button
        noteButton.onclick = () => {
            notepadModal.style.display = 'block';
        };
        
        // Insert button after the video section title
        section.parentNode.insertBefore(noteButton, section.nextSibling);
    });
}

// Initialize note-taking functionality when the page loads
window.addEventListener('load', addNoteButtons);