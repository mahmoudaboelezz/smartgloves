// get element menu
var menu = document.getElementById('menu');
var menu1 = document.getElementById('Path_9');
var menu2 = document.getElementById('Path_10');
var menu3 = document.getElementById('Path_11');
var rect = document.querySelectorAll('rect');

// get element menu-content
var menuContent = document.getElementById('menu-content');
// if nemu is clicked show menu-content and hide menu
menu.addEventListener('click', function () {
    menuContent.classList.toggle('hide');
    if (menuContent.classList.contains('hide')) {
        menu1.style.cssText = "fill: #0B295D; transform: rotate(0) translate(0, 0);";
        menu2.style.cssText = "fill: #0B295D; display: block;";
        menu3.style.cssText = "fill: #0B295D; transform: rotate(0) translate(0, 0);";
        for (var i = 0; i < rect.length; i++) {
            rect[i].style.cssText = "transform: translateX(0px);";
        }
    }
    else {
        menu1.style.cssText = "fill: #FFB066; transform: rotate(45deg) translate(6px, -9px);";
        menu2.style.cssText = "fill: #FFB066; display: none;";
        menu3.style.cssText = "fill: #FFB066; transform: rotate(-46deg) translate(-20px, 0px);";
        for (var i = 0; i < rect.length; i++) {
            rect[i].style.cssText = "transform: translateX(-2px);";
        }
    }
});

//     transform: rotate(46deg) translate(6px, -10px);
// transform: rotate(-46deg) translate(-20px, 0px);


