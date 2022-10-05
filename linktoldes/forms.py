from django import forms


class ContactForm(forms.Form):
    institution = forms.ChoiceField(choices=[('hva', 'Huis van Alijn'), ('dmg', 'Design Museum Gent'), ('industriemuseum', 'Industriemuseum'), ('stam', 'STAM Gent'), ('archief', 'Archief Gent')])
    objectnumber = forms.CharField(required=True)