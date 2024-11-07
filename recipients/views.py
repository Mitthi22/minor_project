from django.shortcuts import render, redirect
from .forms import RecipientRegistrationForm

def register_recipient(request):
    if request.method == 'POST':
        form = RecipientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = RecipientRegistrationForm()
    return render(request, 'register_recipient.html', {'form': form})

def success(request):
    return render(request, 'success.html')

