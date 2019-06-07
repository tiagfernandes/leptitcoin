from django import forms
from .models import Annonces


class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonces
        fields = '__all__'
        exclude = ('date',)
        # exclude = ('auteur', 'categorie', 'slug')  # Exclura les champs nommés « auteur », « categorie » et « slug »


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea())
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

    def clean_message(self):
        message = self.cleaned_data['message']
        if "escroc" in message:
            raise forms.ValidationError("On ne veut pas entendre parler d'escroquerie !")

        return message
