from django.shortcuts import render, redirect, get_object_or_404
from annonce.models import Annonces, Categorie
from .forms import AnnonceForm, ContactForm
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def home(request):
    idCategorie = request.GET.get('id_categorie')
    if idCategorie:
        annonces = Annonces.objects.filter(categorie=idCategorie)
    else:
        annonces = Annonces.objects.all()

    categories = Categorie.objects.all()

    return render(request, 'annonce/accueil.html', locals())


def annonce_new(request):
    form = AnnonceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Annonce créée !')

        return redirect('home')

    return render(request, 'annonce/new.html', locals())


def annonce_update(request, id):
    annonce = get_object_or_404(Annonces, id=id)
    form = AnnonceForm(request.POST or None, request.FILES or None, instance=annonce)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Annonce modifiée !')

        return redirect('annonce_update', id)

    return render(request, 'annonce/update.html', locals())


def annonce_read(request, id):
    annonce = get_object_or_404(Annonces, id=id)

    return render(request, 'annonce/read.html', locals())


def annonce_remove(request, id):
    Annonces.objects.get(id=id).delete()
    messages.add_message(request, messages.WARNING, 'Annonce supprimée !')

    return redirect('home')


def annonce_contact(request, id):
    annonce = get_object_or_404(Annonces, id=id)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # send mail
        # send_mail(
        #     form.data['sujet'],
        #     form.data['message'],
        #     form.data['envoyeur'],
        #     [annonce.email],
        #     fail_silently=False,
        # )
        messages.add_message(request, messages.SUCCESS, 'Message envoyé !')
        return redirect('annonce_contact', id)

    return render(request, 'annonce/contact.html', locals())
