const toastChild = document.querySelectorAll('.my-toast');

if (toastChild) {
  toastChild.forEach((toast) => {
    setTimeout(() => {
      toast.remove();
    }, 3000);
  });
}