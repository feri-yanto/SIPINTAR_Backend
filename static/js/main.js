const TOAST_DURATION = 3000;

$(function () {
  // Pasang timer terpisah untuk setiap toast yang sudah ada
  $('.my-toast').each(function () {
    initToast($(this));
  });

  // Event delegation: berlaku juga untuk toast yang ditambahkan nanti
  $(document).on('click', '.close-toast', function () {
    animateCloseToast($(this).closest('.my-toast'));
  });
});

// Mengatur timer tutup otomatis untuk SATU toast
function initToast($toast, duration = TOAST_DURATION) {
  const timer = setTimeout(() => animateCloseToast($toast), duration);
  $toast.data('timer', timer);
}

function animateCloseToast($toast) {
  if ($toast.data('closing')) return;     // cegah penutupan ganda
  $toast.data('closing', true);

  clearTimeout($toast.data('timer'));     // batalkan timer milik toast ini saja

  const slideOut = $toast.outerWidth() + 60;
  $toast
    .animate({ left: -18 }, 160, 'linear')
    .animate({ left: slideOut, opacity: 0 }, 420, 'swing')
    .animate({
      height: 0, paddingTop: 0, paddingBottom: 0,
      marginBottom: 0, borderLeftWidth: 0
    }, 260, 'swing', function () { $(this).remove(); });
}