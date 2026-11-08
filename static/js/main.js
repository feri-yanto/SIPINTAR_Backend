$(function () {
  const closeBtnAlert = $('.close-toast')

  closeBtnAlert.on('click', function () {
    let parent = $(this).closest('.my-toast');
    
    var slideOut = parent.outerWidth() + 60;

    parent
    .animate({ left: -18 }, 160, 'linear')
    .animate({ left: slideOut, opacity: 0 }, 420, 'swing')
    .animate({
      height: 0, paddingTop: 0, paddingBottom: 0,
      marginBottom: 0, borderLeftWidth: 0
    }, 260, 'swing', function () { $(this).remove(); });
  })
})