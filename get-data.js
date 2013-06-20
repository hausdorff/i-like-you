// Commands entered into the JS console to get our data out!
// NOT a script that can just be run!


// Run this to start continuously scraping data
function delayedScroll() { scroll(0, document.height); }
var id = setInterval(delayedScroll, 1000);

// Run this when you'd like to stop scraping data
clearInterval(id)

// Write all data to console for copy+paste
document.documentElement.innerHTML
