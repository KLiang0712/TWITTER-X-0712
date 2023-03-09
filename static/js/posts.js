$(function() {
    // Executed when js-menu-icon.js clicked
    // $(this) self-element namely div.js-menu-icon
    // next(): Next to div.js-menu-icon, namely div.menu
    // toggle(): Switch show and hide 
    $('.js-menu-icon').click(function() {
      // {alert('clicked!!'); })

      $(this).next().toggle()
    })
})