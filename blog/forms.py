from django import forms
from .models import Add 

class AddForms(forms.ModelForm): # 모델 기반의 폼이라 forms 클래스의 ModelForm을 인자로 넘겨줍니다. 
    class Meta:
        model = Add # 메모 모델을 기반으로 
        fields = ['link','tag','comments'] # 그 안의 제목과 컨텐츠를 form으로 만들어 줍니다. 
				# 전체 필드를 추가하고 싶으면 fields = '__all__' 이렇게 써줍니다.

    