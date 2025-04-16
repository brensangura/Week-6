// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Task 1: Change text content
    const changeTextBtn = document.getElementById('change-text-btn');
    const changeableText = document.getElementById('changeable-text');
    
    changeTextBtn.addEventListener('click', function() {
        changeableText.textContent = "Text successfully changed using JavaScript!";
        changeableText.style.fontStyle = "italic";
    });
    
    // Task 2: Modify CSS styles
    const styleBtn = document.getElementById('style-btn');
    const styleTarget = document.getElementById('style-target');
    
    styleBtn.addEventListener('click', function() {
        styleTarget.classList.toggle('highlight');
        styleTarget.style.color = styleTarget.classList.contains('highlight') ? 'red' : 'black';
    });
    
    // Task 3: Add/remove elements
    const addElementBtn = document.getElementById('add-element-btn');
    const removeElementBtn = document.getElementById('remove-element-btn');
    const elementContainer = document.getElementById('element-container');
    let counter = 1;
    
    addElementBtn.addEventListener('click', function() {
        const newElement = document.createElement('p');
        newElement.textContent = `New element #${counter}`;
        newElement.className = 'dynamic-element';
        elementContainer.appendChild(newElement);
        counter++;
    });
    
    removeElementBtn.addEventListener('click', function() {
        const elements = document.querySelectorAll('.dynamic-element');
        if (elements.length > 0) {
            elements[elements.length - 1].remove();
            counter--;
        } else {
            alert('No more elements to remove!');
        }
    });
});