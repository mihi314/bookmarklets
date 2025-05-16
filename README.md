Working bookmarklet links here: https://mihi314.github.io/bookmarklets

<!--- links start --->
<a href="javascript:%20%28function%20%28%29%20%7B%0A%20%20for%20%28let%20elem%20of%20document.querySelectorAll%28%22body%20%2A%22%29%29%20%7B%0A%20%20%20%20const%20style%20%3D%20getComputedStyle%28elem%29%3B%0A%20%20%20%20if%20%28style.position%20%3D%3D%3D%20%22fixed%22%20%7C%7C%20style.position%20%3D%3D%3D%20%22sticky%22%29%20%7B%0A%20%20%20%20%20%20elem.parentNode.removeChild%28elem%29%3B%0A%20%20%20%20%7D%0A%20%20%7D%0A%20%20for%20%28let%20elem%20of%20document.querySelectorAll%28%22html%2C%20body%22%29%29%20%7B%0A%20%20%20%20elem.style.setProperty%28%22overflow%22%2C%20%22visible%22%2C%20%22important%22%29%3B%0A%20%20%20%20elem.style.setProperty%28%22position%22%2C%20%22static%22%2C%20%22important%22%29%3B%0A%20%20%7D%0A%7D%29%28%29%3B%0A">unstick</a>

<a href="javascript:%20%28function%20%28%29%20%7B%0A%20%20for%20%28let%20button%20of%20document.querySelectorAll%28%22button%22%29%29%20%7B%0A%20%20%20%20button.disabled%20%3D%20false%3B%0A%20%20%7D%0A%7D%29%28%29%3B%0A">zoomable</a>

<a href="javascript:%20%28function%20%28%29%20%7B%0A%20%20for%20%28let%20elem%20of%20document.querySelectorAll%28%22iframe%22%29%29%20%7B%0A%20%20%20%20elem.parentNode.removeChild%28elem%29%3B%0A%20%20%7D%0A%7D%29%28%29%3B%0A">-iframe</a>

<a href="javascript:%20%28function%20%28%29%20%7B%0A%20%20for%20%28let%20button%20of%20document.querySelectorAll%28%22button%22%29%29%20%7B%0A%20%20%20%20button.disabled%20%3D%20false%3B%0A%20%20%7D%0A%7D%29%28%29%3B%0A">enable</a>
<!--- links end --->
