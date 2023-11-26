function submitForm(event) {
    event.preventDefault(); // Prevent form submission

    // Blur the content
    const content = document.querySelector('.container');
    content.classList.add('blur');

    // Display the loading indicator
    const loadingIndicator = document.getElementById('loadingIndicator');
    loadingIndicator.classList.remove('hidden');

    // Update loading text with changing dots
    const loadingText = document.getElementById('loadingText');
    let dotCount = 0;
    const maxDots = 5; // Maximum number of dots in the loading text

    // Function to update the loading text
    function updateLoadingText() {
        dotCount = (dotCount + 1) % (maxDots + 1); 
        const dots = '.'.repeat(dotCount); 
        loadingText.textContent = `Tracking IP's location${dots}`;
    }

    // Function simulating loading effect
    const interval = setInterval(updateLoadingText, 1000); // 
    // Simulate form submission delay (replace with actual form submission)
    setTimeout(() => {
        clearInterval(interval); // Stop updating the text
        loadingText.textContent = `Tracking IP's location...`; 
        event.target.submit(); // Submit the form after delay
    }, 2000); //delay in milliseconds
}

// Event listener for form submission
const trackForm = document.getElementById('trackForm');
trackForm.addEventListener('submit', submitForm);
