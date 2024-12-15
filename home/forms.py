from django import forms

from .models import Test

class TestForm(forms.ModelForm):
    class Meta:
        model = Test  # Link this form to the Test model
        fields = '__all__'  # Include all fields from the model in the form
        #fields = ['firstname','lastname','number','date_of_birth','email','password','paddress','taddress','selectpradesh','gender','message','stream','file','checkbox']
        # Optional: Add widgets for better control over field rendering
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Enter Contact Number'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email Address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'paddress': forms.TextInput(attrs={'placeholder': 'Enter Permanent Address'}),
            'taddress': forms.TextInput(attrs={'placeholder': 'Enter Temporary Address'}),
            'selectpradesh': forms.Select(choices=[
                ('', 'Select'),
                ('Province No. 1', 'Province No. 1'),
                ('Province No. 2', 'Madesh Pradesh'),
                ('Province No. 3', 'Bagmati Pradesh'),
                ('Gandaki Pradesh', 'Gandaki Pradesh'),
                ('Province No. 5', 'Province No. 5'),
                ('Karnali Pradesh', 'Karnali Pradesh'),
                ('Sudurpashchim Pradesh', 'Sudurpashchim Pradesh'),
            ]),  # Customize if choices are provided
            'gender': forms.RadioSelect(choices=[
                ('Male', 'Male'),
                ('Female', 'Female'),
            ]),  # Add RadioSelect widget for gender
            'message': forms.Textarea(attrs={'placeholder': 'Enter Your Message', 'rows': 4}),
            'stream': forms.CheckboxSelectMultiple(
                choices=[
                    ('Science', 'Science'),
                    ('Management', 'Management'),
                    ('Arts', 'Arts'), 
                ]
            ),
            'file': forms.ClearableFileInput(attrs={'multiple': False}),  # Set required to False and add custom data attribute

            'checkbox': forms.CheckboxInput(),
        }


        # Optional: Customize labels or help texts
        labels = {
            'firstname': 'Enter Your First Name',
            'lastname': 'Enter Your Last Name',
            'number': 'Enter Your Contact Number',
            'date_of_birth': 'Enter Your Date of Birth',
            'email': 'Enter Your Email Address',
            'password': 'Enter Your Password',
            'paddress': 'Enter Your Permanent Address',
            'taddress': 'Enter Your Temporary Address',
            'selectpradesh': 'Select Your Pradesh',
            'gender': 'Gender',
            'message': 'Enter Your Message',
            'stream': 'Stream',
            'file': 'Upload Your File',
            'checkbox': 'Accept Terms',
        }
        help_texts = {'checkbox': 'Please check this box to accept the terms.',}

        







""" using (forms.form)
class TestForm(forms.Form):
    firstname = forms.CharField(label="Enter Your First Name", max_length=100)
    lastname = forms.CharField(label="Enter Your Last Name", max_length=100)
    number = forms.IntegerField(label="Enter Your Phone Number")
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))

    email = forms.EmailField(label="Enter Your Email")
    password = forms.CharField(label="Enter Your Password", widget=forms.PasswordInput)
    paddress = forms.CharField(label="Enter Your Permanent Address", max_length=100)
    taddress = forms.CharField(label="Enter Your Temporary Address", max_length=100)
    selectpradesh = forms.ChoiceField(
        label="Select Your Pradesh",
        choices=[
            ('', 'Select'),
            ('Province No. 1', 'Province No. 1'),
            ('Province No. 2', 'Province No. 2'),
            ('Province No. 3', 'Province No. 3'),
            ('Gandaki Pradesh', 'Gandaki Pradesh'),
            ('Province No. 5', 'Province No. 5'),
            ('Karnali Pradesh', 'Karnali Pradesh'),
            ('Sudurpashchim Pradesh', 'Sudurpashchim Pradesh')
        ]
    )
    gender = forms.ChoiceField(
        label="Select Your Gender",
        choices=[('male', 'Male'), ('female', 'Female')],
        widget=forms.RadioSelect
    )
    message = forms.CharField(
        label="Enter Your Message",
        widget=forms.Textarea(attrs={'rows': 3})
    )
    stream = forms.MultipleChoiceField(
        label="Select Your Stream",
        choices=[
            ('Science', 'Science'),
            ('Management', 'Management'),
            ('Arts', 'Arts')
        ],
        widget=forms.CheckboxSelectMultiple
    )
    file = forms.FileField(label="Upload Your File", required=False)
    checkbox = forms.BooleanField(label="Accept The Terms And Policy")
"""