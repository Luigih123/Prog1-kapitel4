equired. permission.
t staff_member_required
otExist

e, login, logout
er

nator 
reverse 

um, Min, Count

sages
imedelta



"ere are some errors, please check again."


est):

= Member.objects.all()
ts = Payment.objects.all()
_amount = Payment.objects.aggregate(total = Sum('Payment_type_amount'))

ata = {'members':members, 'Payments':payments, 'total_amount':total_am}
return render(request, 'index.html', data)

ired('sito.change_member')
equest, find_duplicates=False):

()