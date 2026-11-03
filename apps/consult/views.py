from django.shortcuts import render

# Create your views here.
def consult_submission_view(request):
  return render(request, 'consult/submission.html', {
    'title': 'Pengajuan konsultasi',
  })