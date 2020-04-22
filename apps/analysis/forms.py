from django import forms

visualization_type = {
    ('json', 'Json'),
    ('txt-file', 'Txt file'),
    ('table', 'Table'),
}


class URL(forms.Form):
    url = forms.CharField(label='URL', max_length=100)
    type = forms.MultipleChoiceField(required=True, choices=visualization_type)

