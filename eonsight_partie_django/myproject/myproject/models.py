from django.db import models

class Bridge(models.Model):
    name = models.CharField(max_length=255)  # Nom du pont
    location = models.PointField()          # Localisation (Point géographique, nécessite PostGIS)
    status = models.CharField(max_length=50)  # État du pont (par exemple : "actif", "non actif")
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)      # Dernière mise à jour

    def __str__(self):
        return self.name
