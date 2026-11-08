function pictureUploaded(event, idPreview, idPlaceholder) {
  let image = event.target.files[0]
  let preview = document.getElementById(idPreview)
  let placeholder = document.getElementById(idPlaceholder)

  if (image) {
    const reader = new FileReader();

    reader.onload = function(e) {
      preview.src = e.target.result
      placeholder.classList.add('hidden')
      preview.classList.remove('hidden')
    }
    reader.readAsDataURL(image);
  }

}