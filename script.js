document.addEventListener('DOMContentLoaded', function() {
    const taglineElement = document.querySelector('.tagline');
    const taglineStatements = [
      "Chat. Learn. Master: Your Virtual TA in the World of Data Structures and Algorithms!",
      "Empowering Your DS & Algorithms Journey: Your Smart Chatbot for Syllabus, Concepts, and Beyond!",
      "Navigate Data Structures and Algorithms with Ease: Your Virtual TA for Course Insights and Problem Solving!",
      // Add more statements as needed
    ];
  
    let currentIndex = 0;
  
    function animateTagline() {
      taglineElement.textContent = taglineStatements[currentIndex];
      currentIndex = (currentIndex + 1) % taglineStatements.length;
    }
  
    setInterval(animateTagline, 3000); // Change statement every 3 seconds
  });
  