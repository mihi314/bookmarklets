Working bookmarklet links here: https://mihi314.github.io/bookmarklets

<!--- links start --->
<a href="javascript:%20%28function%20%28%29%20%7B%0A%20%20let%20elements%20%3D%20document.querySelectorAll%28%22body%20%2A%22%29%3B%0A%20%20for%20%28let%20i%20%3D%200%3B%20i%20%3C%20elements.length%3B%20i%2B%2B%29%20%7B%0A%20%20%20%20const%20style%20%3D%20getComputedStyle%28elements%5Bi%5D%29%3B%0A%20%20%20%20if%20%28style.position%20%3D%3D%3D%20%22fixed%22%20%7C%7C%20style.position%20%3D%3D%3D%20%22sticky%22%29%20%7B%0A%20%20%20%20%20%20elements%5Bi%5D.parentNode.removeChild%28elements%5Bi%5D%29%3B%0A%20%20%20%20%7D%0A%20%20%7D%0A%20%20document.querySelector%28%22html%22%29.style.overflow%20%3D%20%22visible%22%3B%0A%20%20document.querySelector%28%22body%22%29.style.overflow%20%3D%20%22visible%22%3B%0A%7D%29%28%29%3B%0A">unstick</a>
<!--- links end --->
