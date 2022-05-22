from django.contrib.auth.models import User
from django import forms
from accounts.models import MyUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput) #widget 옵션을 사용해서 password 속성의 input태그 사용

    class Meta: #modle을 설정하고 fields를 이용해서 입력받을 필드들을 설정
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'phone']

    def clean_password2(self): #각 필드의 clean 메서드가 호출된 후에 호출되는 메서드들. 특별한 유효성 검사나 조작을 원할 시 사용
        cd=self.cleaned_data# cd=유효성 검사를 마친 데이터
        if cd['password'] != cd['password2']: #서로 같은지 비교하는코드
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']