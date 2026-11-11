$(function() {
  const buttonDelete = $('.delete-button-in-table')

  buttonDelete.on('click', function() {
    $('#form-delete-account').attr('action', '/account/delete/'+$(this).data('id'))
    $('#modal_delete .name-placement').text($(this).data('name'))
  })
})