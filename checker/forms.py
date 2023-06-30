from django import forms
from .models import SocialMediaURL
from .models import facebookURL
from django import forms


class SocialMediaURLForm(forms.ModelForm):
    class Meta:
        model = SocialMediaURL
        fields = [
            'whoposturl',
            'whoscreenshotimage',
            'hisposturl',
            'hisscreenshotimage',
            'reasonforreporting',
            'specificcause',
            'violated_law',
            'proposed_action',
            
        ]
class facebookURLForm(forms.ModelForm):
    class Meta:
        model = facebookURL
        fields = [
            'url',
            'screenshot_image',
            'reason_of_reporting',
            'specific_cause',
            'digital_act',
            'imp_person_category',
            'priority_category',
            'subcategory',
        ]






