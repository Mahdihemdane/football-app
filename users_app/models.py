from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=255)

    USER_TYPES = [
        ('Client', 'Client'),
        ('Organisateur', 'Organisateur'),
        ('Admin', 'Admin'),
    ]
    user_type = models.CharField(max_length=255, choices=USER_TYPES) #Client | Organisateur | Admininstrateur

    addresse = models.CharField(max_length=500)
    
    profile_img = models.ImageField(default='profile_img_default.png', blank=True)
    

    def __str__(self):
        return self.user_type

class Organisateur(Users):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    description = models.CharField(max_length = 1000)

    CATEGORIES = [
        ('ligue 1', 'ligue 1'),
        ('ligue 2', 'ligue 2'),
        ('Coupe du tunisie', 'Coupe du tunisie'),
        ('Amateur ligue', 'Amateur ligue'),
    ]
    categorie = models.CharField(max_length=255, choices=CATEGORIES) # Botola PRO | Botola 2 | Amateur League | Coupe du Trone 
    
    
    def __str__(self):
        return self.categorie+': '+self.nom+' '+self.prenom

class Client(Users):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    
    def __str__(self):
        return 'Client: '+self.prenom+' '+self.nom

class Admininstrateur(Users):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    
    def __str__(self):
        return 'Admin: '+self.prenom+' '+self.nom