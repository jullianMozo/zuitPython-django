from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label = 'Username', max_length = 20)
	password = forms.CharField(label = 'Password', max_length = 20)

class AddTaskForm(forms.Form):
	task_name = forms.CharField(label = 'Task_Name', max_length = 50)
	description = forms.CharField(label = 'Description', max_length = 200)

class UpdateTaskForm(forms.Form):
	task_name = forms.CharField(label = 'Task_Name', max_length = 50)
	description = forms.CharField(label = 'Description', max_length = 200)
	status = forms.CharField(label = 'Status', max_length = 50)  


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=20)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
    
class AddEventForm(forms.Form):
	event_name = forms.CharField(label = 'Event name', max_length = 50)
	description = forms.CharField(label = 'Description', max_length = 200)    

