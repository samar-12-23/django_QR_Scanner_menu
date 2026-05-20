from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings




def generate_qr_code(request):

    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['restaurant_name']
            menu_url = form.cleaned_data['menu_url']
            # Here you would generate the QR code using the restaurant_name and menu_url
            # For example, you could use a library like qrcode to create the QR code image
            # and then pass it to the template to display it.

            #Generate QR code logic 
            qr = qrcode.make(menu_url)
            file_name = restaurant_name.replace(" ","_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)

            # Create Image URL
            qr_url=os.path.join(settings.MEDIA_URL, file_name)




            context = {
                'restaurant_name': restaurant_name,
                'qr_url': qr_url,
            }
            return render(request, 'qr_code_result.html', context)

 
    else:
        form = QRCodeForm()
        context={
            'form': form,
        }
    
        return render(request, 'generate_qr_code.html',context) 