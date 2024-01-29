from django import forms


class registerform(forms.Form):
    firstname=forms.CharField(max_length=15,min_length=8)
    lastname=forms.CharField(max_length=15,min_length=8)
    phone_number=forms.IntegerField()
    Email=forms.EmailField()



class myform(forms.Form):
    name=forms.CharField(min_length=8,max_length=15)
    salary=forms.IntegerField()
    email=forms.EmailField()
    height=forms.DecimalField(max_digits=5,decimal_places=2)
    terms=forms.BooleanField()
    # gender=forms.CharField(choices=[('m','male'),('f','female')])
    resume=forms.FileField()
    password=forms.CharField(min_length=8,max_length=15,widget=forms.PasswordInput)
    Review=forms.CharField(max_length=500,widget=forms.Textarea)
    website=forms.URLField()
    image=forms.ImageField()
    dob=forms.DateField()
    time=forms.TimeField()


class registerf(forms.Form):
    first_name=forms.CharField(max_length=15)
    age=forms.IntegerField()
    emailid=forms.EmailField()
    adress=forms.CharField(max_length=15)


